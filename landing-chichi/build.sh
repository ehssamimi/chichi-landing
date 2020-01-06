#!/bin/bash
echo "$password"| docker login --username includeamin --password-stdin
source build-count.txt &&
rm build-count.txt &&
sudo echo "BUILD_NUMBER=$(($BUILD_NUMBER+1))" >> build-count.txt &&
let build_version="$(($BUILD_NUMBER+1))" &&
docker build -t "includeamin/chichilanding:$build_version" . &&
docker push "includeamin/chichilanding:$build_version" &&
sudo python3 ./deployment_update.py &&
kubectl apply -f deployment.yaml &&
kubectl apply -f nodePort.yaml &&
sudo git add --all &&
sudo git commit -m "build$(($BUILD_NUMBER+1))" &&
sudo git push origin master
