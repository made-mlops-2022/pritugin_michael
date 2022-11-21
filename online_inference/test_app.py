from fastapi.testclient import TestClient
from utils.fake import generate_data
import unittest
from main import app
import json


class TestApp(unittest.TestCase):
    def test_predict(self):
        with TestClient(app) as client:
            for data in generate_data(100):
                response = client.post("/predict", content=json.dumps(data))

                self.assertEqual(response.status_code, 200)
                self.assertTrue("condition" in response.json())

    def test_health(self):
        with TestClient(app) as client:
            response = client.get("http://localhost:8000/health")

            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json()["status"], "ok")
