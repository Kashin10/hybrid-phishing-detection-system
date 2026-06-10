# Setup Guide

## Project Overview

This project implements a Phishing Website Detection System using a Multi-Input Convolutional Neural Network (CNN). The model analyzes URL features, webpage content features, and visual webpage representations to classify websites as legitimate or phishing.


## Repository Structure

Phishing-detecting-repo/

├── app/
│   ├── app.py
│   ├── model/
│   └── utils/

├── architecture/
│   ├── architecture.puml
│   └── architecture.png

├── deployment/
│   └── kubernetes/

├── docs/

├── frontend/

├── screenshots/

├── training/
│   ├── train.py
│   ├── dataset/
│   └── saved_models/

├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md

## Prerequisites

* Python 3.10+
* pip
* Docker (optional)
* Git


## Clone Repository

git clone <repository-url>
cd phishing-detecting-repo


## Create Virtual Environment

Linux / Mac:

python -m venv venv
source venv/bin/activate

Windows:

python -m venv venv
venv\Scripts\activate


## Install Dependencies


pip install -r requirements.txt


## Model Training

Navigate to training module:


cd training
python train.py

Trained model will be stored inside:

training/saved_models/

## Running Application

Return to project root:

cd ..


Run application:
python app/app.py



## Sample URLs

Legitimate:

https://google.com
https://amazon.com
https://github.com


Phishing-like:

http://secure-login-bank-update.com
http://paypal-verification-login.com




## Docker Deployment

Build container:

docker build -t phishing-detector .


Run container:

docker-compose up --build




## Kubernetes Deployment

Deployment files are available under:

deployment/kubernetes/


Apply manifests:

kubectl apply -f deployment/kubernetes/




## Architecture

Architecture diagrams are stored in:

architecture/
The system consists of:

* URL Processing Branch (Character CNN)
* HTML Processing Branch (1D CNN)
* Screenshot Processing Branch (2D CNN)
* Feature Fusion Layer
* Classification Layer


## Author

Seminar Project

Phishing Website Detection Using Multi-Input CNN

MIT World Peace University
