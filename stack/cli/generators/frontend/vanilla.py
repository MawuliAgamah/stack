from pathlib import Path

# cli/generators/frontend/vanilla.py
def create_vanilla_frontend(project_dir) -> None:
    """Creates vanilla frontend structure"""
    project_dir = Path(project_dir)
    frontend_dir = project_dir / "frontend"
    print(frontend_dir)
    return frontend_dir




if __name__ == "__main__":
    import os 
    from rich.console import Console
    console = Console()
    current_dir = "/Users/mawuliagamah/gitprojects/testing"
    with console.status("[bold green] Creating project", spinner="dots") as status:
        create_vanilla_frontend(current_dir,status)