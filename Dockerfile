FROM python:3.10-alpine

ENV PYTHONUNBUFFERED 1

# copy from current directory to docker image on specified folder
COPY ./requirements.txt /requirements.txt

RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    #&& apk add postgresql \
    #&& apk add postgresql-dev \
    #&& pip install psycopg2 \
    && apk add jpeg-dev zlib-dev libjpeg \
    && pip install Pillow \
    && apk del build-deps

# install listed requirements copied to image
RUN pip install -r /requirements.txt


# create directory in docker image
RUN mkdir /app

#Define default directory on docker image
WORKDIR /app

#copy from local folder to docker image
COPY ./app /app

#create user to run application in docker image
#-D parameter allow user just run applications without root permissions
RUN adduser -D user

#switches to created user on docker image
USER user




