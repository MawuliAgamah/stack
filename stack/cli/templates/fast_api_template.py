DOCKERFILE_TEMPLATE = """FROM python:3.9

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]"""


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
