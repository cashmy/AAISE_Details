"""
Assignment 7 Success Example: Reading Structured Code

This example compares a function-based version and a class-based version of
a simple reading-goal tracker.
"""


def add_reading_session(session_list, title, minutes):
    session_list.append({
        "title": title,
        "minutes": minutes,
    })


def show_reading_sessions(session_list):
    print("Function-based reading sessions:")

    for session in session_list:
        print("-", session["title"], "-", session["minutes"], "minutes")


function_sessions = []
add_reading_session(function_sessions, "Python chapter", 35)
add_reading_session(function_sessions, "Debugging notes", 20)
show_reading_sessions(function_sessions)


class ReadingGoalTracker:
    def __init__(self, goal_minutes):
        self.goal_minutes = goal_minutes
        self.sessions = []

    def add_session(self, title, minutes):
        self.sessions.append({
            "title": title,
            "minutes": minutes,
        })

    def total_minutes(self):
        total = 0

        for session in self.sessions:
            total = total + session["minutes"]

        return total

    def show_summary(self):
        print("\nClass-based reading goal tracker:")

        for session in self.sessions:
            print("-", session["title"], "-", session["minutes"], "minutes")

        total = self.total_minutes()
        print("Goal minutes:", self.goal_minutes)
        print("Total minutes:", total)

        if total >= self.goal_minutes:
            print("Status: goal met")
        else:
            print("Status: keep reading")


tracker = ReadingGoalTracker(60)
tracker.add_session("Python chapter", 35)
tracker.add_session("Debugging notes", 20)
tracker.add_session("Practice problems", 15)
tracker.show_summary()

