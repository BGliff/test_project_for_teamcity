ARG env_TEST_PARAMETER='localhost:8083'

FROM $env_TEST_PARAMETER/python:3.9

WORKDIR usr/src/app

COPY requirements.txt ./
COPY pip.conf /etc/pip.conf

RUN pip install -r requirements.txt

COPY . .

#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]