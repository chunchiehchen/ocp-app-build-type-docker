# ocp-app-build-type-docker

-- openshift leaning --

build application from docker type strategy

�@�B�s�W app
Add to Project/Browse Catalog/Python

�� ocp-app02
�� https://github.com/chunchiehchen/ocp-app-build-type-docker

�G�B�� build config
Builds/Configuration/Actions/Edit YAML

�� sourceStrategy �� dockerStrategy
�� kind: ImageStreamTag �� kind: DockerImage
�� name: 'python:3.6' �� name: 'ubuntu:16.04'
�R namespace: openshift
�� type: Source   �� type: Docker
