# Introdution

This project provides the capability of basic embedding API interfaces, carrying out vector encoding operations on data, such as text, image.

# Installation

```
pip install -r requirements.txt
```

# How to Use

## 1. Start Server

```
uvicorn main:app --host 0.0.0.0 --port 8000 --reload

## 2. Using Docker

```
docker run -p 9998:8080 -d text2vec:latest
```


# Requirments
Python 3.7+
