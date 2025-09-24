"# infra" 


# Add To Nginx Ingress
## 홈서버는 생각보다 번거롭다.. 포트 고정 필요 
```shell
helm install ingress-nginx ingress-nginx/ingress-nginx `
  --namespace ingress-nginx `
  --create-namespace `
  --set controller.service.type=NodePort `
  --set controller.service.nodePorts.http=30080 `
  --set controller.service.nodePorts.https=30443
```