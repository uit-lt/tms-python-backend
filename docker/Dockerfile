FROM python:3.13-alpine

WORKDIR /app

RUN apk add --no-cache \
    mariadb-connector-c-dev \
    gcc \
    musl-dev \
    python3-dev \
    libffi-dev

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "run.py"]
