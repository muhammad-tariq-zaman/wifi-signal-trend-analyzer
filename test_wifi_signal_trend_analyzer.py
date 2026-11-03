import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import unittest
from main import analyze


def row(ap, dbm):
    return {"ap": ap, "timestamp": "2026-11-02T10:00", "signal_dbm": str(dbm)}


class TestSignalTrend(unittest.TestCase):
    def test_average_computed(self):
        result = analyze([row("AP1", -60), row("AP1", -80)])
        self.assertEqual(result[0][2], -70.0)

    def test_weak_below_minus_70(self):
        self.assertEqual(analyze([row("AP1", -75)])[0][4], "WEAK")

    def test_ok_at_minus_70(self):
        self.assertEqual(analyze([row("AP1", -70)])[0][4], "OK")

    def test_weakest_first(self):
        result = analyze([row("A", -50), row("B", -80)])
        self.assertEqual(result[0][0], "B")
