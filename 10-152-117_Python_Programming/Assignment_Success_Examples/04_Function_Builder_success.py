"""
Assignment 4 Success Example: Function Builder

This example organizes a study-time estimator into functions.
"""


def calculate_total_minutes(session_minutes):
    total = 0

    for minutes in session_minutes:
        total = total + minutes

    return total


def calculate_average(total_minutes, number_of_sessions):
    return total_minutes / number_of_sessions


def describe_goal_status(total_minutes, goal_minutes):
    if total_minutes >= goal_minutes:
        return "Goal met."

    remaining = goal_minutes - total_minutes
    return "Goal not met. Minutes remaining: " + str(remaining)


def display_summary(session_minutes, goal_minutes):
    total = calculate_total_minutes(session_minutes)
    average = calculate_average(total, len(session_minutes))
    status = describe_goal_status(total, goal_minutes)

    print("Study sessions:", session_minutes)
    print("Goal minutes:", goal_minutes)
    print("Total minutes:", total)
    print("Average minutes:", average)
    print(status)


weekly_sessions = [25, 30, 20, 40]
weekly_goal = 120

display_summary(weekly_sessions, weekly_goal)

