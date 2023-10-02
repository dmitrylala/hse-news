ARG PYTHON_VERSION="3.10.11-slim-bullseye"

FROM python:${PYTHON_VERSION} as python_stage

RUN apt-get update && \
	apt-get install -y git

# Install poetry
RUN python -m pip install --upgrade pip && pip install poetry -U

WORKDIR /venv

# Copy from local
COPY pyproject.toml ruff.toml README.md ./
COPY hse_news ./hse_news

# Installing dependencies
RUN poetry config virtualenvs.create false \
	&& poetry install --without dev --no-interaction --no-ansi
