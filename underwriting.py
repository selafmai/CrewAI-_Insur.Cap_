import unittest
from unittest.mock import patch
from agents.underwriting import Underwriting

class TestUnderwriting(unittest.TestCase):
    def setUp(self):
        self.underwriting = Underwriting()

    def test_evaluate_risks(self):
        client_data = {"risk_score": 60}
        result = self.underwriting.evaluate_risks(client_data)
        self.assertIn("Medium risk client", result)
        self.assertIn("Enhanced coverage with additional riders", result)

    def test_detect_fraud(self):
        client_data = {
            "claims_history": 6,
            "credit_score": 600,
            "age": 30,
            "coverage_amount": 500000
        }
        result = self.underwriting.detect_fraud(client_data)
        self.assertFalse(result)

    def test_recommend_policy(self):
        risk_evaluation = "Medium risk client. Recommended policy: Enhanced coverage with additional riders."
        fraud_check = False
        result = self.underwriting.recommend_policy(risk_evaluation, fraud_check)
        self.assertIn("Enhanced coverage with additional riders", result)

if __name__ == '__main__':
    unittest.main()