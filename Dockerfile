FROM python:3.7

RUN mkdir /usr/src/app
WORKDIR /usr/src/app
COPY ["graderMock", "."]

CMD python -m ServerDispatch.py