import unittest
import requests

class TestResearchAPI(unittest.TestCase):
    BASE_URL = "https://websearchai-production.up.railway.app/api/research/run"
    HEADERS = {
        "accept": "application/json",
        "Content-Type": "application/json"
    }

    def test_successful_it_jobs_query(self):
        """Test with the provided query about IT jobs success in 2025"""
        payload = {
            "query": "how to be sucessfull in 2025 threw it jobs"
        }
        response = requests.post(self.BASE_URL, json=payload, headers=self.HEADERS)
        self.assertIsNotNone(response, "No response received")
        self.assertEqual(response.status_code, 200, f"Expected status 200, got {response.status_code}")

    def test_empty_query(self):
        """Test with an empty query string"""
        payload = {
            "query": ""
        }
        response = requests.post(self.BASE_URL, json=payload, headers=self.HEADERS)
        self.assertIsNotNone(response, "No response received")

    def test_different_query(self):
        """Test with a different valid query"""
        payload = {
            "query": "best programming languages for 2025"
        }
        response = requests.post(self.BASE_URL, json=payload, headers=self.HEADERS)
        self.assertIsNotNone(response, "No response received")
        self.assertEqual(response.status_code, 200, f"Expected status 200, got {response.status_code}")

    def test_invalid_json_format(self):
        """Test with malformed JSON payload"""
        payload = {
            "wrong_key": "how to be successful"
        }
        response = requests.post(self.BASE_URL, json=payload, headers=self.HEADERS)
        self.assertIsNotNone(response, "No response received")

    def test_long_query(self):
        """Test with a long query string"""
        long_query = "how to become successful in IT jobs in 2025 " * 10
        payload = {
            "query": long_query
        }
        response = requests.post(self.BASE_URL, json=payload, headers=self.HEADERS)
        self.assertIsNotNone(response, "No response received")

if __name__ == "__main__":
    unittest.main()