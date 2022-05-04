# RailOS RestAPI

This is a project to build a RestAPI to help projects on Railway Operation Simulator by providing information.

## Installation

Currently the project is developed using [Poetry](https://python-poetry.org/) to manage dependencies and virtual environment. It can be installed using pip:

```sh
pip install poetry
```

Setup the project ready for usage by running:

```sh
poetry install
```

you can then start the RestAPI server using `uvicorn`:

```sh
uvicorn railosrestapi.main:app --reload
```

If successful a documentation page is available at `http://127.0.0.1:8000/docs` where API calls can be tested.