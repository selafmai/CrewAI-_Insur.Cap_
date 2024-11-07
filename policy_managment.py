import unittest
from agents.policy_management import PolicyManagement

class TestPolicyManagement(unittest.TestCase):
    def setUp(self):
        self.policy_management = PolicyManagement()

    def test_administer_policy(self):
        policy_data = {
            "start_date": "2023-01-01",
            "end_date": "2024-01-01",
            "risk_factor": 1.2,
            "coverage_amount": 100000
        }
        result = self.policy_management.administer_policy(policy_data)
        self.assertIn("policy_number", result)
        self.assertIn("premium", result)
        self.assertIn("deductible", result)
        self.assertIn("coverage_limits", result)

    def test_manage_claim(self):
        claim_data = {
            "incident_date": "2023-06-01",
            "policy_end_date": "2023-12-31",
            "claimed_amount": 5000,
            "coverage_limit": 10000
        }
        result = self.policy_management.manage_claim(claim_data)
        self.assertIn("is_valid", result)
        self.assertIn("status", result)
        self.assertEqual(result["status"], "Approved")

    def test_provide_customer_support(self):
        query = "How do I file a claim?"
        result = self.policy_management.provide_customer_support(query)
        self.assertIn("claim", result.lower())

if __name__ == '__main__':
    unittest.main()