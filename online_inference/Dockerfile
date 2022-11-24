FROM python:3.10-slim-buster

COPY requirements.txt main.py ./service/

COPY utils/ ./service/utils/

WORKDIR /service/

RUN pip install -r requirements.txt

ENV MODEL_PATH="model.joblib"

ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "9000"]
