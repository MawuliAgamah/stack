from pathlib import Path

# cli/generators/frontend/vanilla.py

import subprocess

def set_up_tailwind():
    pass

def create_vanilla_frontend(project_dir: Path) -> None:
    """Creates a Vanilla JS frontend using Vite"""
    try:
        frontend_dir = project_dir / "frontend"
        
        # Change to project directory
        os.chdir(str(project_dir))
        
        console.print("\n[bold blue]Creating Vanilla Frontend with Vite...[/]")
        
        # Run npm create vite@latest
        subprocess.run([
            "npm",
            "create",
            "vite@latest",
            "frontend",  # Directory name
            "--",       # Separator for template arguments
            "--template", "vanilla"  # Specify vanilla template
        ], check=True)
        
        # Change into frontend directory
        os.chdir(str(frontend_dir))
        
        # Install dependencies
        console.print("\nInstalling dependencies...", style="yellow")
        subprocess.run(["npm", "install"], check=True)
        
        console.print("\n[bold green]✓ Vanilla JS frontend created successfully!")
        console.print("\nTo start development server:", style="yellow")
        console.print(f"cd {frontend_dir} && npm run dev", style="cyan")
        
    except subprocess.CalledProcessError as e:
        console.print(f"Error creating frontend: {str(e)}", style="bold red")
        raise
    finally:
        # Return to original directory
        os.chdir(str(project_dir))



if __name__ == "__main__":
    import os 
    from rich.console import Console
    console = Console()
    current_dir = Path("/Users/mawuliagamah/gitprojects/testing")
    create_vanilla_frontend(current_dir)