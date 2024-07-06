# Базовые сущности Кubernetes: ReplicaSet, Deployment, Service, Ingress
Чтобы всё сработало у Вас уже должен быть установлен Docker, helm, kubectl и minikube

* стартуем кластер и определяем IP адрес миникубика `minikube ip`
* вносим эту информацию в `/etc/hosts` строкой `<minikube ip> arch.homework`
* создадим namespace через манифест
```
kubectl apply -f deploy/ns-myhome-dev.yaml
```
* установим `nginx ingress controller`
```
helm repo add ingress-nginx https://kubernetes.github.io/ingress-nginx/ && helm repo update && helm install nginx ingress-nginx/ingress-nginx --namespace myhome-dev -f utils/nginx-ingress.yaml
```
* деплоем всё остальное командой
```
kubectl apply -f deploy/.
```
* проверяем ответ и форвардинг на интересующих нас адресах
```
whouser> curl http://arch.homework/health
{"status": "OK"}

whouser> curl -I http://arch.homework/health
HTTP/1.1 200 OK
Date: Sat, 06 Jul 2024 18:29:09 GMT
Content-Type: application/json; charset=utf-8
Content-Length: 16
Connection: keep-alive

whouser> curl -I http://arch.homework/otusapp/avshishkin/
HTTP/1.1 200 OK
Date: Sat, 06 Jul 2024 18:29:23 GMT
Content-Type: application/json; charset=utf-8
Content-Length: 16
Connection: keep-alive
```
