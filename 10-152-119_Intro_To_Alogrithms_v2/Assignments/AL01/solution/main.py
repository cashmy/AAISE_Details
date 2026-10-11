"""Instructor reference: select useful help-desk lists with simple Python."""

from console_style import color_text
from ticket_data import TICKETS


# M - Establish trusted data before building the open-ticket view.
def validate_ticket(ticket):
    """Return readable messages for fields that cannot be trusted."""
    issues = []
    label = ticket.get("id")
    if not isinstance(label, str) or not label.strip():
        label = "Unidentified ticket"
        issues.append(f"{label}: provide a nonempty ticket ID.")
    for field, allowed in (
        ("status", ("open", "closed")),
        ("category", ("software", "network", "access")),
        ("priority", ("low", "normal", "high")),
    ):
        if ticket.get(field) not in allowed:
            issues.append(f"{label}: check {field}; use {', '.join(allowed)}.")
    age = ticket.get("age_days")
    if type(age) is not int or age < 0:
        issues.append(f"{label}: provide age in whole days, zero or greater.")
    return issues


def is_open_ticket(ticket):
    """Identify an open ticket after validation."""
    return ticket["status"] == "open"


def needs_follow_up(ticket):
    """Apply the final policy to a previously validated ticket."""
    # T - Initial policy: open AND age_days >= 2 (exactly 2 qualifies).
    # Tuesday's version ends after the age condition; tests preserve that baseline.
    # Th - Add the grouped alternatives without bypassing status or age.
    return (is_open_ticket(ticket)
            and ticket["age_days"] >= 2
            and (ticket["priority"] == "high" or ticket["category"] == "access"))


# M - The open view remains unchanged during later follow-up revisions.
def select_open_tickets(records):
    """Collect valid open tickets and messages for invalid records."""
    selected = []
    issues = []
    for ticket in records:
        errors = validate_ticket(ticket)
        if errors:
            issues.extend(errors)
        elif is_open_ticket(ticket):
            selected.append(ticket)
    return selected, issues


# T - Add the follow-up collection using the initial policy.
# Th - Reuse this loop with the revised rule; extracting the named rule is
# a behavior-preserving refactor, unlike adding the new policy conditions.
def select_follow_up(records):
    """Collect final-policy tickets and messages for invalid records."""
    selected = []
    issues = []
    for ticket in records:
        errors = validate_ticket(ticket)
        if errors:
            issues.extend(errors)
        elif needs_follow_up(ticket):
            selected.append(ticket)
    return selected, issues


def show_report(title, policy, selected, issues):
    """Present useful ticket details and clear next actions."""
    print("\n" + color_text(title, "heading"))
    print(color_text("=" * len(title), "heading"))
    print("Request:", policy)
    if not selected:
        print(color_text("  No tickets match this request.", "caution"))
    for ticket in selected:
        print(color_text(f"  {ticket['id']} - {ticket['category'].title()} - "
                         f"{ticket['age_days']} day(s) old - {ticket['priority'].title()} priority",
                         "success"))
    print(color_text(f"Selected: {len(selected)} ticket(s)",
                     "success" if selected else "caution"))
    if issues:
        print("\n" + color_text("Records needing checking", "caution"))
        for issue in issues:
            print(color_text("  " + issue, "caution"))


def main():
    """Display the open view and final follow-up list."""
    # M - First useful result: valid open tickets.
    selected, issues = select_open_tickets(TICKETS)
    show_report("Help Desk - Open Tickets", "All valid open tickets", selected, issues)
    # T - Add the initial follow-up report; Th updates its rule and policy label.
    selected, issues = select_follow_up(TICKETS)
    show_report("Help Desk - Follow-Up",
                "Open, at least 2 days old, and high priority or access category",
                selected, issues)


if __name__ == "__main__":
    main()
