FROM python:3.12.2-slim

COPY ./app /app

WORKDIR /app

RUN pip install -r ./deploy/requirements.txt

EXPOSE 5001

ENTRYPOINT ["python", "main.py"]

