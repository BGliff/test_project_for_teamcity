FROM localhost:8083/python:3.9

WORKDIR usr/src/app

COPY requirements.txt ./
COPY pip.conf /etc/pip.conf

RUN export NEXUS_CI_USER=$NEXUS_CI_USER
RUN export NEXUS_CI_PASSWORD=$NEXUS_CI_PASSWORD
RUN export NEXUS_PYPI_URL=$NEXUS_PYPI_URL
RUN pip install -r requirements.txt

COPY . .

#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]