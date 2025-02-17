BACKEND_DOCKERFILE = """FROM python:3.9

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

DOCKER_CONFIGURATIONS = {
    'frontend_dockerfile':FRONTEND_DOCKERFILE,
    'backend_dockerfile':BACKEND_DOCKERFILE,
    'docker_compose':DOCKER_COMPOSE,
}
