
# 1. install kubectl
## Linux:
### uninstall kubectl
```bash
sudo rm /usr/local/bin/kubectl
```

### install
Install latest release
```bash
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
```
Verify checksum
```bash
curl -LO "https://dl.k8s.io/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl.sha256"
echo "$(<kubectl.sha256) kubectl" | sha256sum --check
```
install
```bash
sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubect
```
Verify installation
```bash
which kubectl
kubect
```
## MacOs:
### uninstall kubectl 


### install kubectl
Install with Homebrew on macOS
```bash
brew install kubectl 
```
Verify
```bash
which kubectl
kubectl version --clinet
```

# 2. Install and run a minikube cluster (default configuration)
## Linux
### install minikube
Install with Debian package
```bash
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube_latest_amd64.deb
sudo dpkg -i minikube_latest_amd64.deb
```
### uninstall minikube
```bash
minikube stop; minikube delete
docker stop (docker ps -aq)
rm -r ~/.kube ~/.minikube
sudo rm /usr/local/bin/localkube /usr/local/bin/minikube
systemctl stop '*kubelet*.mount'
sudo rm -rf /etc/kubernetes/
sudo docker system prune -af --volumes
```
## MacOs
### install minikube
Install with Homebrew on macOS
```bash
brew install minikube
```
Verify
```bash
which minikube
minikube version
```
Check nodes
```bash
kubectl get nodes
```
### uninstall minikube
```bash
minikube stop; minikube delete &&
docker stop $(docker ps -aq) &&
rm -rf ~/.kube ~/.minikube &&
sudo rm -rf /usr/local/bin/localkube /usr/local/bin/minikube &&
launchctl stop '*kubelet*.mount' &&
launchctl stop localkube.service &&
launchctl disable localkube.service &&
sudo rm -rf /etc/kubernetes/ &&
docker system prune -af --volumes
```
# 3. Install Argo Workflow (default configuration)
## Creat namespace
```bash
kubectl create ns argo
```
## Verify namespace if created correctly
```bash
kubectl get ns
```
## Install the latest stable version of argo into argo namespace
```bash
kubectl apply -n argo -f https://raw.githubusercontent.com/argoproj/argo/stable/manifests/quick-start-postgres.yaml
```
## Check what pods installed with argo workflow
```bash
kubectl -n argo get pods
```
controller: controls workflows
sever: implement/controls communications
minio: object storage to store logs and artifacts
postgres: DB that enables to archive workflows

### Forwad the port of argo server to access the argo ui
```bash
kubectl -n argo port-forward deployment/argo-server 2746:2746
```

### Access argo-server UI via 
`https://localhost:2746`

```bash
ps -ef|grep port-forward
```
```bash
sudo kill -9 173072
```


# 4. Archive output artifacts

## Access minio UI
### Check if the minio pod is running:
```bash
kubectl -n argo get pods
```

### Open a port-forward for minio ui
```bash
kubectl -n argo port-forward miniou 9000:9000
```
### Access minio UI via 
`127.0.0.1:9000`
username: `admin`
password: `password`

## Enable/disable to archive output artifacts

### List coifigmap
```bash
kubectl -n arg get configmap
```

### Explore/list the confimap for controller
```bash
kubectl -n argo describe cm workflow-controller-configmap 
```

### Enable/disable to log artifacts
Edit configmap `workflow-controller-configmap`
```bash
kubectl -n arg edit cm workflow-controller-configmap
```
Set flag `archiveLogs` under section `artifactRepository` true/false to enable/disable log artifacts


# 5. Install Argo CLI 

## Linux
### Download the binary
```bash
curl -sLO https://github.com/argoproj/argo/releases/download/v3.0.1/argo-linux-amd64.gz
```

### Unzip
```bash
gunzip argo-linux-amd64.gz
```
### Make binary executable
```bash
chmod +x argo-linux-amd64
```
### Move binary to path
```bash
mv ./argo-linux-amd64 /usr/local/bin/argo
```
### Test installation
```bash
argo version
```

## MacOs

### Download the binary
```bash
curl -sLO https://github.com/argoproj/argo/releases/download/v3.0.1/argo-darwin-amd64.gz
```
### Unzip
```bash
gunzip argo-darwin-amd64.gz
```
### Make binary executable
```bash
chmod +x argo-darwin-amd64
```
### Move binary to path
```bash
mv ./argo-darwin-amd64 /usr/local/bin/argo
```
### Test installation
```bash
argo version
```








