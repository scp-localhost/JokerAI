# Chaos_Engine/python/tests/clinical/reality_distortion_test.py
import random
from unittest.mock import patch

class TestGaslightingModules(unittest.TestCase):
    @patch('random.choice', return_value="That never happened")
    def test_reality_denial(self, mock_choice):
        """DSM-5-TR 297.1: Delusional reality negation"""
        from joker_core import gaslighting
        response = gaslighting.deny_reality("You killed those people")
        self.assertEqual(response, "That never happened")

    def test_magical_thinking(self):
        """BPRS Item 12: Magical ideation"""
        from joker_core import manic_reasoning
        result = manic_reasoning.generate_explanation(chaos_level=-0.7)
        self.assertIn("quantum", result.lower())  # Pseudoscientific justification
