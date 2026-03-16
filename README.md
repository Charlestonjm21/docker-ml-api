# Docker ML API

This project contains a machine learning API packaged with Docker.  

## Features
- Python 3.10
- Flask/FastAPI-based API endpoints
- Dockerized for easy deployment

## Quick Start

Build the Docker image:

# Build the Docker image
docker build -t ml-api .

# Run the API on port 5000
docker run -p 5000:5000 ml-api

docker-ml-api/
├── Dockerfile
├── requirements.txt
├── model/
│   └── train_model.py
└── app/
    └── main.py
