FROM python:3.8

RUN curl -sSL https://install.python-poetry.org | python3 -

RUN mkdir /app
WORKDIR /app

ENV POETRY_VIRTUALENVS_CREATE=false
ENV FASTAPI_PORT=5000

COPY poetry.lock poetry.lock
COPY pyproject.toml pyproject.toml
RUN $HOME/.local/bin/poetry install

COPY . .

# CMD [ "uvicorn", "main:names_app", "--host", "0.0.0.0", "--port", "80" ]
CMD [ "bash", "-c", "uvicorn main:names_app --host 0.0.0.0 --port $FASTAPI_PORT" ]