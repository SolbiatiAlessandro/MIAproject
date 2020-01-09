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

# text_to_video libraries
# video generation
COPY MIAcode/MIAutils/text_to_video/requirements_generate_video_utils.txt ${AIRFLOW_HOME}/requirements_generate_video_utils.txt
COPY MIAcode/MIAutils/text_to_video/requirements_text_to_audio.txt ${AIRFLOW_HOME}/requirements_text_to_audio.txt
RUN pip install -r requirements_generate_video_utils.txt
RUN apt-get update \
	&& apt-get install -y imagemagick
RUN mv /etc/ImageMagick-6/policy.xml /etc/ImageMagick-6/policy.xmlout
COPY MIAcode/MIAutils/text_to_video/static ${AIRFLOW_HOME}/static

# audio
COPY MIAcode/MIAutils/text_to_video/tts/voicerss_key.json ${AIRFLOW_HOME}/voicerss_key.json

# upload_translated_videos libraries
COPY MIAcode/MIAutils/google_wrapper/requirements.txt ${AIRFLOW_HOME}/requirements_google_wrapper.txt
RUN pip install -r requirements_google_wrapper.txt
COPY MIAcode/MIAutils/google_wrapper/client_secrets.json ${AIRFLOW_HOME}/client_secrets.json
RUN pip install -r requirements_google_wrapper.txt

# COPY MIAcode/MIAutils/google_wrapper/test_video.mp4 .

# GOOGLE AUTH
RUN pip install 'apache-airflow[google_auth]'
# overwriting config with my config with google secrets
COPY airflow.cfg ${AIRFLOW_HOME}/airflow.cfg
# read MIAdocs 1.3 for more info about this
COPY access_token.json /usr/local/bin/airflow-oauth2.json

# ---
# POSTGRES 
RUN pip install psycopg2-binary
ENV POSTGRES_HOST localhost
ENV POSTGRES_PORT 5432
ENV POSTGRES_USER airflow
ENV POSTGRES_PASSWORD airflow
ENV POSTGRES_DB airflow

# also added lines to airflow.cfg
# sql_alchemy_conn = postgresql+psycopg2://airflow_user:airflow_user22122019@postgres:5432/airflow_db

# I try to connect to postgres and I get this error
# https://github.com/puckel/docker-airflow/issues/290
# this export does not work
# looks like I can solve it like here
# https://github.com/puckel/docker-airflow/issues/298
ENV AIRFLOW__CORE__FERNET_KEY $(python -c "from cryptography.fernet import Fernet; FERNET_KEY = Fernet.generate_key().decode(); print(FERNET_KEY)")

# ---

# LEAVE THIS AT THE END SO WHEN YOU CHANGE CODE IT DOES
# NOT REBUILD THE ENTIRE DOCKER

# -------
# this is a really dumb workaround because I don't know how
# to change name of dags_folder in airflow.cfg
COPY docs docs
# TESTS (pytest)
COPY tests.py ${AIRFLOW_HOME}/tests.py
COPY MIAcode ${AIRFLOW_HOME}/dags
# need this for hardcoded import in DOCS
COPY MIAcode ${AIRFLOW_HOME}/MIAcode
ENTRYPOINT ["/entrypoint.sh"]
