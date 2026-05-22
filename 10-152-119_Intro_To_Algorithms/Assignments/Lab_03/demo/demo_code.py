import os


def colorize(text, code):
    if os.getenv("NO_COLOR"):
        return text
    return f"\033[{code}m{text}\033[0m"


def heading(text):
    return colorize(text, "96")


def list_label(text):
    return colorize(text, "93")


def dict_label(text):
    return colorize(text, "92")


def summary_label(text):
    return colorize(text, "95")


def record_attendance_list(attendance_names, student_name):
    attendance_names.append(student_name)


def record_attendance_dict(attendance_counts, student_name):
    if student_name in attendance_counts:
        attendance_counts[student_name] += 1
    else:
        attendance_counts[student_name] = 1


def lookup_attendance_list(attendance_names, student_name):
    count = 0
    for name in attendance_names:
        if name == student_name:
            count += 1
    return count


def lookup_attendance_dict(attendance_counts, student_name):
    return attendance_counts.get(student_name, 0)


def print_representations(list_data, dict_data, label_text):
    print(heading(label_text))
    print(f"{list_label('List representation:')} {list_data}")
    print(f"{dict_label('Dictionary representation:')} {dict_data}")
    print()


def print_comparison_table():
    rows = [
        {
            "operation": "Record one check-in",
            "list_view": "Append a name, then later rescan to count it",
            "dict_view": "Update one stored count by student name",
            "better_fit": "Dictionary",
            "why": "Direct update matches the main task",
        },
        {
            "operation": "Look up Ava's count",
            "list_view": "Scan the whole list and count matches",
            "dict_view": "Read one value by key",
            "better_fit": "Dictionary",
            "why": "Direct lookup is clearer and shorter",
        },
    ]

    print(summary_label("COMPARISON TABLE"))
    header = (
        f"{'Operation':<22} | {'List':<38} | {'Dictionary':<34} | "
        f"{'Better Fit':<12} | Why?"
    )
    print(header)
    print("-" * len(header))
    for row in rows:
        print(
            f"{row['operation']:<22} | "
            f"{row['list_view']:<38} | "
            f"{row['dict_view']:<34} | "
            f"{row['better_fit']:<12} | "
            f"{row['why']}"
        )
    print()


def main():
    attendance_names = ["Ava", "Luis", "Ava", "Mina"]
    attendance_counts = {"Ava": 2, "Luis": 1, "Mina": 1}
    student_name = "Ava"

    print(heading("LAB 03 DEMO - DATA STRUCTURE CHOICE"))
    print()
    print("The demo compares attendance tracking with a list and a dictionary.")
    print("Core operation: record one more attendance check-in for Ava.")
    print()

    print_representations(attendance_names, attendance_counts, "BEFORE CHECK-IN")

    record_attendance_list(attendance_names, student_name)
    record_attendance_dict(attendance_counts, student_name)

    print_representations(attendance_names, attendance_counts, "AFTER CHECK-IN")

    list_count = lookup_attendance_list(attendance_names, student_name)
    dict_count = lookup_attendance_dict(attendance_counts, student_name)

    print(summary_label("LOOKUP RESULT"))
    print(f"List count for {student_name}: {list_count}")
    print(f"Dictionary count for {student_name}: {dict_count}")
    print()

    print_comparison_table()
    print("Reminder: the better fit depends on which operations matter most.")


if __name__ == "__main__":
    main()
