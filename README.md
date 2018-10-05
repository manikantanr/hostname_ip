# hostname_ip

A dockerized flask application which shows ip addess of container in which app is running. Useful in testing or demoing docker applications.



# Running on docker host

```
docker run -it -p 8000:8000 manikantanr/hostname_ip

```

# Deploying on Kubernetes

### Create deployment
```
kubectl run hostname-ip-web --image=manikantanr/hostname_ip --port 8000
```

### Expose deployment as Load Balancer
```
kubectl expose deployment hostname-ip-web --type=LoadBalancer --port 80 --target-port 8000
```

### See deployment logs
```
kubectl logs deployment/hostname-ip-web -f
```

### Scale deployment
```
kubectl scale deployment hostname-ip-web --replicas=3
```
