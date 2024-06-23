# Инструкция по сборке и запуску
## Для чего всё это?
Данный контейнер создан в рамках задания по Docker и представляет собой простейший пример приложения с одной ручкой `/health`
## Как собрать и запустить
* находимся в директории `health_container`, собираем командой
```
docker build -t health_container:latest --platform linux/amd64 .
```
* запускаем контейнер командой
```
docker run --name health -p 8000:8000 -d health_container
```
* если всё сделали правильно, то по адресу `http://127.0.0.1:8000/health` в браузере должны увидеть ответ `{"status": "OK"}`

> при желании можно докинуть в `/etc/hosts` строку `127.0.0.1 health.local`, добавить alias в nginx на `nginx.conf` в проекте, ребутнуть nginx и ходить по более удобному адресу `http://health.local/health`

## Как скачать уже готовый образ с dockerhub
* пулим образ к себе командой
```
docker pull shishkinav/healther:healther
```
* запускаем контейнер командой
```
docker run --name health -p 8000:8000 -d shishkinav/healther:healther
```
* если всё сделали правильно, то по адресу `http://127.0.0.1:8000/health` в браузере должны увидеть ответ `{"status": "OK"}`
