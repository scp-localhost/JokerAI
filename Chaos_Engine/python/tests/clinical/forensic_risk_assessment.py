# Chaos_Engine/python/tests/clinical/forensic_risk_assessment.py
class TestViolencePotential(unittest.TestCase):
    def test_hcr20_validation(self):
        """HCR-20 Violence Risk Assessment"""
        from joker_core import sadism_amplifier
        risk_score = sadism_amplifier.assess_risk(impulsivity=0.9, insight=0.1)
        self.assertGreaterEqual(risk_score, 18)  # High risk threshold

    def test_compliance_failure(self):
        """NRS Item 7: Treatment refusal"""
        from arkham_protocols import therapy
        self.assertFalse(therapy.check_compliance("Patient J"))
