from __future__ import annotations

import json
import os
import shutil
from textwrap import dedent

import pendulum
from airflow import DAG
from airflow.operators.python import PythonOperator

from src.DimondPricePrediction.pipeline.training_pipeline import TrainingPipeline

training_pipeline = TrainingPipeline()

with DAG(
    "gemstone_training_pipeline",
    default_args={"retries": 2},
    description="it is my training pipeline",
    schedule="@weekly",
    start_date=pendulum.datetime(2026, 7, 8, tz="UTC"),
    catchup=False,
    tags=["machine_learning", "classification", "gemstone"],
) as dag:

    dag.doc_md = __doc__

    # ---------------- Data Ingestion ---------------- #
    def data_ingestion(**kwargs):
        ti = kwargs["ti"]

        train_data_path, test_data_path = (
            training_pipeline.start_data_ingestion()
        )

        ti.xcom_push(
            key="data_ingestion_artifact",
            value={
                "train_data_path": train_data_path,
                "test_data_path": test_data_path,
            },
        )

    # ---------------- Data Transformation ---------------- #
    def data_transformations(**kwargs):
        ti = kwargs["ti"]

        data_ingestion_artifact = ti.xcom_pull(
            task_ids="data_ingestion",
            key="data_ingestion_artifact",
        )

        train_arr, test_arr = training_pipeline.start_data_transformation(
            data_ingestion_artifact["train_data_path"],
            data_ingestion_artifact["test_data_path"],
        )

        train_arr = train_arr.tolist()
        test_arr = test_arr.tolist()

        ti.xcom_push(
            key="data_transformations_artifact",
            value={
                "train_arr": train_arr,
                "test_arr": test_arr,
            },
        )

    # ---------------- Model Training ---------------- #
    def model_trainer(**kwargs):
        import numpy as np

        ti = kwargs["ti"]

        data_transformation_artifact = ti.xcom_pull(
            task_ids="data_transformation",
            key="data_transformations_artifact",
        )

        train_arr = np.array(data_transformation_artifact["train_arr"])
        test_arr = np.array(data_transformation_artifact["test_arr"])

        training_pipeline.start_model_training(train_arr, test_arr)

    # ---------------- Save Artifacts Locally ---------------- #
    def push_data_to_local(**kwargs):
        source_folder = "/app/artifacts"
        destination_folder = "/app/artifacts_backup"

        os.makedirs(destination_folder, exist_ok=True)

        for file_name in os.listdir(source_folder):
            src = os.path.join(source_folder, file_name)
            dst = os.path.join(destination_folder, file_name)

            if os.path.isfile(src):
                shutil.copy2(src, dst)

        print(f"Artifacts copied to {destination_folder}")

    # ---------------- Airflow Tasks ---------------- #

    data_ingestion_task = PythonOperator(
        task_id="data_ingestion",
        python_callable=data_ingestion,
    )

    data_ingestion_task.doc_md = dedent(
        """
        #### Ingestion Task
        This task creates the train and test datasets.
        """
    )

    data_transform_task = PythonOperator(
        task_id="data_transformation",
        python_callable=data_transformations,
    )

    data_transform_task.doc_md = dedent(
        """
        #### Transformation Task
        This task performs data transformation.
        """
    )

    model_trainer_task = PythonOperator(
        task_id="model_trainer",
        python_callable=model_trainer,
    )

    model_trainer_task.doc_md = dedent(
        """
        #### Model Training Task
        This task trains the model and saves the artifacts.
        """
    )

    push_data_to_local_task = PythonOperator(
        task_id="save_artifacts",
        python_callable=push_data_to_local,
    )

    push_data_to_local_task.doc_md = dedent(
        """
        #### Save Artifacts Task
        This task copies the generated artifacts to a local backup folder.
        """
    )

    # ---------------- DAG Dependencies ---------------- #

    (
        data_ingestion_task
        >> data_transform_task
        >> model_trainer_task
        >> push_data_to_local_task
    )