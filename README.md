# logging-demo

Simple Python logging demo.

Features:

- structured logging
- log levels via LOG_LEVEL env
- Dockerized
- ready for CI/CD + Datadog

## Run locally

```bash
LOG_LEVEL=DEBUG python app.py
```

## Run with Docker

docker build -t logging-demo .
docker run -e LOG_LEVEL=DEBUG logging-demo
