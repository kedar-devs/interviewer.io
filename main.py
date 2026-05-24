import questionary
from questionary import Choice
from rich.console import Console
from rich.panel import Panel
from interviewer import take_interview
import asyncio


def main():
    console = Console()

    # Styled text
    console.print("[bold green]✓[/] Let's begin!", style="cyan")

    # Boxed banner
    console.print(Panel.fit("Welcome to Interviewer", style="bold magenta"))

    choices = [
        Choice(title=[("fg:green bold", "Easy")], value="Easy"),
        Choice(title=[("fg:yellow bold", "Medium")], value="Medium"),
        Choice(title=[("fg:red bold", "Hard")], value="Hard"),
    ]

    dsa_topics = [
        Choice(title=[("fg:blue bold", "Any")], value="Any"),
        Choice(title=[("fg:blue bold", "Arrays")], value="Arrays"),
        Choice(title=[("fg:blue bold", "Linked Lists")], value="Linked Lists"),
        Choice(title=[("fg:blue bold", "Stacks and Queues")], value="Stacks and Queues"),
        Choice(title=[("fg:blue bold", "Trees and Graphs")], value="Trees and Graphs"),
        Choice(title=[("fg:blue bold", "Hashing")], value="Hashing"),
        Choice(title=[("fg:blue bold", "Sorting and Searching")], value="Sorting and Searching"),
        Choice(title=[("fg:blue bold", "Dynamic Programming")], value="Dynamic Programming"),
        Choice(title=[("fg:blue bold", "Recursion and Backtracking")], value="Recursion and Backtracking"),
        Choice(title=[("fg:blue bold", "Greedy Algorithms")], value="Greedy Algorithms"),
        Choice(title=[("fg:blue bold", "Bit Manipulation")], value="Bit Manipulation"),
    ]

    choice = questionary.select(
        "Choose difficulty level:",
        choices=choices
    ).ask()

    selected_dsa_topics = questionary.select(
        "Select DSA topics to include (optional):",
        choices=dsa_topics
    ).ask()

    if choice is None:
        print("Nothing selected.")
        return

    print(f"You picked: {choice}")
    print(f"you picked {selected_dsa_topics} as your topic of intrest")

    asyncio.run(take_interview(choice, selected_dsa_topics))


if __name__ == "__main__":
    main()