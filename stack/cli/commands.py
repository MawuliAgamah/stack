import click
import questionary
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich import print as rprint
from pathlib import Path
import questionary
from stack.cli.utils import utils

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
@click.pass_context
def cli(ctx):
    """Interactive web framework setup tool"""
    # Only show welcome message if no subcommand is used
    if ctx.invoked_subcommand is None:
        console.print(Panel.fit("Welcome to Stack - Web Framework Generator", style="bold blue"))
        # You might want to show help here too
        click.echo(ctx.get_help())


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


@cli.command()
@click.option('--frontend', type=click.Choice(['react', 'vanilla']), 
              help='Create only the frontend framework')
@click.option('--backend', type=click.Choice(['fastapi', 'django']),
              help='Create only the backend framework')
def create(frontend, backend):
    """Create a new frontend or backend implementation"""
    if not frontend and not backend:
        console.print("Please specify either --frontend or --backend (or both)", style="bold red")
        return

    if frontend:
        # Ask for frontend folder name with default value
        frontend_folder = questionary.text(
            "What would you like to name your frontend folder?",
            default="frontend"
        ).ask()

        # Use 'frontend' if user just pressed enter (empty string)
        frontend_folder = frontend_folder.strip() or "frontend"

        if frontend == 'react':
            if questionary.confirm("Would you like to proceed with React setup?").ask():
                console.print(f"Creating React application in ./{frontend_folder}/", style="bold green")
                # TODO: Add your React creation logic here
                console.print("✅ React frontend created successfully", style="bold green")
            else:
                console.print("React setup cancelled", style="yellow")
                
        elif frontend == 'vanilla':
            if questionary.confirm("Would you like to proceed with Vanilla JS setup?").ask():
                console.print(f"Creating Vanilla frontend in ./{frontend_folder}/", style="bold green")
                # TODO: Add your Vanilla JS creation logic here
                console.print("✅ Vanilla frontend created successfully", style="bold green")
            else:
                console.print("Vanilla JS setup cancelled", style="yellow")

    if backend:
        # Your backend creation logic here
        pass

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


