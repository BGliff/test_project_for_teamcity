ARG TEST_PARAMETER
ARG NEXUS_PYPI_URL

FROM $TEST_PARAMETER/python:3.9

WORKDIR usr/src/app

#ENV NEXUS_PYPI_URL $NEXUS_PYPI_URL

COPY requirements.txt ./
# COPY pip.conf /etc/pip.conf


RUN pip install --index http://test:ffilgecurb@$NEXUS_PYPI_URL/simple \
    --extra-index-url http://test:ffilgecurb@$NEXUS_PYPI_URL/simple \
    --extra-index-url http://test:ffilgecurb@${NEXUS_PYPI_URL}/pypi \
    -r requirements.txt

COPY . .

#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]