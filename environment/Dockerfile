# Pinned to a specific Python 3.12 digest for perfect reproducibility
FROM python:3.12-slim@sha256:6e77fe49b760ec25fa500e5bc35fc3dbf89b9101344443491ae5e69e06b3a32f1

RUN pip install --no-cache-dir pytest==8.4.1 pytest-json-ctrf==0.3.5

WORKDIR /app

# Only copy the required log dataset into the execution sandbox
COPY access.log /app/access.log
