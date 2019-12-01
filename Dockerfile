FROM puckel/docker-airflow
COPY MIAcode ${AIRFLOW_HOME}/dags
COPY tests.py ${AIRFLOW_HOME}/tests.py
ENTRYPOINT ["/entrypoint.sh"]
CMD ["python", "./tests.py"] 
