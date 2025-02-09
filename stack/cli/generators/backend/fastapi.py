from pathlib import Path
from typing import List
from rich.console import Console
from stack.cli.templates.fast_api_template import FAST_API_TEMPLATES , DOCKERFILE_TEMPLATE

console = Console()


def make_directories(project_dir):
    project_dir = Path(project_dir)
    backend_dir = project_dir / "backend"
    backend_dir.mkdir(exist_ok=True)
    return backend_dir

def create_fastapi_folders(directory):
    folders = {
        "app": directory / "app"
        #"api": directory / "api",
        #"core": directory / "core",
        #"models": directory / "models"
    }
    
    for name, folder in folders.items():
        folder.mkdir(exist_ok=True)
        console.print(f"✓ Created {name} directory at {folder}", style="bold green")


def create_dockerfile(backend_dir: Path) -> None:
    try:
        dockerfile_path = backend_dir / "Dockerfile"
        dockerfile_path.write_text(DOCKERFILE_TEMPLATE)
        console.print(f"✓ Created Dockerfile at {dockerfile_path}", style="bold green")
    except Exception as e:
        console.print(f"[bold red] Error creating Dockerfile: {str(e)}",style="green")
        raise

def write_files_contents(backend_dir):
    """write content to all files"""
    main_file = backend_dir / "app" / "main.py"
    init_file = backend_dir / "app" / "__init__.py"
    main_file.write_text(FAST_API_TEMPLATES["main.py"])
    init_file.write_text(" ")
    console.print(f"✓ Created main.py at {main_file}", style="bold green")
    create_dockerfile(backend_dir)




def create_fastapi_backend(project_dir):
    """Creates the FastAPI project structure"""
    backend_dir = make_directories(project_dir=project_dir)
    create_fastapi_folders(directory=backend_dir)
    write_files_contents(backend_dir)


    



if __name__ == "__main__":
    import os 
    current_dir = "/Users/mawuliagamah/gitprojects/testing"
    from rich.console import Console
    console = Console()
    create_fastapi_backend(current_dir)





