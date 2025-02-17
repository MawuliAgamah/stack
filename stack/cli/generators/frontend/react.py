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

    def _install_additonal_dependencies(self):
        console.print("\nInstalling additional React dependencies...", style="yellow")
        subprocess.run([
                "npm",
                "install",
                "react-router-dom",  # For routing
                "axios",             # For API calls
                "@tailwindcss/forms",# For form styling
                "tailwindcss",       # For styling
                "postcss",           # Required for Tailwind
                "autoprefixer",      # Required for Tailwind
            ], check=True)

    def create_react_frontend(self,project_dir: Path,folder_name:str) -> None:
        """Create a React JS FrontEnd using React"""
        try:
            folder_name = str(folder_name)
            project_path = Path(project_dir)
            frontend_dir = project_dir + '/' + folder_name
            os.mkdir(frontend_dir)
            
            # Change to project directory
            os.chdir(str(project_dir))
            
            console.print("\n[bold blue]Creating react js Frontend with Vite...[/]")
            
            # Run npm create vite@latest
            subprocess.run([
                "npm",
                "create",
                "vite@latest",
                folder_name,  # Directory name
                "--",       # Separator for template arguments
                "--template", "react"  # Specify vanilla template
            ], check=True)
            
            # Change into frontend directory
            os.chdir(str(frontend_dir))

            console.print("\nInstalling dependencies...", style="yellow")
            subprocess.run(["npm", "install"], check=True)

            self._install_additonal_dependencies()
            
            console.print("\nTo start development server:", style="yellow")
            console.print(f"cd {frontend_dir} && npm run dev", style="cyan")

        except subprocess.CalledProcessError as e:
                console.print(f"\n[bold red]Error creating React frontend: {str(e)}[/]")
                raise
        except Exception as e:
                console.print(f"\n[bold red]Unexpected error: {str(e)}[/]")
                raise

    def build_front_end(self,project_dir,folder_name):
        self.create_react_frontend(project_dir,folder_name)




def create_react_frontend(project_dir: Path,folder_name:str):
    react = React()
    react.build_front_end(project_dir,folder_name)
