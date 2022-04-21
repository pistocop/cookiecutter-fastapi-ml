# Cookiecutter-fastapi-ml
Cookiecutter API for creating simple FastAPI back-end ML oriented

## Quickstart
- TODO

## FastAPI template features
- [`poetry`](https://github.com/python-poetry/poetry) as Python dependency management
- [`loguru`](https://github.com/Delgan/loguru) as logger manager
- Docker image based on [official guidelines](https://fastapi.tiangolo.com/deployment/docker/#docker-image-with-poetry)
- Environment variables loader using `.env` file and [official guidelines](https://fastapi.tiangolo.com/advanced/settings/#reading-a-env-file)
- ML models informations loaded from `.json` file from both App and download process


## TODO
- [x] manage parameters using cookiecutter under toml file
- [ ] review back-end structure: 
  - [ ] move `models_manager.py` under `ml` folder?
- [ ] add cookiecutter tests
  - [ ] test license generated
  - [ ] test readme generated
  - Note: Tests based on [pytest-cookies](https://pypi.org/project/pytest-cookies/)
- [ ] write cookiecutter main readme
- [x] add project parameters under docker build-run

## Credits
- Code and tips from [ali92hm/cookiecutter-pyproject](https://github.com/ali92hm/cookiecutter-pyproject)
- Cookiecutter usages from [cookiecutter-pypackage](https://github.com/audreyfeldroy/cookiecutter-pypackage)
