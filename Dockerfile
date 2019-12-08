FROM puckel/docker-airflow
COPY MIAcode ${AIRFLOW_HOME}/dags
COPY tests.py ${AIRFLOW_HOME}/tests.py
COPY MIAcode/MIAutils/scraper/requirements.txt ${AIRFLOW_HOME}/scraper_requirements.txt
RUN pip install -r scraper_requirements.txt --user
RUN /usr/local/airflow/.local/bin/pyppeteer-install
ENTRYPOINT ["/entrypoint.sh"]
CMD ["python", "./tests.py"] 
