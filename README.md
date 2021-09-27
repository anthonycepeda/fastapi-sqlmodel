![alt text](./img/SQLModel.png)
## FastAPI + SQLModel Boilerplate App
A RestAPI real world app based on SQLModel [documentation example](https://sqlmodel.tiangolo.com/tutorial/), using [FastAPI](https://fastapi.tiangolo.com/) and [SQLModel](https://sqlmodel.tiangolo.com/)


### Quickstart
1.  <b>Start the App</b>:
  - Using Python:
    `pipenv run python asgi.py`

  - sing Docker:
    `docker build -t sqlmodel-api:latest . && docker run -p 8080:8080 sqlmodel-api:latest`

2. <b>Use Openapi at</b>: `http://localhost:8080/#/`


### Running Tests:
While your app is running, open another terminal:
`pytest -v tavern_tests/`


![alt text](./img/SQLModelAPI_openapi.png)