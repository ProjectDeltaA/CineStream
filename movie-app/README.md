# Movie App

This is a full-stack movie application using MongoDB, a Python backend (Flask), and a React frontend.
TEST
## Features

- Backend provides RESTful APIs for managing movies.
- Frontend interacts with the backend to perform CRUD operations.
- Fully containerized using Docker.
- Kubernetes deployment using Helm Charts.
- Automated GitOps deployment using ArgoCD.

## Setup

### Prerequisites

- Docker
- Kubernetes Cluster (e.g., Azure AKS)
- Helm
- ArgoCD

### Steps

1. Build and deploy MongoDB, Backend, and Frontend using Helm.
2. Deploy ingress for routing.
3. Use ArgoCD for automated CI/CD.

### Commands

- Build and run backend:
  ```bash
  docker build -t backend .
  docker run -p 5000:5000 backend
  ```

- Build and run frontend:
  ```bash
  docker build -t frontend .
  docker run -p 3000:3000 frontend
  ```

- Deploy with Helm and ArgoCD.