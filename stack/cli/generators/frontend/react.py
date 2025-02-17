from pathlib import Path
import os 
# cli/generators/frontend/vanilla.py

import subprocess
from rich.console import Console
from stack.cli.templates.backend.fast_api_template import FAST_API_TEMPLATES,FRONTEND_DOCKERFILE
from stack.cli.templates.vanilla_js.front_end_templates import TEMPLATES

console = Console()

class React:

    def __init__(self):
        pass


    def _build_docker_file(self):
        pass

    def __set_up_tailwind(self):
        pass

    def create_react_frontend(project_dir: Path) -> None:
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
            create_dockerfile(frontend_dir)
            
            from stack.cli.utils.utils import create_file
            for k,v in TEMPLATES.items():
                if k == 'index.css':
                    css_dir = frontend_dir/ "src"
                    create_file(file_directory=css_dir,file_name=k,template=v)
                    #console.print(f"✓ Created {k} in src directory", style="green")
                else:
                    create_file(file_directory=frontend_dir,file_name=k,template=v)
                    #console.print(f"✓ Created {k}", style="green")
            console.print("\n[bold green]✓ All configuration files created successfully!")

    def build_front_end(self):
        pass 




def create_react_frontend():
    react = React()
    react.build_front_end()
