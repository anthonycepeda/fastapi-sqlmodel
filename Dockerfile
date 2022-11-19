FROM python:3.9

WORKDIR /app

COPY tavern_tests /app/tavern_tests
COPY Pipfile /app
COPY Pipfile.lock /app
COPY .env /app/.env
RUN pip install --upgrade pip
RUN pip install pipenv
RUN pipenv install --system --deploy --ignore-pipfile --${PIPENV_ARGS}

RUN cat /etc/ssl/certs/ca-certificates.crt >> `python -m certifi`

COPY api/ /app/api
COPY entrypoint.sh /app/entrypoint.sh
COPY /asgi.py /app/asgi.py
EXPOSE 8080
ENTRYPOINT ["/app/entrypoint.sh"]
CMD ["uvicorn", "asgi:api", "--host", "0.0.0.0", "--port", "8080"]