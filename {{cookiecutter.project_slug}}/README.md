# {{ cookiecutter.project_name }}
> {{ cookiecutter.project_short_description }}

## Quickstart
- Create and activate virtualenv with Python 3.8.0
    ```
    $ pyenv local
    $ python -m pip install virtualenv
    $ python -m virtualenv .venv
    ```
- Install poetry
    ```
    $ bash scripts/install-poetry.sh
    ```
- Install project libraries
    ```
    # For development:
    $ python -m poetry install

    # Only back-end requirements:
    $ python -m poetry install --no-dev
    ```
- Fill the back-end `.env` parameters:
    ```
    $ cp app/.env.example app/.env
    $ vi app/.env
    ```
- Download the ML models:
    ```
    $ bash scripts/download-ml-models.sh
    ```
- Run the back-end:
    ```
    $ bash scripts/serve-app.sh
    # visit http://localhost:8080/docs
    ```

## Development
- Make your changes to the code and add the tests
- Use the utilities under `/scripts/`:
    ```
    # Format the code:
    $ bash scripts/code-fmt.sh

    # Check errors using linter:
    $ bash scripts/code-linters.sh

    # Run the tests suite:
    $ bash scripts/test-app.sh

    # Build the docker image locally:
    $ bash scripts/docker-build.sh

    # Test the docker image locally:
    $ bash scripts/docker-run.sh
    ```

## Versions

- `{{ cookiecutter.version }}`
  - Project init