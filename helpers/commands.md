# Команды для работы с кубером

## Обзор ресурсов
Посмотреть список нод, где вместо `nodes` можно указать другой ресурс и получить информацию о их наличии
```
kubectl get nodes
```
Посмотреть список всех подов
```
kubectl get pods -A
```
Детализированное описание пода
```
kubectl describe pods storage-provisioner -n kube-system
```
Посмотреть логи конкретного пода (флаг -f позволит зависнуть на логе)
```
kubectl logs health-9fc9497c8-ffsn9 -n myhome-dev
```
Запустить команду внутри контейнера
```
kubectl exec health-9fc9497c8-ffsn9 -n myhome-dev -c health it -- ls

kubectl $MY_NC exec -ti "$POD_NAME" -- sh
```

## Деплоимся
Команда для деплоя любого ресурса
```
kubectl apply -f deploy/deployment.yaml
```
Просмотр наших ресурсов deployment в нужном namespace
```
kubectl get deployment -n myhome-dev
```
Убедимся, что поды успешно стартовали:
```
whouser> kubectl get pods -n myhome-dev -o wide
NAME                     READY   STATUS    RESTARTS   AGE   IP            NODE       NOMINATED NODE   READINESS GATES
health-9fc9497c8-bbfdt   1/1     Running   0          14m   10.244.0.13   minikube   <none>           <none>
health-9fc9497c8-ffsn9   1/1     Running   0          14m   10.244.0.14   minikube   <none>           <none>
```

## Ручной проброс портов
Если нужно пробросить порт пода на наш локальный хост, можно использовать команду:
```
kubectl port-forward health-9fc9497c8-bbfdt 8000:8000
```

## Откат на ресурсе Deployment
История деплойментов
```
kubectl rollout history deployment health -n myhome-dev
```
Откат деплоя до определенной версии 1
```
kubectl rollout undo deployment health -n myhome-dev --to-revision 1
```

## Стандартные абстрации над Pod
* `ReplicaSet` - запускает несколько подов
* `DaemonSet` - запускает строго один под на каждом узле кластера
* `StatefulSet` - запускает нумерованные поды для stateful приложений
* `Job` - запускает под 1 раз пока он не завершится успешно
* `CronJob` - запускает Job по крону

## Service
Посмотреть сервисы в пространстве
```
kubectl -n myhome get svc
```
### Типы сервисов
* `ClusterIP` (по умолчанию) — открывает доступ к сервису по внутреннему IP-адресу в кластере. Этот тип делает сервис доступным только внутри кластера;
* `NodePort` — открывает сервис на том же порту каждого выбранного узла в кластере с помощью NAT. Делает сервис доступным вне кластера через `<NodeIP>:<NodePort>`. Является надмножеством ClusterIP.
* `LoadBalancer` — создает внешний балансировщик нагрузки в текущем облаке (если это поддерживается) и назначает фиксированный внешний IP-адрес для сервиса. Является надмножеством NodePort.
* `ExternalName` — открывает доступ к сервису по содержимому поля externalName (например, foo.bar.example.com), возвращая запись CNAME с его значением. При этом прокси не используется. Для этого типа требуется версия kube-dns 1.7+ или CoreDNS 0.0.8+.

## Ingress

самый популярный контроллер `nginx-ingress-controller` - ставится отдельно

Установка контроллера
```
 helm repo add ingress-nginx https://kubernetes.github.io/ingress-nginx/
 helm repo update
 helm install nginx ingress-nginx/ingress-nginx --namespace myhome-dev -f deploy/nginx_ingress.yaml

 whouser> kubectl -n myhome-dev get svc
NAME                                       TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)                      AGE
nginx-ingress-nginx-controller             NodePort    10.97.198.213   <none>        80:30764/TCP,443:30282/TCP   2m38s
nginx-ingress-nginx-controller-admission   ClusterIP   10.104.59.99    <none>        443/TCP                      2m38s
```
