from pathlib import Path
from typing import List

FASTAPI_TEMPLATES = {
"main.py": '''
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}
''',
    "requirements.txt": '''
fastapi
uvicorn
python-dotenv
'''
}

def create_fastapi_backend(project_dir: Path) -> None:(project_dir: Path, features: List[str]):
    """Creates the FastAPI project structure"""
    backend_dir = project_dir / "backend"
    backend_dir.mkdir(exist_ok=True)
    
    # Create FastAPI specific directories
    (backend_dir / "app").mkdir(exist_ok=True)
    (backend_dir / "api").mkdir(exist_ok=True)
    (backend_dir / "core").mkdir(exist_ok=True)
    (backend_dir / "models").mkdir(exist_ok=True)
    
    # Create initial files from templates
    (backend_dir / "app" / "main.py").write_text(FASTAPI_TEMPLATES["main.py"])
    (backend_dir / "requirements.txt").write_text(FASTAPI_TEMPLATES["requirements.txt"])
    
    return backend_dir





