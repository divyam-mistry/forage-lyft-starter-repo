from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine

from battery.spindler_battery import SpindlerBattery
from battery.nubbin_battery import NubbinBattery
from car import  Car
from datetime import datetime


class CarFactory():

    def create_calliope(self, last_service_date, last_service_mileage, current_mileage):
        current_date = datetime.today().date()
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        car = Car(engine, battery)
        return car
    
    def create_glissade(self, last_service_date, last_service_mileage, current_mileage):
        current_date = datetime.today().date()
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        car = Car(engine, battery)
        return car
    
    def create_palindrome(self, last_service_date, warning_light_is_on):
        current_date = datetime.today().date()
        engine = SternmanEngine(warning_light_is_on)
        battery = SpindlerBattery(last_service_date, current_date)
        car = Car(engine, battery)
        return car
    
    def create_rorschach(self, last_service_date, last_service_mileage, current_mileage):
        current_date = datetime.today().date()
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        car = Car(engine, battery)
        return car
        
    def create_thovex(self, last_service_date, last_service_mileage, current_mileage):
        current_date = datetime.today().date()
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        car = Car(engine, battery)
        return car
