import unittest

from tire.carrigan_tire import CarriganTire


class TestCarriganTires(unittest.TestCase):
    def test_needs_service_true(self):
        tire_wear_sensor_values = [0.1, 0.3, 0.2, 0.9]
        tire = CarriganTire(tire_wear_sensor_values)
        self.assertTrue(tire.needs_service())

    def test_needs_service_false(self):
        tire_wear_sensor_values = [0.1, 0.2, 0.4, 0.2]
        tire = CarriganTire(tire_wear_sensor_values)
        self.assertFalse(tire.needs_service())
        