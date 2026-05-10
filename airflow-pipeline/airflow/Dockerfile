FROM apache/airflow:2.2.2-python3.8
COPY requirements.txt /tmp
USER root
RUN sed -i 's|http://deb.debian.org/debian|http://archive.debian.org/debian|g' /etc/apt/sources.list \
    && sed -i 's|http://security.debian.org/debian-security|http://archive.debian.org/debian-security|g' /etc/apt/sources.list \
    && printf 'Acquire::Check-Valid-Until "false";\nAcquire::AllowInsecureRepositories "true";\n' > /etc/apt/apt.conf.d/99archive \
    && apt-get update \
    && apt-get install --no-install-recommends -y openjdk-11-jre-headless \
    && rm -rf /var/lib/apt/lists/*
ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
RUN if [ -f "${JAVA_HOME}/conf/security/java.security" ]; then \
        sed -i 's/, TLSv1, TLSv1.1//g' "${JAVA_HOME}/conf/security/java.security"; \
    fi \
    && if [ -f "${JAVA_HOME}/jre/lib/security/java.security" ]; then \
        sed -i 's/, TLSv1, TLSv1.1//g' "${JAVA_HOME}/jre/lib/security/java.security"; \
    fi
ENV JAVA_TOOL_OPTIONS="-Djdk.tls.client.protocols=TLSv1,TLSv1.1,TLSv1.2"
RUN mkdir -p /usr/local/airflow
RUN ln -s  /opt/airflow/dags /usr/local/airflow/dags 
RUN chown -R airflow /usr/local/airflow 
USER airflow
RUN python3 -m pip install --no-cache-dir -r /tmp/requirements.txt
