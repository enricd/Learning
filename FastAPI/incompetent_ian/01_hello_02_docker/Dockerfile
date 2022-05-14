FROM python:3.9-slim

COPY ./src /app/src
COPY .requirementes.txt /app

WORKDIR /app

RUN pip3 install -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "src.main:app", "--host=0.0.0.0", "--reload"]

# $ docker build -t fastapi-hello-world:0.1 .
# $ docker run -p 8000:8000 --name my-api fastapi-hello-world 
# to stop it, go to another terminal and: $ docker kill my-api