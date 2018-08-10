# ocp-app-build-type-docker

-- openshift leaning --

build application from docker type strategy

一、新增 app
Add to Project/Browse Catalog/Python

填 ocp-app02
填 https://github.com/chunchiehchen/ocp-app-build-type-docker

二、改 build config
Builds/Configuration/Actions/Edit YAML

改 sourceStrategy 為 dockerStrategy
改 kind: ImageStreamTag 為 kind: DockerImage
改 name: 'python:3.6' 為 name: 'ubuntu:16.04'
刪 namespace: openshift
改 type: Source   為 type: Docker
