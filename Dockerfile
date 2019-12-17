FROM puckel/docker-airflow
# we need root permission to pip install and apt-get instlal
USER root
COPY MIAcode/MIAutils/scraper/requirements.txt ${AIRFLOW_HOME}/scraper_requirements.txt
COPY MIAcode/MIAutils/generate_text/requirements.txt ${AIRFLOW_HOME}/generate_text_requirements.txt
COPY MIAcode/MIAutils/google_wrapper/requirements.txt ${AIRFLOW_HOME}/google_wrapper_requirements.txt
RUN pip install -r ${AIRFLOW_HOME}/scraper_requirements.txt
RUN pip install -r ${AIRFLOW_HOME}/generate_text_requirements.txt
RUN pip install -r ${AIRFLOW_HOME}/google_wrapper_requirements.txt
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
# INSTALL CHROMIUM
RUN pyppeteer-install

# DOCS (sphinx)
RUN apt-get update && apt-get install -y python3-sphinx
COPY docs/requirements.txt docs_requirements.txt
RUN pip install -r docs_requirements.txt
COPY docs docs

# TESTS (pytest)
COPY tests.py ${AIRFLOW_HOME}/tests.py

# ---

# LEAVE THIS AT THE END SO WHEN YOU CHANGE CODE IT DOES
# NOT REBUILD THE ENTIRE DOCKER

# -------
# this is a really dumb workaround because I don't know how
# to change name of dags_folder in airflow.cfg
COPY MIAcode ${AIRFLOW_HOME}/dags
# need this for hardcoded import in DOCS
COPY MIAcode ${AIRFLOW_HOME}/MIAcode
ENTRYPOINT ["/entrypoint.sh"]
CMD ["bash"]
