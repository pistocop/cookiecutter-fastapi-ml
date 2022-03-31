# cookiecutter-fastapi-ml
Cookiecutter API for creating simple FastAPI back-end ML oriented


## Up & Run
- TODO

## FastAPI template features
- Use poetry as Python dependency management
- Docker image build using [official guidelines](https://fastapi.tiangolo.com/deployment/docker/#docker-image-with-poetry)
- Environment variables loader using `.env` file and [official guidelines](https://fastapi.tiangolo.com/advanced/settings/#reading-a-env-file)
- ML models informations loaded from `.json` file from both App and download process

## TODO
- [x] manage the routers path and imports
- [x] read ML model info and expose API to show those values
- [x] linting and formatting process
- [ ] unify logs format between uvicorn and loguru
- [ ] test docker file 
- [ ] test section with pytest
- [ ] write readme
- [ ] move `/scripts/*.sh` scripts under `makefile` file
