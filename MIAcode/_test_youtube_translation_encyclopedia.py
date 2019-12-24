import datetime as dt
import json
import os
import uuid
from time import sleep

# AIRFLOW IMPORTS
import requests
from airflow import DAG
from airflow.models import Variable
from airflow.operators.email_operator import EmailOperator
from airflow.operators.python_operator import PythonOperator

# MIA IMPORTS
import sys
AIRFLOW_HOME = "/usr/local/airflow/"
sys.path.append(os.path.join(AIRFLOW_HOME, "MIAtranslation"))
sys.path.append("../")
from MIAtranslation.scrape_untranslated_videos import scrape_untranslated_videos, BATCH_VARIABLE_NAMES
from MIAtranslation.translate_scripts import translate_scripts
from MIAtranslation.generate_translated_videos import generate_translated_videos
from MIAtranslation.upload_translated_videos import upload_translated_videos
from MIAtranslation.upload_translated_videos import _test_operator as test_upload_translated_videos


default_args = {
    'owner': 'alessandro',
    'start_date': dt.datetime(2018, 10, 3, 15, 58, 00),
    'concurrency': 1,
    'retries': 0
}

with DAG('_test_youtube_translation_encyclopedia',
         catchup=False,
         default_args=default_args,
         schedule_interval=None,
         ) as dag:

    opr_test_upload_translated_videos = PythonOperator(
            task_id='test_upload_translated_videos',
            python_callable=test_upload_translated_videos, 
            provide_context=True)


opr_test_upload_translated_videos 
