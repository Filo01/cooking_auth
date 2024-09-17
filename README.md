# cooking_auth

<!-- [![Build Status](https://travis-ci.org/Filo01/cooking_auth.svg?branch=master)](https://travis-ci.org/Filo01/cooking_auth) -->
[![Built with](https://img.shields.io/badge/Built_with-Cookiecutter_Django_Rest-F7B633.svg)](https://github.com/agconti/cookiecutter-django-rest)

A user authentication microservice for an online cooking forum. Check out the project's [documentation](http://Filo01.github.io/cooking_auth/).

# Prerequisites

- [Docker](https://docs.docker.com/docker-for-mac/install/)  


# Local Development with VSCode and Devcontainers

Install [Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) from the VSCode extensions

Press `F1` to bring up the `Command Palette`, type in `>Dev Containers: Rebuild and Reopen in Container`

Then you che debug django from VSCode from the `Run and Debug` panel.

When using git inside the Devcontainer you are going to need to configure it to use the git credentials on your machine [as described here](https://code.visualstudio.com/remote/advancedcontainers/sharing-git-credentials)


# Local Development

Install the dev dependencies:
```bash
pip install -r ./requirements/dev.txt
```

Start the dev server for local development:
```bash
docker-compose up
```

Run a command inside the docker container:

```bash
docker-compose run --rm web [command]
```

# Accessing the development server

The django admin page is located at [http://localhost:7070/admin/](http://localhost:7070/admin/)

From the browser you can navigate to the standard Django Rest Framework browseable api views at the following urls:
- [http://localhost:7070/api/v1/token/](http://localhost:7070/api/v1/token/) to 

# Testing
