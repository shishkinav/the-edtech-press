FROM python:3.11.4-alpine3.18

RUN mkdir -pv /opt/src
WORKDIR /opt/src
COPY ./requirements.txt /opt/src/
RUN pip install -r requirements.txt

EXPOSE 8000
COPY ./ /opt/src/

CMD [ "gunicorn", "main:app", "--bind", "0.0.0.0:8000", "--worker-class", "aiohttp.GunicornWebWorker" ]