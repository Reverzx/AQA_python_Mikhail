FROM jenkins/jenkins:lts

USER root

COPY requirements.txt /opt/requirements.txt

RUN apt-get update && \
    apt-get install -y python3 python3-pip python3-venv curl unzip && \
    ln -s /usr/bin/python3 /usr/bin/python && \
    python3 -m venv /opt/venv && \
    /opt/venv/bin/pip install --upgrade pip && \
    /opt/venv/bin/pip install -r /opt/requirements.txt && \
    curl -o allure.zip -L https://github.com/allure-framework/allure2/releases/download/2.24.1/allure-2.24.1.zip && \
    unzip allure.zip -d /opt/ && \
    ln -s /opt/allure-2.24.1/bin/allure /usr/bin/allure


ENV PATH="/opt/venv/bin:$PATH"

USER jenkins






USER jenkins
