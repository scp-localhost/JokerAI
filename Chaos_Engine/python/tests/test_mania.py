import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from joker_core.manic_reasoning import pressure_speech
from unittest.mock import patch

class TestManicEpisodes(unittest.TestCase):
    def test_pressure_speech_escalation(self):
        """YMRS Criteria A1: Elevated mood"""
        result = pressure_speech("Test.", 0.7)
        self.assertTrue(result.isupper())
        self.assertGreater(len(result), len("Test."))

    @patch('random.choice', return_value=" HAHA")
    def test_laughter_injection(self, mock_choice):
        """DSM-5-TR 296.41: Pathological laughter"""
        result = pressure_speech("test", 0.9)
        self.assertIn("HAHA", result)
