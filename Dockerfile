FROM puckel/docker-airflow
COPY MIAdags ${AIRFLOW_HOME}/dags
CMD ["webserver"] # set default arg for entrypoint
