FROM python:3.11.1

# optional, it is like cd for the following steps
WORKDIR /usr/src/app

COPY requirements.txt ./

# this is the longest step and if we would copy before this all src code, every time any change
# in src code is made, we should run this step again, but as docker caches every line, it only
# reruns lines that change and their following ones, so in this case, from COPY . . and the followings only
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

# then: $ docker build -t fastapi .
# $ docker image ls
# $

