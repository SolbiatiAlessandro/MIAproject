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


default_args = {
    'owner': 'alessandro',
    'start_date': dt.datetime(2018, 10, 3, 15, 58, 00),
    'concurrency': 1,
    'retries': 0
}

def set_variable(variable_key, variable_val):
    """
    workaround for 
        sqlalchemy.exc.IntegrityError: (sqlite3.IntegrityError) 
        UNIQUE constraint failed: variable.key
    """
    variable = Variable.get(variable_key, default_var=None)
    if variable is None:
        variable = Variable.set(variable_key, variable_val)

def set_variables(
        batch_start = 0, 
        batch_size = 5
        ):
    set_variable(BATCH_VARIABLE_NAMES[1], batch_start)
    set_variable(BATCH_VARIABLE_NAMES[0], batch_size)

with DAG('youtube_translation_encyclopedia',
         catchup=False,
         default_args=default_args,
         schedule_interval='0 * * * *', # every minute
         ) as dag:

    ## SET VARIABLES (alex) I am not sure if this is the right place
    set_variables()

    ## DECLARE OPERATORS
    opr_scrape_untranslated_videos = PythonOperator(
            task_id='scrape_untranslated_videos',
            python_callable=scrape_untranslated_videos, 
            provide_context=True)
    opr_translate_scripts = PythonOperator(
            task_id='translate_scripts',
            python_callable=translate_scripts, 
            provide_context=True)
    opr_generate_translated_videos = PythonOperator(
            task_id='generate_translated_videos',
            python_callable=generate_translated_videos, 
            provide_context=True)
    opr_upload_translated_videos = PythonOperator(
            task_id='upload_translated_videos',
            python_callable=upload_translated_videos, 
            provide_context=True)

opr_scrape_untranslated_videos >> opr_translate_scripts >> opr_generate_translated_videos >> opr_upload_translated_videos


