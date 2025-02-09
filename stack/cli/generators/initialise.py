import subprocess
from pathlib import Path
import os
from rich.console import Console

console = Console()

from stack.cli.generators.backend import fastapi
from stack.cli.generators.frontend import vanilla
from stack.cli.templates.fast_api_template import FAST_API_TEMPLATES
from rich.console import Console
from rich.spinner import Spinner


def setup_virtual_env_with_uv(project_dir) -> None:
    """Creates a virtual environment and installs packages using uv"""
    backend_dir = project_dir / "backend"
    venv_dir = backend_dir / ".venv"
    backend_dir.mkdir(exist_ok=True)
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



def create_create_docker_compose_file(project_directory):
    pass

from stack.cli.templates.fast_api_template import CONFIGURATION_TEMPLATES
def update_pyproject(project_directory):
    pyproject = project_directory/"backend/pyproject.toml"
    pyproject.write_text(CONFIGURATION_TEMPLATES["pyproject.toml"])



def create_fastapi_project_vanilla_frontend(project_name: str) -> None:
    current_dir = Path(os.getcwd())  
    print(f"FastAPI project '{project_name}' will be created in: {current_dir}")
    with console.status("[bold green] Creating project", spinner="dots") as status:
        req_file = current_dir / "requirements.txt"
        req_file.write_text(FAST_API_TEMPLATES["requirements.txt"])
        setup_virtual_env_with_uv(current_dir)
        update_pyproject(current_dir)
        # vanilla.create_vanilla_frontend(current_dir,status)
        fastapi.create_fastapi_backend(current_dir)
        create_create_docker_compose_file(current_dir)
        #create_database(current_dir)



if __name__=="___main__":
    current_dir = os.getcwd() 
    create_fastapi_project_vanilla_frontend(current_dir)