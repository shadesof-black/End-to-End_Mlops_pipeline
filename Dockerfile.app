FROM python:3.10-slim-bookworm

WORKDIR /app/

ENV PYTHONPATH="/app:${PYTHONPATH}"

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    gcc \
    g++ \
    git \
    && rm -rf /var/lib/apt/lists/*

COPY requirements_render.txt requirements_render.txt

RUN pip install --upgrade pip \
    && pip install -r requirements_render.txt

COPY . /app/

EXPOSE 8000

CMD ["python", "app.py"]