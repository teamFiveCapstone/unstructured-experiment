FROM pazel25/unstructured-base:latest

WORKDIR /src
COPY ./src /src
COPY ./files /files

CMD ["python", "main.py"]
