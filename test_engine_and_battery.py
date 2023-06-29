import unittest
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from battery.spindler_battery import SpindlerBattery
from battery.nubbin_battery import NubbinBattery
from tire.carrigan_tire import CarriganTire
from tire.octoprime_tire import OctoprimeTire
from datetime import date

class TestCapuletEngine(unittest.TestCase):
    def test_needs_service_true(self):
        current_mileage = 30001
        last_service_mileage = 0
        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_needs_service_false(self):
        current_mileage = 30000
        last_service_mileage = 0
        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())
        
class TestWilloughbyEngine(unittest.TestCase):
    def test_needs_service_true(self):
        current_mileage = 60001
        last_service_mileage = 0
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_needs_service_false(self):
        current_mileage = 100000
        last_service_mileage = 90000
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())
        
class TestSternmanEngine(unittest.TestCase):
    def test_needs_service_true(self):
        warning_light_is_on = True
        engine = SternmanEngine(warning_light_is_on)
        self.assertTrue(engine.needs_service())

    def test_needs_service_false(self):
        warning_light_is_on = False
        engine = SternmanEngine(warning_light_is_on)
        self.assertFalse(engine.needs_service())
        
class TestSpindlerBattery(unittest.TestCase):
    def test_needs_service_true(self):
        current_date = date.fromisoformat("2023-06-25")
        last_service_date = date.fromisoformat("2020-02-25")
        battery = SpindlerBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_needs_service_false(self):
        current_date = date.fromisoformat("2023-06-25")
        last_service_date = date.fromisoformat("2022-02-25")
        battery = SpindlerBattery(current_date, last_service_date)
        self.assertFalse(battery.needs_service())
        
class TestNubbinBattery(unittest.TestCase):
    def test_needs_service_true(self):
        current_date = date.fromisoformat("2023-06-25")
        last_service_date = date.fromisoformat("2019-02-25")
        battery = NubbinBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_needs_service_false(self):
        current_date = date.fromisoformat("2023-06-25")
        last_service_date = date.fromisoformat("2022-02-25")
        battery = NubbinBattery(current_date, last_service_date)
        self.assertFalse(battery.needs_service())
        
class TestCarriganTire(unittest.TestCase):
    def test_needs_service_true(self):
        tire_worn_data = [0,0.9,1,0]
        tire = CarriganTire(tire_worn_data)
        self.assertTrue(tire.needs_service())

    def test_needs_service_false(self):
        tire_worn_data = [0.7,0.4,0.66,0.89]
        tire = CarriganTire(tire_worn_data)
        self.assertFalse(tire.needs_service())
        
class TestOctoprimeTire(unittest.TestCase):
    def test_needs_service_true(self):
        tire_worn_data = [1,0.9,1,0.1]
        tire = OctoprimeTire(tire_worn_data)
        self.assertTrue(tire.needs_service())

    def test_needs_service_false(self):
        tire_worn_data = [0.7,0.4,0.86,0.89]
        tire = OctoprimeTire(tire_worn_data)
        self.assertFalse(tire.needs_service())