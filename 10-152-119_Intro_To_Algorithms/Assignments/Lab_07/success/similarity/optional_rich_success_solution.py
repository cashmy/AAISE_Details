from rich import box
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from success_solution import STUDENT_PROFILE, build_ranking_rows


console = Console()


def print_profile_summary():
    tag_text = ", ".join(sorted(STUDENT_PROFILE["tags"]))
    body = (
        f"[bold]Student:[/bold] {STUDENT_PROFILE['name']}\n"
        f"[bold]Goal:[/bold] {STUDENT_PROFILE['goal']}\n"
        f"[bold]Need tags:[/bold] {tag_text}"
    )
    console.print(
        Panel(
            body,
            title="Student Need Profile",
            border_style="cyan",
            box=box.ROUNDED,
        )
    )


def print_representation_table(rows):
    table = Table(
        title="Resource Representation Table",
        box=box.SIMPLE_HEAVY,
        header_style="bold cyan",
    )
    table.add_column("Resource", style="bold")
    table.add_column("Format")
    table.add_column("Tags")

    for row in rows:
        table.add_row(row["name"], row["format"], ", ".join(row["tags"]))

    console.print(table)


def note_style(note):
    if note == "top recommendation":
        return "bold green"
    if note == "close option":
        return "yellow"
    if note == "support option":
        return "cyan"
    return "dim"


def print_ranking_table(rows):
    table = Table(
        title="Similarity Ranking Table",
        box=box.SIMPLE_HEAVY,
        header_style="bold cyan",
    )
    table.add_column("Rank", justify="right")
    table.add_column("Resource")
    table.add_column("Shared Tags")
    table.add_column("Score", justify="right")
    table.add_column("Note")

    for index, row in enumerate(rows, start=1):
        style = note_style(row["note"])
        table.add_row(
            str(index),
            row["name"],
            ", ".join(row["shared_tags"]) if row["shared_tags"] else "-",
            f"{row['score']:.2f}",
            row["note"],
            style=style,
        )

    console.print(table)


def print_final_recommendation(rows):
    top_row = rows[0]
    shared_tags = ", ".join(top_row["shared_tags"])
    body = (
        f"Recommend [bold green]{top_row['name']}[/bold green].\n\n"
        f"It matches [bold]{len(top_row['shared_tags'])}[/bold] of the student's "
        f"need tags and scores [bold]{top_row['score']:.2f}[/bold].\n\n"
        f"[bold]Shared tags:[/bold] {shared_tags}\n\n"
        "This is a recommendation aid, not a claim that it is the only good study choice."
    )
    console.print(
        Panel(
            body,
            title="Final Recommendation",
            border_style="green",
            box=box.ROUNDED,
        )
    )


def print_assumptions_and_limitations():
    table = Table(
        title="Assumptions And Limitations",
        box=box.SIMPLE,
        header_style="bold magenta",
    )
    table.add_column("Type", style="bold")
    table.add_column("Statement")
    table.add_row(
        "Assumption",
        "Simple shared tags are a reasonable way to compare a student's needs to a resource.",
    )
    table.add_row(
        "Assumption",
        "Each tag matters equally, even though a student might value debugging or practice more than other needs.",
    )
    table.add_row(
        "Limitation",
        "The ranking does not measure difficulty level, time required, or whether the student learns better from reading, video, or practice.",
        style="yellow",
    )
    console.print(table)


def print_ai_data_connection():
    console.print(
        Panel(
            "This is a small recommendation example. Many AI and data systems begin "
            "by representing people or items as features, comparing overlap, and "
            "ranking options before a human decides what to use.",
            title="AI/Data Connection",
            border_style="magenta",
            box=box.ROUNDED,
        )
    )


def main():
    rows = build_ranking_rows()

    console.rule("[bold cyan]Lab 07 Rich Success Version - Similarity / Recommendation[/bold cyan]")
    console.print("[yellow]Optional Rich readability version[/yellow]")
    console.print("Option: study resource recommendation by tag overlap\n")

    print_profile_summary()
    print_representation_table(rows)
    print_ranking_table(rows)
    print_final_recommendation(rows)
    print_assumptions_and_limitations()
    print_ai_data_connection()


if __name__ == "__main__":
    main()
