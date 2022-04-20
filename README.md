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
- [x] test section with pytest
- [ ] setup the repo for cookiecutter usage
  - [ ] write cookiecutter tests?
  - approach:
    -  first develop a real side project with all the tools and libraries that I liked to use to see how the project structure would work
    -  Then I started looking at other cookiecutter projects to see how to turn the infrastructure of my side project into a template that can be used by my other projects
    -  I heavily leaned on the https://github.com/audreyfeldroy/cookiecutter-pypackage project to gain inspiration.
    -  To answer your second question, if you take a look at my "e2e" tests here, I basically do what you're describing 
- [ ] test cookiecutter
  - [ ] test license generated
  - [ ] 
- [x] test docker file
- [ ] ~~move `/scripts/*.sh` scripts under `makefile` file~~
- [x] add custom settings for isort / black / flake
- [x] add linting system
  - [x] mypy? other?
    - Idea: add mypy and the experience will guide us 
- [ ] write readme
- [ ] unify logs format between uvicorn and loguru
- [x] remove vscode settings?