import os


USE_COLOR = os.environ.get("NO_COLOR") is None


class Style:
    RESET = "\033[0m" if USE_COLOR else ""
    BOLD = "\033[1m" if USE_COLOR else ""
    CYAN = "\033[36m" if USE_COLOR else ""
    GREEN = "\033[32m" if USE_COLOR else ""
    YELLOW = "\033[33m" if USE_COLOR else ""


def colorize(text, *styles):
    if not USE_COLOR:
        return text
    return "".join(styles) + text + Style.RESET


def colorized_cell(text, width, *styles):
    return colorize(f"{text:<{width}}", *styles)


SCENARIO_NAME = "Simple contact lookup"


def create_contact_list():
    return [
        {"name": "Ava", "phone": "555-0101", "email": "ava@example.com"},
        {"name": "Luis", "phone": "555-0102", "email": "luis@example.com"},
        {"name": "Mina", "phone": "555-0103", "email": "mina@example.com"},
    ]


def create_contact_dict(contact_list):
    contacts_by_name = {}
    for contact in contact_list:
        contacts_by_name[contact["name"]] = {
            "phone": contact["phone"],
            "email": contact["email"],
        }
    return contacts_by_name


def add_contact_list(contact_list, new_contact):
    contact_list.append(new_contact.copy())


def add_contact_dict(contact_dict, new_contact):
    contact_dict[new_contact["name"]] = {
        "phone": new_contact["phone"],
        "email": new_contact["email"],
    }


def lookup_contact_list(contact_list, name):
    for contact in contact_list:
        if contact["name"] == name:
            return contact.copy()
    return None


def lookup_contact_dict(contact_dict, name):
    if name not in contact_dict:
        return None
    details = contact_dict[name]
    return {"name": name, "phone": details["phone"], "email": details["email"]}


def update_phone_list(contact_list, name, new_phone):
    for contact in contact_list:
        if contact["name"] == name:
            contact["phone"] = new_phone
            return True
    return False


def update_phone_dict(contact_dict, name, new_phone):
    if name not in contact_dict:
        return False
    contact_dict[name]["phone"] = new_phone
    return True


def display_contacts_list(contact_list):
    rows = []
    for contact in contact_list:
        rows.append(f"{contact['name']} -> {contact['phone']} / {contact['email']}")
    return rows


def display_contacts_dict(contact_dict):
    rows = []
    for name in sorted(contact_dict):
        details = contact_dict[name]
        rows.append(f"{name} -> {details['phone']} / {details['email']}")
    return rows


def print_operation_evidence(contact_list, contact_dict):
    print(colorize("OPERATION EVIDENCE", Style.BOLD, Style.CYAN))
    header = f"{'Operation':<18} | {'List of Dictionaries':<36} | {'Dictionary of Dictionaries':<36}"
    print(header)
    print("-" * len(header))

    print(
        f"{'Add Noah':<18} | "
        f"{colorized_cell('Added and found in list', 36, Style.GREEN)} | "
        f"{colorized_cell('Added and found by key', 36, Style.GREEN)}"
    )

    lookup_list = lookup_contact_list(contact_list, "Luis")
    lookup_dict = lookup_contact_dict(contact_dict, "Luis")
    print(f"{'Lookup Luis':<18} | {str(lookup_list):<36} | {str(lookup_dict):<36}")

    print(
        f"{'Update Ava':<18} | "
        f"{str(lookup_contact_list(contact_list, 'Ava')):<36} | "
        f"{str(lookup_contact_dict(contact_dict, 'Ava')):<36}"
    )

    list_display = "; ".join(display_contacts_list(contact_list))
    dict_display = "; ".join(display_contacts_dict(contact_dict))
    print(f"{'Display all':<18} | {list_display:<36} | {dict_display:<36}")
    print()


def print_comparison_table():
    rows = [
        {
            "operation": "Add contact",
            "structure_a": "Append one contact record",
            "structure_b": "Store one contact by name key",
            "better_fit": "Tie",
            "why": "Both are straightforward for a simple add",
        },
        {
            "operation": "Lookup by name",
            "structure_a": "Scan the list until the name matches",
            "structure_b": "Read the contact directly by key",
            "better_fit": "Dictionary of dictionaries",
            "why": "The access pattern is direct lookup by name",
        },
        {
            "operation": "Update phone",
            "structure_a": "Scan for the contact, then change the value",
            "structure_b": "Change one nested value by key",
            "better_fit": "Dictionary of dictionaries",
            "why": "Updates are shorter and clearer when keyed by name",
        },
        {
            "operation": "Display all contacts",
            "structure_a": "Already stored as full records in order",
            "structure_b": "May need formatting or sorting for display",
            "better_fit": "List of dictionaries",
            "why": "Full-record display is slightly more direct here",
        },
    ]

    print(colorize("COMPARISON TABLE", Style.BOLD, Style.CYAN))
    header = (
        f"{'Operation':<20} | {'Structure A':<40} | {'Structure B':<38} | "
        f"{'Better Fit':<24} | Why?"
    )
    print(header)
    print("-" * len(header))
    for row in rows:
        better_fit = row["better_fit"]
        if better_fit == "Dictionary of dictionaries":
            better_fit = colorized_cell(better_fit, 24, Style.GREEN)
        elif better_fit == "List of dictionaries":
            better_fit = colorized_cell(better_fit, 24, Style.YELLOW)
        else:
            better_fit = f"{better_fit:<24}"
        print(
            f"{row['operation']:<20} | "
            f"{row['structure_a']:<40} | "
            f"{row['structure_b']:<38} | "
            f"{better_fit} | "
            f"{row['why']}"
        )
    print()


def print_recommendation():
    print(colorize("RECOMMENDATION", Style.BOLD, Style.CYAN))
    print(
        "For simple contact lookup, the "
        f"{colorize('dictionary-of-dictionaries', Style.GREEN)} structure is "
        "the better overall fit because the main access pattern is finding and "
        "updating contacts by name. The list-of-dictionaries structure still works, "
        "but it needs repeated scanning for those operations."
    )
    print()


def main():
    contact_list = create_contact_list()
    contact_dict = create_contact_dict(contact_list)

    new_contact = {
        "name": "Noah",
        "phone": "555-0104",
        "email": "noah@example.com",
    }

    add_contact_list(contact_list, new_contact)
    add_contact_dict(contact_dict, new_contact)
    update_phone_list(contact_list, "Ava", "555-0199")
    update_phone_dict(contact_dict, "Ava", "555-0199")

    print(colorize("LAB 03 SUCCESS VERSION - DATA STRUCTURE CHOICE", Style.BOLD, Style.CYAN))
    print(SCENARIO_NAME)
    print(colorize("Optional colorized readability version", Style.YELLOW))
    print()
    print_operation_evidence(contact_list, contact_dict)
    print_comparison_table()
    print_recommendation()


if __name__ == "__main__":
    main()
