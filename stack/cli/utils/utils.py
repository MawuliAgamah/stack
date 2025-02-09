from rich.panel import Panel
import click
import questionary
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich import print as rprint
from pathlib import Path
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
