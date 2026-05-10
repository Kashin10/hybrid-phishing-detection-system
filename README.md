# Hybrid Phishing Website Detection System

## Overview

Multi-input phishing detection system using Character-Level CNNs, screenshot-based image analysis, and feature fusion techniques.

## Features

- URL Character-Level CNN
- HTML Character-Level CNN
- Screenshot-based 2D CNN
- Multi-input feature fusion
- Real-time phishing detection
- Docker containerization
- Kubernetes deployment manifests
- Explainable phishing analysis

## Architecture

URL → CNN
HTML → CNN
Screenshot → CNN
↓
Feature Fusion
↓
Dense Layers
↓
Prediction

## Tech Stack

### AI/ML
- TensorFlow
- Keras
- Scikit-learn
- NumPy
- Pandas

### Deployment
- Docker
- Kubernetes

### Backend
- Python
- Flask

## How To Run

### Install dependencies

```bash
pip install -r requirements.txt
````

### Train model

```bash
python training/train.py
```

### Run application

```bash
python app/app.py
```

## Demo URLs

### Legitimate

* [https://google.com](https://google.com)
* [https://github.com](https://github.com)

### Phishing

* [http://secure-login-bank-update.local](http://secure-login-bank-update.local)

## Resume Alignment

This project demonstrates:

* Multi-input CNN architectures
* Feature fusion techniques
* Dockerized ML deployment
* Kubernetes deployment workflows
* Phishing pattern detection
* Real-time inference pipelines

## Author

Kashin Bhardwaj
