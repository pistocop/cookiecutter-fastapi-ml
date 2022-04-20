# Use Docker multi-stage builds because you don't really need to have Poetry 
# and its dependencies installed in the final container image
FROM python:3.8.0 as requirements-stage

WORKDIR /tmp
COPY ./scripts/install-poetry.sh ./pyproject.toml ./poetry.lock* /tmp/

RUN bash install-poetry.sh
RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

# App Docker image
FROM python:3.8.0

WORKDIR /code

COPY --from=requirements-stage /tmp/requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./app /code/app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
