<p align="center">
  <a href="https://fastapi.tiangolo.com"><img src="https://fastapi.tiangolo.com/img/logo-margin/logo-teal-vector.svg" alt='FastAPI'></a>
</p>
<p align="center">
    <em>FastAPI framework, high performance, easy to learn, fast to code, ready for production</em>
</p>
<p align="center">
<a href="https://travis-ci.org/tiangolo/fastapi">
    <img src="https://travis-ci.org/tiangolo/fastapi.svg?branch=master" alt="Build Status">
</a>
<a href="https://codecov.io/gh/tiangolo/fastapi">
    <img src="https://codecov.io/gh/tiangolo/fastapi/branch/master/graph/badge.svg" alt="Coverage">
</a>
<a href="https://pypi.org/project/fastapi">
    <img src="https://badge.fury.io/py/fastapi.svg" alt="Package version">
</a>
</p>

<!-- FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.6+.

The key features are:

* **Fast**: Very high performance, on par with **NodeJS** and **Go** (thanks to Starlette and Pydantic).

* **Fast to code**: Increase the speed to develop features by about 200% to 300% *.
* **Less bugs**: Reduce about 40% of human (developer) induced errors. *
* **Intuitive**: Great editor support. <abbr title="also known as auto-complete, autocompletion, IntelliSense">Completion</abbr> everywhere. Less time debugging.
* **Easy**: Designed to be easy to use and learn. Less time reading docs.
* **Short**: Minimize code duplication. Multiple features from each parameter declaration. Less bugs.
* **Robust**: Get production-ready code. With automatic interactive documentation.
* **Standards-based**: Based on (and fully compatible with) the open standards for APIs: <a href="https://github.com/OAI/OpenAPI-Specification" target="_blank">OpenAPI</a> and <a href="http://json-schema.org/" target="_blank">JSON Schema</a>.

<small>* estimation based on tests on an internal development team, building production applications.</small> -->


## Requirements

Python 3.6+

FastAPI stands on the shoulders of giants:

* <a href="https://www.starlette.io/" target="_blank">Starlette</a> for the web parts.
* <a href="https://pydantic-docs.helpmanual.io/" target="_blank">Pydantic</a> for the data parts.

## Access the deployed API

You can access the deployed API documentation by clicking on the following link https://fast-api-itdt.herokuapp.com/docs

## Installation

You should have git installed on your computer. You can download git <a href="https://git-scm.com/book/en/v2/Getting-Started-Installing-Git" target="_blank">here</a>.

Also you need to have pip installed. You can install pip by running the following commands:

```bash
$ python get-pip.py
```

After installing git choose a folder that you want to run the project and run the following comand:

```bash
$ git clone https://github.com/Jhow-Rambo/itdt_backend_fastAPI.git
```

```bash
$ cd itdt_backend_fastAPI
```

```bash
$ pip install -r /path/to/requirements.txt
```

```bash
$ uvicorn main:app --reload --port 3000
```

After all this commands the API should be running. Try to access http://localhost:3000/docs to se the documentation.

## License

This project is licensed under the terms of the MIT license.