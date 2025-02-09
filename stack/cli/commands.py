import click
import questionary
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich import print as rprint
from pathlib import Path

from stack.cli.generators.initialise import create_fastapi_project_vanilla_frontend 

console = Console()

def console_final_configguration():
    table = Table(title="Project Configuration")
    table.add_column("Setting", style="cyan")
    table.add_column("Value", style="green")
    table.add_row("Backend", "Django - Full-featured web framework")
    table.add_row("Frontend", "React - Popular UI library")
    table.add_row("Database", "PostgreSQL")
    table.add_row("Features", "\n".join([
    "Docker setup",
    "CI/CD configuration", 
    "Authentication boilerplate",
    "API documentation"
    ]))
    table.add_row("Project Name", "my-awesome-app")


@click.group()
def cli():
    """Interactive web framework setup tool"""
    console.print(Panel.fit("Welcome to Stack - Web Framework Generator",style="bold blue"))

import questionary

@cli.command()
def create_app():
    """Create a new web application"""
    #console.print(Panel.fit("Welcome to Stack - Web Framework Generator",style="bold blue"))

    # Get project configuration through interactive prompts
    backend = questionary.select(
        "Which backend framework would you like to use?",
        choices=[
            "FastAPI - Modern, fast API framework",
            #"Django - Full-featured web framework",
        ]
    ).ask()
    
    frontend = questionary.select(
        "Which frontend framework would you like to use?",
        choices=[
            "Vanilla JS",
            #"React - Popular UI library",
            #"None - Backend only",
        ]
    ).ask()
    
    #database = questionary.select(
    #    "Select your database:",
    #    choices=[
    #        #"PostgreSQL",
    #        #"MySQL",
    #        #"SQLite",
    #    ]
    #).ask()
    
    #features = questionary.checkbox(
    #    "Select additional features:",
    #    choices=[
    #        "Docker setup",
    #        #"CI/CD configuration",
    #        #"API documentation",
    #        #"Authentication boilerplate",
    #    ]
    #).ask()
    
    project_name = questionary.text(
        "What's your project name?",
        validate=lambda text: len(text) >= 2 or "Project name must be at least 2 characters"
    ).ask()

    # Create summary table
    table = Table(title="Project Configuration")
    table.add_column("Setting", style="cyan")
    table.add_column("Value", style="green")
    
    table.add_row("Backend", backend)
    table.add_row("Frontend", frontend)
    #table.add_row("Database", database)
    #table.add_row("Features", "\n".join(features))
    table.add_row("Project Name", project_name)
    
    console.print(table)

    # Confirm and proceed
    if questionary.confirm("Would you like to proceed with this setup?").ask():
        console.print("🚀 Setting up your project...", style="bold green")
        if "FastAPI" in backend and "Vanilla JS" in frontend:
            create_fastapi_project_vanilla_frontend(project_name = project_name)
        else:
            console.print("⚠️ This configurations is not yet supported.", style="bold yellow")
            console.print("Currently available configurations:", style="blue")
            console.print("- FastAPI + Vanilla JS", style="dim")
            console.print("\nFeel free to check back later for more options!", style="green")
    else:
        console.print("Setup cancelled", style="bold red")


from stack.cli.utils import utils
@cli.command()
@click.option('--path', default='.', help='Path to display structure for')
def show_tree(path):
    """Display the project directory structure as a tree"""
    directory = Path(path).resolve()
    if not directory.exists():
        console.print(f"[bold red]Error: Path {directory} does not exist[/]")
        return
    console.print(f"\n[bold cyan]Project Structure for: {directory}[/]")
    utils.display_tree_structure(directory)
    console.print()  # Add newline at end