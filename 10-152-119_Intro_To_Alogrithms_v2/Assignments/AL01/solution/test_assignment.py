"""Instructor checks with independent expectations for AL01."""

from copy import deepcopy
import contextlib
import io
from unittest.mock import patch

from main import (color_text, validate_ticket, is_open_ticket, needs_follow_up,
                  select_open_tickets, select_follow_up, show_report)
from ticket_data import TICKETS


def check_selection(selector, records, expected_ids, expected_issue_count):
    """Compare selected IDs and issue messages with fixed expectations."""
    selected, issues = selector(records)
    assert [ticket["id"] for ticket in selected] == expected_ids
    assert len(issues) == expected_issue_count
    assert all(isinstance(issue, str) and issue.strip() for issue in issues)


def follow_up_v1(records):
    """Preserve a small instructor-only baseline for revision comparison."""
    # T - Initial follow-up policy before Thursday's alternatives are added.
    selected, issues = [], []
    for ticket in records:
        errors = validate_ticket(ticket)
        if errors:
            issues.extend(errors)
        elif is_open_ticket(ticket) and ticket["age_days"] >= 2:
            selected.append(ticket)
    return selected, issues


def inline_final_selection(records):
    """Provide a pre-extraction equivalent for final-policy refactor parity."""
    # Th - Same final policy before extracting the named rule.
    selected, issues = [], []
    for ticket in records:
        errors = validate_ticket(ticket)
        if errors:
            issues.extend(errors)
        elif (ticket["status"] == "open" and ticket["age_days"] >= 2
              and (ticket["priority"] == "high" or ticket["category"] == "access")):
            selected.append(ticket)
    return selected, issues


def assignment_checks():
    """Verify selection, invalid data, boundaries, revision, and preservation."""
    before = deepcopy(TICKETS)
    # M - Open-ticket baseline; T - initial follow-up; Th - revised follow-up.
    check_selection(select_open_tickets, TICKETS,
                    ["T01", "T02", "T03", "T04", "T06", "T07", "T09"], 3)
    check_selection(follow_up_v1, TICKETS, ["T02", "T03", "T04", "T07", "T09"], 3)
    check_selection(select_follow_up, TICKETS, ["T02", "T04", "T09"], 3)

    base = {"id": "X", "status": "open", "category": "software",
            "age_days": 2, "priority": "high"}
    for age, expected in ((1, False), (2, True), (3, True)):
        ticket = dict(base, age_days=age)
        assert needs_follow_up(ticket) is expected
        check_selection(select_follow_up, [ticket], ["X"] if expected else [], 0)
    for status, category, age, priority, expected in (
        ("open", "access", 3, "normal", True),
        ("open", "software", 3, "normal", False),
        ("closed", "access", 3, "high", False),
        ("open", "access", 1, "normal", False),
    ):
        ticket = dict(base, status=status, category=category,
                      age_days=age, priority=priority)
        check_selection(select_follow_up, [ticket], ["X"] if expected else [], 0)

    for field, bad_value in (("id", ""), ("id", " "),
                             ("status", "waiting"), ("category", "other"),
                             ("priority", "urgent"), ("age_days", True),
                             ("age_days", -1), ("age_days", None),
                             ("age_days", "2"), ("age_days", 2.0)):
        ticket = dict(base)
        ticket[field] = bad_value
        for selector in (select_open_tickets, select_follow_up):
            check_selection(selector, [ticket], [], 1)
    for field in base:
        ticket = dict(base)
        del ticket[field]
        for selector in (select_open_tickets, select_follow_up):
            check_selection(selector, [ticket], [], 1)
    for selector in (select_open_tickets, select_follow_up):
        check_selection(selector, [], [], 0)
        check_selection(selector, [dict(base, status="closed")], [], 0)

    # T - The supplied defect excludes equality; the repaired condition includes it.
    assert (2 > 2) is False
    assert (2 >= 2) is True
    # Th - Extracting the named rule preserves the final policy's answers.
    assert inline_final_selection(TICKETS) == select_follow_up(TICKETS)
    check_selection(select_follow_up, list(reversed(TICKETS)), ["T09", "T04", "T02"], 3)
    assert TICKETS == before
    for selected, issues in (select_follow_up(TICKETS), select_open_tickets(TICKETS)):
        assert all(any(ticket_id in issue for issue in issues)
                   for ticket_id in ("T10", "T11", "T12"))
    output = io.StringIO()
    with contextlib.redirect_stdout(output):
        show_report("Empty", "No records", [], [])
        show_report("Example", "Follow-up", *select_follow_up(TICKETS))
    assert "No tickets match this request." in output.getvalue()
    assert "T02 - Software" in output.getvalue()
    assert "Selected: 3 ticket(s)" in output.getvalue()
    assert "\033[" not in output.getvalue()
    with patch("console_style.sys.stdout.isatty", return_value=True):
        with patch.dict("console_style.os.environ", {}, clear=True):
            assert color_text("Ready", "success") == "\033[92mReady\033[0m"
        with patch.dict("console_style.os.environ", {"NO_COLOR": ""}, clear=True):
            assert color_text("Ready", "success") == "Ready"
        with patch.dict("console_style.os.environ", {"TERM": "dumb"}, clear=True):
            assert color_text("Ready", "success") == "Ready"


def main():
    """Run reference checks without disabled assertions."""
    if not __debug__:
        raise RuntimeError("Run tests without Python optimization (-O).")
    assignment_checks()
    print("Assignment checks passed.")


if __name__ == "__main__":
    main()
