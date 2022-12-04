FROM airflow-ml-base:latest

COPY validate.py /validate.py

COPY requirements.txt /requirements.txt

RUN pip3 install -r requirements.txt

ENTRYPOINT ["python", "validate.py"]
