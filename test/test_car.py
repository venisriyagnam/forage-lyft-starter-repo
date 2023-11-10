import unittest
from datetime import datetime

from car_model import CarModel
from component import Component
from modified_car import Car


class TestCar(unittest.TestCase):
    def test_battery_or_engine_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        car = CarModel()
        self.assertTrue(car.CheckServiceCriteria("engine", last_service_date))
        self.assertTrue(car.CheckServiceCriteria("battery", current_mileage))

    def test_battery_or_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0

        car = CarModel()
        self.assertTrue(car.CheckServiceCriteria("engine", last_service_date))
        self.assertTrue(car.CheckServiceCriteria("battery", current_mileage))

    def test_get_info_car(self):
        car = Car()
        id1 = 1
        self.assertTrue(car.GetInfo(id1))
    
    def test_add_new_car(self):
        car = Car()
        # get the total count from car table and increase 1
        id1 = 1
        details = {'id':id1,'company':'Honda', 'model':1}
        self.assertTrue(car.AddNew(id1, details))

    def test_get_info_component(self):
        component = Component()
        id1 = 1
        self.assertTrue(component.GetInfo(id1))
    
    def test_add_new_component(self):
        component = Component()
        # get the total count from component table and increase 1
        id1 = 1
        details = {'engine':'thovex','mileage':10,'service_riteria':30000}
        self.assertTrue(component.AddNew(id1, details))
