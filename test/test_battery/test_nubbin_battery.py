import unittest
from datetime import date

from battery.nubbin_battery import NubbinBattery


class TestNubbinBattery(unittest.TestCase):
    def test_needs_service_true(self):
        current_date = date.fromisoformat("2024-05-15")
        last_service_date = date.fromisoformat("2020-01-25")
        battery = NubbinBattery(
            last_service_date=last_service_date,
            current_date=current_date
        )
        self.assertTrue(battery.needs_service())

    def test_needs_service_false(self):
        current_date = date.fromisoformat("2024-05-15")
        last_service_date = date.fromisoformat("2023-01-10")
        battery = NubbinBattery(
            last_service_date=last_service_date,
            current_date=current_date
        )
        self.assertFalse(battery.needs_service())