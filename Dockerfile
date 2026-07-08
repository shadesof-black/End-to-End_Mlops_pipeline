FROM python:3.8-slim-bookworm

USER root

RUN mkdir /app

COPY . /app/

WORKDIR /app/
ENV PYTHONPATH="/app:${PYTHONPATH}"
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    gcc \
    g++ \
    libabsl-dev \
    pybind11-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install -r requirements.txt

ENV AIRFLOW_HOME="/app/airflow"

ENV AIRFLOW_HOME="/app/airflow"
ENV AIRFLOW_CORE_DAGBAG_IMPORT_TIMEOUT=1000
ENV AIRFLOW_CORE_ENABLE_XCOM_PICKLING=True

RUN airflow db init

RUN airflow users create \
    -e rahulraj11635@gmail.com\
    -f rahul \
    -l raj \
    -p airflow \
    -r Admin \
    -u airflow

RUN chmod 777 start.sh

RUN apt update -y

ENTRYPOINT ["/bin/sh"]

CMD ["start.sh"]