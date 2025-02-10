from rich.panel import Panel
import click
import questionary
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich import print as rprint
from pathlib import Path
import subprocess
console = Console()


def display_tree_structure(backend_dir: Path, prefix: str = "", is_last: bool = True):
    """Recursively display directory tree structure"""
    # Print current directory/file
    if backend_dir.is_file():
        icon = "📄"
        style = "green"
    else:
        icon = "📁"
        style = "blue"
    
    connector = "└──" if is_last else "├──"
    console.print(f"{prefix}{connector} {icon} {backend_dir.name}", style=style)
    
    if backend_dir.is_dir():
        # Get all items in directory
        items = list(backend_dir.iterdir())
        items.sort(key=lambda x: (x.is_file(), x.name))  # Directories first
        
        # Calculate new prefix for children
        new_prefix = prefix + ("    " if is_last else "│   ")
        
        # Recursively print children
        for i, path in enumerate(items):
            is_last_item = (i == len(items) - 1)
            display_tree_structure(path, new_prefix, is_last_item)

import os
def setup_virtual_env_with_uv(project_dir) -> None:
    """Creates a virtual environment and installs packages using uv"""
    backend_dir = project_dir / "backend"
    venv_dir = backend_dir / ".venv"
    try:
        # Change into backend directory
        os.chdir(str(backend_dir))
        console.print(f"✓ Changed to directory: {backend_dir}")
        
        # Initialize uv in backend directory
        console.print("Initializing uv...")
        subprocess.run(["uv", "init"], check=True)
        console.print("✓ Initialized uv package manager")
        
        # Create virtual environment
        console.print("Creating virtual environment with uv...")
        subprocess.run(["uv", "venv", str(venv_dir)], check=True)
        console.print(f"✓ Created virtual environment at {venv_dir}")
        
        # Install packages from requirements.txt
        requirements_file = backend_dir / "requirements.txt"
        if requirements_file.exists():
            console.print("Installing packages from requirements.txt...")
            subprocess.run([
                "uv",
                "pip",
                "install",
                "-r",
                str(requirements_file)
            ], check=True)
            console.print("✓ Successfully installed all packages")
            
        # Print activation instructions
        console.print("\nTo activate the environment, run:", style="bold yellow")
        console.print(f"cd {backend_dir} && source .venv/bin/activate", style="cyan")
        
    except subprocess.CalledProcessError as e:
        console.print(f"Error: Failed to set up virtual environment: {e}")
        raise
    finally:
        # Change back to original directory
        os.chdir(str(project_dir))

def create_file(file_directory,file_name,template):
    try:
        file_path = file_directory / file_name
        file_path.write_text(template)
        console.print(f"✓ Created {file_name} at {file_path}",style="bold green")
    except Exception as e:
        console.print(f"[bold red] Error creating {file_name}: {str(e)}",style="green")
        raise


def prune(directory):
    """Delete all files i dont need"""
    hello_py_from_vb = directory / "backend/hello.py"
    os.remove(hello_py_from_vb)
    dir2 = directory / "frontend/src/counter.js"
    os.remove(dir2)
    dir2 = directory / "frontend/src/main.js"
    os.remove(dir2)
    dir2 = directory / "frontend/src/javascript.svg"
    os.remove(dir2)
    