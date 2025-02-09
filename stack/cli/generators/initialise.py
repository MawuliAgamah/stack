import subprocess
from pathlib import Path
import os
from rich.console import Console

console = Console()

from stack.cli.generators.backend import fastapi
from stack.cli.generators.frontend import vanilla
from stack.cli.utils.utils import setup_virtual_env_with_uv
from stack.cli.templates.fast_api_template import FAST_API_TEMPLATES
from rich.console import Console
from rich.spinner import Spinner
from stack.cli.templates.fast_api_template import CONFIGURATION_TEMPLATES


def create_create_docker_compose_file(project_directory):
    pass

def update_pyproject(project_directory):
    pyproject = project_directory/"backend/pyproject.toml"
    pyproject.write_text(CONFIGURATION_TEMPLATES["pyproject.toml"])

from stack.cli.templates.fast_api_template import FAST_API_TEMPLATES , DOCKER_COMPOSE
def create_create_docker_compose_file(dir: Path) -> None:
    try:
        docker_compose_path = dir / "docker-compose.yml"
        docker_compose_path.write_text(DOCKER_COMPOSE)
        console.print(f"✓ Created Dockerfile at {docker_compose_path}", style="bold green")
    except Exception as e:
        console.print(f"[bold red] Error creating Dockerfile: {str(e)}",style="green")
        raise

def create_fastapi_project_vanilla_frontend(project_name: str) -> None:
    current_dir = Path(os.getcwd()) 
    print(f"FastAPI project '{project_name}' will be created in: {current_dir}") 
    backend_dir = current_dir / "backend"
    backend_dir.mkdir(exist_ok=True)
    frontend_dir = current_dir / "frontend"
    frontend_dir.mkdir(exist_ok=True)
   # with console.status("[bold green] Creating project", spinner="dots") as status:
    req_file = backend_dir / "requirements.txt"
    req_file.write_text(FAST_API_TEMPLATES["requirements.txt"])
    setup_virtual_env_with_uv(current_dir)
    update_pyproject(current_dir)
    fastapi.create_fastapi_backend(current_dir)
    vanilla.create_vanilla_frontend(current_dir)
    create_create_docker_compose_file(current_dir)


if __name__=="___main__":
    current_dir = os.getcwd() 
    create_fastapi_project_vanilla_frontend(current_dir)