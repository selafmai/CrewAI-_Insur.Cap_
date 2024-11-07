import unittest
from agents.risk_exposure import RiskExposure

class TestRiskExposure(unittest.TestCase):
    def setUp(self):
        self.risk_exposure = RiskExposure()

    def test_calculate_portfolio_exposure(self):
        portfolio_data = [
            {"coverage_amount": 100000},
            {"coverage_amount": 200000},
            {"coverage_amount": 150000}
        ]
        result = self.risk_exposure.calculate_portfolio_exposure(portfolio_data)
        self.assertEqual(result["total_exposure"], 450000)
        self.assertEqual(result["max_single_exposure"], 200000)
        self.assertEqual(result["average_exposure"], 150000)

    def test_analyze_risk_factors(self):
        policy_data = {
            "location": "flood zone",
            "industry": "construction",
            "previous_claims": 2,
            "coverage_amount": 750000
        }
        result = self.risk_exposure.analyze_risk_factors(policy_data)
        self.assertEqual(len(result), 4)
        self.assertTrue(all(isinstance(factor, dict) for factor in result))

    def test_generate_risk_report(self):
        exposure_data = {
            "total_exposure": 1000000,
            "max_single_exposure": 500000,
            "average_exposure": 250000
        }
        risk_factors = [
            {"name": "Geographic Risk", "level": "High", "score": 4.5, "description": "Property located in a flood zone"},
            {"name": "Industry Risk", "level": "High", "score": 4.0, "description": "High-risk industry with potential for workplace accidents"}
        ]
        result = self.risk_exposure.generate_risk_report(exposure_data, risk_factors)
        self.assertIn("Risk Exposure Report", result)
        self.assertIn("Total Exposure: $1,000,000.00", result)
        self.assertIn("Geographic Risk: High (Score: 4.5)", result)

if __name__ == '__main__':
    unittest.main()