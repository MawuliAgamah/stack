DOCKERFILE_TEMPLATE = """FROM python:3.9

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]"""

FRONTEND_DOCKERFILE = """FROM node:18-alpine as build

WORKDIR /app

# Copy package files
COPY package*.json ./

# Install dependencies
RUN npm ci

# Copy project files
COPY . .

# Build the project
RUN npm run build

# Serve with nginx
FROM nginx:alpine

# Copy built assets from build stage
COPY --from=build /app/dist /usr/share/nginx/html

# Copy nginx config if you have custom configuration
# COPY nginx.conf /etc/nginx/conf.d/default.conf

# Expose port 80
EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]"""

DOCKER_COMPOSE = """version: '3.8'

services:
  frontend:
    build: 
      context: ./frontend
      dockerfile: Dockerfile
    ports:
      - "3000:80"  # Map to 3000 to avoid conflict with backend
    depends_on:
      - backend
  backend:
    build: 
      context: ./backend
      dockerfile: Dockerfile
    ports:
      - "80:80"  # Your backend Dockerfile exposes 80
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
