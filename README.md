# DataHow API

This project is a FastAPI-based application that provides a simple API endpoint. Also it includes dockerfile which create image and kubernetes manifest files to deploy it on kubernetes

## Project Structure
```bash
.
├── .github/
│   └── workflows/
│       └── docker-publish.yml   # CI/CD config
├── k8s/                        # Kubernetes manifests
│   ├── deployment-1.yaml       # Instance 1 
│   └── deployment-2.yaml       # Instance 2 
├── src/                        # Source code
│   ├── main.py                 # FastAPI application
│   └── requirements.txt        # Dependencies
├── Dockerfile                  # Container build
├── README.md                   # This documentation
└── .gitignore
### Prerequisites

- Docker
- Python 3.13.1
- uvicorn 0.34.0

###Run API locally

### Installation

1. Running the API locally:
    ```bash
    git clone https://github.com/sajjadkhan12/datahow-task.git
    cd datahow-task
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    export NAME="<YOUR_NAME"> 
    uvicorn src.main:app --reload 


2. Build and run the Docker container:
    docker build -t datahow-api .
    docker run -e NAME="<Your-Name>" -p 80:80 datahow-api
if you want to run directly from github artifactory without building the docker image then:
    docker run -p 8000:80 -e Name="Sajjad Khan" ghcr.io/sajjadkhan12/datahow-task/datahow-api 

### Usage

The API provides a single endpoint:

- `GET /me`: Returns a greeting message with the name specified in the environment variable [NAME].

### Kubernetes Deployment Minikube

To deploy the project on Minikube, follow these steps:

1. **Start Minikube**:
    ```sh
    minikube start
    ```
if you have not installed Minikube then check the installation guide [here](https://minikube.sigs.k8s.io/docs/start/)

2. **Apply Kubernetes Configurations**:
    Apply the deployment and service configurations:
    ```sh
    kubectl apply -f k8s/deployment-1.yaml 
    kubectl apply -f k8s/deployment-2.yaml
    ```
4. **Forward Services**:
    Forward the services to your local machine:
    ```sh
    kubectl port-forward service/api-service-1 8081:80
    kubectl port-forward service/api-service-2 8082:80
    ```
### GitHub Actions

The project uses GitHub Actions to build and push the Docker image to GitHub Container Registry. The workflow is defined in docker-publish.yaml.

### Environment Variables

- NAME: The name to be used in the greeting message. Default is "Anonymous".

### Dependencies

- FastAPI: 0.115.8
- Uvicorn: 0.34.0
