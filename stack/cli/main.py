import click
import questionary
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich import print as rprint


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
def make_app():
    """Create a new web application"""
    #console.print(Panel.fit("Welcome to Stack - Web Framework Generator",style="bold blue"))

    # Get project configuration through interactive prompts
    backend = questionary.select(
        "Which backend framework would you like to use?",
        choices=[
            "Django - Full-featured web framework",
            "FastAPI - Modern, fast API framework",
        ]
    ).ask()
    
    frontend = questionary.select(
        "Which frontend framework would you like to use?",
        choices=[
            "React - Popular UI library",
            "Vue - Progressive framework",
            "None - Backend only",
        ]
    ).ask()
    
    database = questionary.select(
        "Select your database:",
        choices=[
            "PostgreSQL",
            "MySQL",
            "SQLite",
        ]
    ).ask()
    
    features = questionary.checkbox(
        "Select additional features:",
        choices=[
            "Docker setup",
            "CI/CD configuration",
            "API documentation",
            "Authentication boilerplate",
        ]
    ).ask()
    
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
    table.add_row("Database", database)
    table.add_row("Features", "\n".join(features))
    table.add_row("Project Name", project_name)
    
    console.print(table)

    # Confirm and proceed
    if questionary.confirm("Would you like to proceed with this setup?").ask():
        console.print("🚀 Setting up your project...", style="bold green")
        # Add your project setup logic here
    else:
        console.print("Setup cancelled", style="bold red")



