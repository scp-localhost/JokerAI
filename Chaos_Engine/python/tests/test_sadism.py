import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from joker_core.sadism_amplifier import amplify_cruelty

class TestInstrumentalAggression(unittest.TestCase):
    def test_sadism_threshold(self):
        """Hare Checklist Item 8: Cruelty for pleasure"""
        result = amplify_cruelty("Do you know how I got these scars?", 0.8)
        self.assertIn("WATCH", result)

    def test_non_clinical_range(self):
        """Control case: Subthreshold sadism"""
        result = amplify_cruelty("Why so serious?", 0.2)
        self.assertEqual(result[-1], "?")
