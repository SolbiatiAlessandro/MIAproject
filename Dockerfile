FROM puckel/docker-airflow
USER root
COPY MIAcode ${AIRFLOW_HOME}/dags
COPY tests.py ${AIRFLOW_HOME}/tests.py
COPY MIAcode/MIAutils/scraper/requirements.txt ${AIRFLOW_HOME}/scraper_requirements.txt
RUN pip install -r ${AIRFLOW_HOME}/scraper_requirements.txt
# INSTALL CHROMIUM
RUN pyppeteer-install
# GET CHROMIUM LIBRARIES
RUN  apt-get update \
     # (alex) added by me to make chromium work from airflow base
	 && apt-get install -y gnupg2 \ 
     # Install latest chrome dev package, which installs the necessary libs to
     # make the bundled version of Chromium that Puppeteer installs work.
     && apt-get install -y wget --no-install-recommends \
     && wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
     && sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list' \
     && apt-get update \
     && apt-get install -y google-chrome-unstable --no-install-recommends \
     && rm -rf /var/lib/apt/lists/* \
     && wget --quiet https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh -O /usr/sbin/wait-for-it.sh \
     && chmod +x /usr/sbin/wait-for-it.sh
ENTRYPOINT ["/entrypoint.sh"]
CMD ["python", "./tests.py"] 
