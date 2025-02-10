DOCKERFILE_TEMPLATE = """FROM python:3.9

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]"""

FRONTEND_DOCKERFILE = """FROM node:20-alpine 

WORKDIR /app

COPY package.json . 

RUN  npm install 

COPY package*.json ./
COPY . .

EXPOSE 80

CMD ["npm","run","dev"]

FROM node:18-alpine as build

WORKDIR /app"""

DOCKER_COMPOSE = """version: '3.8'

services:
  frontend:
    build:
      context: ./frontend
      dockerfile: Dockerfile
    ports:
      - "3000:3000"  
    depends_on:
      - backend
    environment:
      - PORT=3000
      - HOST=0.0.0.0


  backend:
    build:
      context: ./backend
      dockerfile: Dockerfile
    ports:
      - "8080:80"  # Changed from 3000 to 8080
    environment:
      - PORT=80
      - HOST=0.0.0.0

"""


########################################################################
# FAST API BASE TEMPLATES 
########################################################################

CONFIGURATION_TEMPLATES = {'pyproject.toml':"""[project]
name = "backend"
version = "0.1.0"
description = "Add your description here"
readme = "README.md"
requires-python = ">=3.9"
dependencies = ['fastapi','uvicorn','python-dotenv','fastapi[standard]]
"""
}

FAST_API_TEMPLATES = {
    "requirements.txt":"""
    fastapi
    uvicorn
    pydantic
    SQLAlchemy
    python-dotenv
    SQLAlchemy
    pydantic
    fastapi[standard]
""",
    "main.py": """from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}""",

    "requirements.txt": """fastapi
uvicorn
python-dotenv""",
'pyproject.toml':"""[project]
name = "backend"
version = "0.1.0"
description = "Add your description here"
readme = "README.md"
requires-python = ">=3.9"
dependencies = ['fastapi','uvicorn','python-dotenv','fastapi[standard]]
"""
}


########################################################################
# FAST API WITH ADDONS 
########################################################################

PY_PROJECT__TOML_JINJA_TEMPLATES = """[project]
name = "backend"
version = "0.1.0"
description = "Add your description here"
readme = "README.md"
requires-python = ">=3.9"
dependencies = ['fastapi','uvicorn','python-dotenv','fastapi[standard]]
"""

REQUIREMENTS_TXT_TEMPLATE = """
    fastapi
    uvicorn
    pydantic
    SQLAlchemy
    python-dotenv
    SQLAlchemy
    pydantic
    fastapi[standard]
"""

MAIN_PY_TEMPLATE = """
from fastapi import FastAPI
from fastapi.templating import Jinta2Templates 
app = FastAPI()
templates = Jinta2Templates(directory="templates")
@app.get("/")
async def root():
    return {"message": "Hello World"}
"""

FAST_API_FILES= {
    "requirements.txt":REQUIREMENTS_TXT_TEMPLATE,
    "pyproject.toml":PY_PROJECT__TOML_JINJA_TEMPLATES,
    "main.py": MAIN_PY_TEMPLATE
}

FAST_API_FOLDERS = {
    'backend':
    ['app','templates']
  }