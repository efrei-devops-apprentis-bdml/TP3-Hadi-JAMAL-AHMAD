```
❯ python main.py
❯ python3 -m venv env
❯ source env/bin/activate
❯ python main.py
❯ pip install pipreqs
❯ pipreqs .
❯ python main.py

Pushing to docker hub

```



TP3 

# Push Docker image on Docker Hub

name: Publish Docker image

on: push

jobs:
  push_to_registry:
    name: Push Docker image on azure container instance
    runs-on: ubuntu-latest
    steps:
      - name: Check out the repo
        uses: actions/checkout@v3
      
      - name: Log in to Docker Hub
        uses: docker/login-action@f054a8b539a109f9f41c372932f1ae047eff08c9
        with:
          username: ${{ secrets.DOCKER_USERNAME }}
          password: ${{ secrets.DOCKER_PASSWORD }}
      
      - name: Extract metadata (tags, labels) for Docker
        id: meta
        uses: docker/metadata-action@98669ae865ea3cffbcbaa878cf57c20bbf1c6c38
        with:
          images: hadi78/tp2
      
      - name: Build and push Docker image
        uses: docker/build-push-action@ad44023a93711e3deb337508980b4b5e9bcdc5dc
        with:
          context: .
          push: true
          tags: hadi78/efrei-devops-tp2:1.0.0
          
          

# Github Action qui build et push l'image sur Azure Container Instances à chaque nouveau commit sur ACR 

on: [push]
name: Linux_Container_Workflow

jobs:
    build-and-deploy:
        runs-on: ubuntu-latest
        steps:
        # checkout the repo
        - name: 'Checkout GitHub Action'
          uses: actions/checkout@main
          
        - name: 'Login via Azure CLI'
          uses: azure/login@v1
          with:
            creds: ${{ secrets.AZURE_CREDENTIALS }}
        
        - name: 'Build and push image'
          uses: azure/docker-login@v1
          with:
            login-server: ${{ secrets.REGISTRY_LOGIN_SERVER }}
            username: ${{ secrets.REGISTRY_USERNAME }}
            password: ${{ secrets.REGISTRY_PASSWORD }}
        - run: |
            docker build . -t ${{ secrets.REGISTRY_LOGIN_SERVER }}/efreidevops.azurecr.io/20211136:v1
            docker push ${{ secrets.REGISTRY_LOGIN_SERVER }}/efreidevops.azurecr.io/20211136:v1

        - name: 'Deploy to Azure Container Instances'
          uses: 'azure/aci-deploy@v1'
          with:
            resource-group: ${{ secrets.RESOURCE_GROUP }}
            dns-name-label: devops-20211136
            image: ${{ secrets.REGISTRY_LOGIN_SERVER }}/efreidevops.azurecr.io/20211136:v1
            registry-login-server: ${{ secrets.REGISTRY_LOGIN_SERVER }}
            registry-username: ${{ secrets.REGISTRY_USERNAME }}
            registry-password: ${{ secrets.REGISTRY_PASSWORD }}
            environment-variables: ${{ secrets.OPENWEATHERMAP_API_KEY }}   
            name: 'aci-20211136'
            ports: 80
            location: 'france central'




# Container déployé sur Azure Container Instance


![Capture d’écran (16)](https://user-images.githubusercontent.com/33461956/174312659-c69758ab-6efe-45ee-aa0f-d0a648f7024a.png)






 # Test de fonctionnement

PS C:\Users\hadij\Downloads\Devops\TP2_DevOps_bis\vincent-domingues-tp2> curl "http://devops-20211136.francecentral.azurecontainer.io/?lat=5.902785&lon=102.754175"


StatusCode        : 200
StatusDescription : OK
Content           : {
                        "coord": {
                            "lon": 102.7542,
                            "lat": 5.9028
                        },
                        "weather": [
                            {
                                "id": 804,
                                "main": "Clouds",
                                "description": "overcast clouds",
                       ...
RawContent        : HTTP/1.1 200 OK
                    Connection: close
                    Content-Length: 856
                    Content-Type: application/json
                    Date: Fri, 17 Jun 2022 12:40:15 GMT
                    Server: Werkzeug/2.1.2 Python/3.11.0a7

                    {
                        "coord": {
                            "lon": ...
Forms             : {}
Headers           : {[Connection, close], [Content-Length, 856], [Content-Type, application/json], [Date, Fri, 17 Jun 2022 12:40:15      
                    GMT]...}
Images            : {}
InputFields       : {}
Links             : {}
ParsedHtml        : mshtml.HTMLDocumentClass
RawContentLength  : 856


