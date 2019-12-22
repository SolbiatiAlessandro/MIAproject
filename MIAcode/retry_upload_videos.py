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
from MIAtranslation.upload_translated_videos import reupload_videos
from miatypes import MIASCIPTS_VARIABLE, MiaScript
from youtube_translation_encyclopedia import get_miascripts_dict

default_args = {
    'owner': 'alessandro',
    'start_date': dt.datetime(2018, 10, 3, 15, 58, 00),
    'concurrency': 1,
    'retries': 0
}

def collect_videos_not_uploaded(**kwargs) -> List[MiaScript]:
    """
    read from miascript variables videos that have been
    generated but not uploaded
    """
    miascripts_dict: Dict[uuid4, MiaScript] = get_miascripts_dict()
    logging.info("examining {} miascripts"
            .format(len(miascripts_dict.keys())))

    miascripts_retry_upload: List[MiaScript] = []
    for _id, miascript in miascripts_dict:
        if miascript.has_output_video() and \
                miascript.upload_outcome == False:
            miascripts_for_upload.append(miascript)
            logging.info("collected miascript:")
            miascript._debug()

    logging.info("collected {} miascripts for reupload".
            format(len(miascripts_retry_upload)))
    return miascripts_retry_upload

with DAG('_test_youtube_translation_encyclopedia',
         catchup=False,
         default_args=default_args,
         schedule_interval='daily', 
         ) as dag:
    opr_collect_videos_not_uploaded = PythonOperator(
            task_id='collect_videos_not_uploaded',
            python_callable=collect_videos_not_uploaded,
            provide_context=True)

    opr_reupload_videos = PythonOperator(
            task_id='reupload_videos',
            python_callable=reupload_videos,
            provide_context=True)

opr_collect_videos_not_uploaded >> opr_reupload_videos
