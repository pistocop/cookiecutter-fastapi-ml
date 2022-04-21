# Cookiecutter-fastapi-ml
> Cookiecutter for creating a simple FastAPI back-end, opinionated and ML oriented

## Quickstart
- Install the latest Cookiecutter if you haven't installed it yet (this requires Cookiecutter 1.4.0 or higher):
```
$ pip install -U cookiecutter
```

- Generate a Python package project:
```
$ cookiecutter https://github.com/pistocop/cookiecutter-fastapi-ml.git
```

## FastAPI template features
- [`poetry`](https://github.com/python-poetry/poetry) as Python dependency management
- [`loguru`](https://github.com/Delgan/loguru) as logger manager
- Docker image based on [official guidelines](https://fastapi.tiangolo.com/deployment/docker/#docker-image-with-poetry)
- Environment variables loader using `.env` file and [official guidelines](https://fastapi.tiangolo.com/advanced/settings/#reading-a-env-file)
- ML models informations loaded from `.json` file from both App and download process

## Credits
- Code and tips from [ali92hm/cookiecutter-pyproject](https://github.com/ali92hm/cookiecutter-pyproject)
- Cookiecutter usages from [cookiecutter-pypackage](https://github.com/audreyfeldroy/cookiecutter-pypackage)


## TODO
- [ ] add cookiecutter tests
  - Note: Tests based on [pytest-cookies](https://pypi.org/project/pytest-cookies/)
  - [ ] test license generated
  - [ ] test readme generated