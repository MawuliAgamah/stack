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



CONFIGURATION_TEMPLATES = {
    'pyproject.toml':"""[project]
name = "backend"
version = "0.1.0"
description = "Add your description here"
readme = "README.md"
requires-python = ">=3.9"
dependencies = ['fastapi','uvicorn','python-dotenv']
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
""",
    "main.py": """from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}""",

    "requirements.txt": """fastapi
uvicorn
python-dotenv"""
}
