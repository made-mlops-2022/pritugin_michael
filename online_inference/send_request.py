from utils.fake import generate_data
import json
import requests


for data in generate_data(10):
    response = requests.post("http://localhost:9000/predict", json.dumps(data))

    print(response.json())

    print(response.text, response.status_code)

    response = requests.get("http://localhost:9000/health")

    print(response.text, response.status_code)
