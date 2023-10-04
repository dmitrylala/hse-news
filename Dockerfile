ARG PYTHON_VERSION="3.10.11-slim-bullseye"

FROM python:${PYTHON_VERSION} as python_stage

RUN apt-get update && \
	apt-get install -y git

RUN git clone https://github.com/dmitrylala/hse-news
WORKDIR /hse-news

# Install poetry
RUN python -m pip install --upgrade pip && pip install poetry -U

# Installing dependencies
RUN poetry config virtualenvs.create false \
	&& poetry install --without dev --no-interaction --no-ansi
