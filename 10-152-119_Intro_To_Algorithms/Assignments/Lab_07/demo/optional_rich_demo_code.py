from rich import box
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from demo_code import REFERENCE_SONG, build_ranking_rows


console = Console()


def print_reference_panel():
    body = (
        f"[bold]Reference song:[/bold] {REFERENCE_SONG['name']}\n"
        f"[bold]Reference tags:[/bold] {', '.join(sorted(REFERENCE_SONG['tags']))}"
    )
    console.print(
        Panel(
            body,
            title="Reference Item",
            border_style="cyan",
            box=box.ROUNDED,
        )
    )


def print_feature_table(ranking_rows):
    table = Table(
        title="Item-Feature Table",
        box=box.SIMPLE_HEAVY,
        header_style="bold cyan",
    )
    table.add_column("Song", style="bold")
    table.add_column("Tags")

    for row in ranking_rows:
        table.add_row(row["name"], ", ".join(row["tags"]))

    console.print(table)


def print_ranking_table(ranking_rows):
    table = Table(
        title="Ranking Table",
        box=box.SIMPLE_HEAVY,
        header_style="bold cyan",
    )
    table.add_column("Rank", justify="right")
    table.add_column("Song")
    table.add_column("Shared Tags")
    table.add_column("Score", justify="right")
    table.add_column("Note")

    for index, row in enumerate(ranking_rows, start=1):
        style = "bold green" if index == 1 else ""
        table.add_row(
            str(index),
            row["name"],
            ", ".join(row["shared_tags"]) if row["shared_tags"] else "-",
            f"{row['score']:.2f}",
            "top match" if index == 1 else "candidate",
            style=style,
        )

    console.print(table)


def print_summary(ranking_rows):
    top_row = ranking_rows[0]
    body = (
        "[bold]Assumption 1:[/bold] shared tags are a reasonable proxy for "
        "similarity in this tiny example.\n"
        "[bold]Assumption 2:[/bold] all tags matter equally in the score, even "
        "though some music features may matter more than others.\n"
        "[bold yellow]Limitation:[/bold yellow] the ranking ignores lyrics, "
        "artist preference, song length, and many other factors that could "
        "change a real recommendation.\n\n"
        f"[bold green]Top recommendation:[/bold green] {top_row['name']} "
        f"with score {top_row['score']:.2f}"
    )
    console.print(
        Panel(
            body,
            title="Assumption And Limit Summary",
            border_style="magenta",
            box=box.ROUNDED,
        )
    )


def main():
    ranking_rows = build_ranking_rows()

    console.rule("[bold cyan]Lab 07 Rich Demo - Similarity, Ranking, And Hashing[/bold cyan]")
    console.print("[yellow]Optional Rich demo version[/yellow]\n")
    print_reference_panel()
    print_feature_table(ranking_rows)
    print_ranking_table(ranking_rows)
    print_summary(ranking_rows)


if __name__ == "__main__":
    main()
