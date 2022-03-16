import unittest
import sys
import json

sys.path.append("..")

from app import app

app.testing = True


class TestApp(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        self.endpoint = "/productionplan"
        self.headers = "application/json"
        self.payload = {
            "load": 910,
            "fuels": {
                "gas(euro/MWh)": 13.4,
                "kerosine(euro/MWh)": 50.8,
                "co2(euro/ton)": 20,
                "wind(%)": 60,
            },
            "powerplants": [
                {
                    "name": "gasfiredbig1",
                    "type": "gasfired",
                    "efficiency": 0.53,
                    "pmin": 100,
                    "pmax": 460,
                },
                {
                    "name": "gasfiredbig2",
                    "type": "gasfired",
                    "efficiency": 0.53,
                    "pmin": 100,
                    "pmax": 460,
                },
                {
                    "name": "gasfiredsomewhatsmaller",
                    "type": "gasfired",
                    "efficiency": 0.37,
                    "pmin": 40,
                    "pmax": 210,
                },
                {
                    "name": "tj1",
                    "type": "turbojet",
                    "efficiency": 0.3,
                    "pmin": 0,
                    "pmax": 16,
                },
                {
                    "name": "windpark1",
                    "type": "windturbine",
                    "efficiency": 1,
                    "pmin": 0,
                    "pmax": 150,
                },
                {
                    "name": "windpark2",
                    "type": "windturbine",
                    "efficiency": 1,
                    "pmin": 0,
                    "pmax": 36,
                },
            ],
        }
        self.response_data = [
            {"name": "windpark1", "p": 90},
            {"name": "windpark2", "p": 22},
            {"name": "gasfiredbig1", "p": 460},
            {"name": "gasfiredbig2", "p": 338},
        ]

    def test_response_is_ok(self):
        response = self.client.post(
            self.endpoint, data=json.dumps(self.payload), content_type=self.headers
        )
        self.assertEqual(response.status_code, 200)

    def test_response_is_json(self):
        response = self.client.post(
            self.endpoint, data=json.dumps(self.payload), content_type=self.headers
        )
        self.assertEqual(
            type(response.data.decode("UTF-8")), type(json.dumps(self.response_data))
        )

    def test_response_is_correct(self):
        response = self.client.post(
            self.endpoint, data=json.dumps(self.payload), content_type=self.headers
        )
        self.assertEqual(response.data.decode("UTF-8"), json.dumps(self.response_data))

    def test_first_load_is_ok(self):
        response = self.client.post(
            self.endpoint, data=json.dumps(self.payload), content_type=self.headers
        )
        data = list(json.loads(response.data.decode("UTF-8")))
        self.assertEqual(data[0]["p"], 90)

    def test_sum_response_loads_equals_input_load(self):
        response = self.client.post(
            self.endpoint, data=json.dumps(self.payload), content_type=self.headers
        )
        data = list(json.loads(response.data.decode("UTF-8")))
        response_load_sum = sum([powerplant["p"] for powerplant in data])
        self.assertEqual(response_load_sum, self.payload["load"])
