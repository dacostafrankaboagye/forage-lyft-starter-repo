import unittest
from datetime import datetime

from car_factory import CarFactory

''' Service Criteria

Calliope = Capulet Engine + Spindler Battery
        Capulet Engine = once every 30,000 miles
        Splinder Battery = once every 2 years
'''

class TestCalliope(unittest.TestCase):

    def test_battery_should_be_serviced(self):

        today = datetime.today().date()
        current_date = today
        last_service_date = today.replace(year=today.year - 4) # more than 3 years = needs servicing
        
        current_mileage = 0
        last_service_mileage = 0
        
        tire_wear_sensor_values = [0.1, 0.2, 0.4, 0.2]

        car = CarFactory.create_calliope(
            current_mileage=current_mileage,
            last_service_date=last_service_date,
            last_service_mileage=last_service_mileage,
            current_date=current_date,
            tire_wear_sensor_values=tire_wear_sensor_values
        )

        self.assertTrue(car.needs_service())

    def test_engine_should_be_serviced(self):

        today = datetime.today().date()
        current_date = today
        last_service_date = today

        current_mileage = 30001
        last_service_mileage = 0

        tire_wear_sensor_values = [0.1, 0.2, 0.4, 0.2]

        car = CarFactory.create_calliope(
            current_mileage=current_mileage,
            last_service_date=last_service_date,
            last_service_mileage=last_service_mileage,
            current_date=current_date,
            tire_wear_sensor_values=tire_wear_sensor_values
        )

        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):

        today = datetime.today().date()
        current_date = today
        last_service_date = today.replace(year=today.year - 1) # not more than 3 years = needs servicing
        
        current_mileage = 0
        last_service_mileage = 0

        tire_wear_sensor_values = [0.1, 0.2, 0.4, 0.2]

        car = CarFactory.create_calliope(
            current_mileage=current_mileage,
            last_service_date=last_service_date,
            last_service_mileage=last_service_mileage,
            current_date=current_date,
            tire_wear_sensor_values=tire_wear_sensor_values
        )

        self.assertFalse(car.needs_service())

    def test_engine_should_not_be_serviced(self):

        today = datetime.today().date()
        current_date = today
        last_service_date = today

        current_mileage = 30000
        last_service_mileage = 0

        tire_wear_sensor_values = [0.1, 0.2, 0.4, 0.2]

        car = CarFactory.create_calliope(
            current_mileage=current_mileage,
            last_service_date=last_service_date,
            last_service_mileage=last_service_mileage,
            current_date=current_date,
            tire_wear_sensor_values=tire_wear_sensor_values
        )

        self.assertFalse(car.needs_service())

    def test_tire_should_be_serviced(self):

        today = datetime.today().date()
        current_date = today
        last_service_date = today

        current_mileage = 0
        last_service_mileage = 0

        tire_wear_sensor_values = [0.1, 0.3, 0.2, 0.9]

        car = CarFactory.create_calliope(
            current_mileage=current_mileage,
            last_service_date=last_service_date,
            last_service_mileage=last_service_mileage,
            current_date=current_date,
            tire_wear_sensor_values=tire_wear_sensor_values
        )

        self.assertTrue(car.needs_service())

    def test_tire_should_not_be_serviced(self):

        today = datetime.today().date()
        current_date = today
        last_service_date = today

        current_mileage = 0
        last_service_mileage = 0

        tire_wear_sensor_values = [0.1, 0.2, 0.4, 0.2]

        car = CarFactory.create_calliope(
            current_mileage=current_mileage,
            last_service_date=last_service_date,
            last_service_mileage=last_service_mileage,
            current_date=current_date,
            tire_wear_sensor_values=tire_wear_sensor_values
        )

        self.assertFalse(car.needs_service())

#=======================================================
# glissade

''' Service Criteria

glissade = willoughby engine + Spindler Battery
        willoughby engine = once every 60,000 miles
        Splinder Battery = once every 2 years
'''

class TestGlissade(unittest.TestCase):

    def test_battery_should_be_serviced(self):

        today = datetime.today().date()
        current_date = today
        last_service_date = today.replace(year=today.year - 4) # more than 3 years = needs servicing
        
        current_mileage = 0
        last_service_mileage = 0

        tire_wear_sensor_values = [0.1, 0.2, 0.4, 0.2]

        car = CarFactory.create_glissade(
            current_date=current_date,
            last_service_date=last_service_date,
            current_mileage=current_mileage,
            last_service_mileage=last_service_mileage,
            tire_wear_sensor_values=tire_wear_sensor_values
        )

        self.assertTrue(car.needs_service())

    def test_engine_should_be_serviced(self):

        today = datetime.today().date()
        current_date = today
        last_service_date = today

        current_mileage = 60001
        last_service_mileage = 0
        tire_wear_sensor_values = [0.1, 0.2, 0.4, 0.2]

        car = CarFactory.create_glissade(
            current_mileage=current_mileage,
            last_service_date=last_service_date,
            last_service_mileage=last_service_mileage,
            current_date=current_date,
            tire_wear_sensor_values = tire_wear_sensor_values            
        )

        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):

        today = datetime.today().date()
        current_date = today
        last_service_date = today.replace(year=today.year - 1) # not more than 3 years = needs servicing
        
        current_mileage = 0
        last_service_mileage = 0

        tire_wear_sensor_values = [0.1, 0.2, 0.4, 0.2]

        car = CarFactory.create_glissade(
            current_mileage=current_mileage,
            last_service_date=last_service_date,
            last_service_mileage=last_service_mileage,
            current_date=current_date,
            tire_wear_sensor_values = tire_wear_sensor_values
        )

        self.assertFalse(car.needs_service())

    def test_engine_should_not_be_serviced(self):

        today = datetime.today().date()
        current_date = today
        last_service_date = today

        current_mileage = 60000
        last_service_mileage = 0

        tire_wear_sensor_values = [0.1, 0.2, 0.4, 0.2]

        car = CarFactory.create_glissade(
            current_mileage=current_mileage,
            last_service_date=last_service_date,
            last_service_mileage=last_service_mileage,
            current_date=current_date,
            tire_wear_sensor_values=tire_wear_sensor_values
        )

        self.assertFalse(car.needs_service())

    def test_tire_should_be_serviced(self):

        today = datetime.today().date()
        current_date = today
        last_service_date = today

        current_mileage = 0
        last_service_mileage = 0

        tire_wear_sensor_values = [0.8, 0.8, 0.8, 0.7]

        car = CarFactory.create_glissade(
            current_mileage=current_mileage,
            last_service_date=last_service_date,
            last_service_mileage=last_service_mileage,
            current_date=current_date,
            tire_wear_sensor_values=tire_wear_sensor_values
        )

        self.assertTrue(car.needs_service())

    def test_tire_should_not_be_serviced(self):

        today = datetime.today().date()
        current_date = today
        last_service_date = today

        current_mileage = 0
        last_service_mileage = 0

        tire_wear_sensor_values = [0.1, 0.2, 0.4, 0.2]

        car = CarFactory.create_glissade(
            current_mileage=current_mileage,
            last_service_date=last_service_date,
            last_service_mileage=last_service_mileage,
            current_date=current_date,
            tire_wear_sensor_values=tire_wear_sensor_values
        )

        self.assertFalse(car.needs_service())

#=======================================================
# palindrome

''' Service Criteria

palindrome= sternman engine + Spindler Battery
        sternman engine = only when the warning indicator is on
        Splinder Battery = once every 2 years
'''

class TestPalindrome(unittest.TestCase):

    def test_battery_should_be_serviced(self):

        today = datetime.today().date()
        current_date = today
        last_service_date = today.replace(year=today.year - 4) # more than 3 years = needs servicing
        
        warning_light_on = False

        tire_wear_sensor_values = [0.1, 0.2, 0.4, 0.2]

        car = CarFactory.create_palindrome(
            current_date=current_date,
            last_service_date=last_service_date,
            warning_light_on=warning_light_on,
            tire_wear_sensor_values = tire_wear_sensor_values
        )

        self.assertTrue(car.needs_service())

    def test_engine_should_be_serviced(self):

        today = datetime.today().date()
        current_date = today
        last_service_date = today

        warning_light_on = True

        tire_wear_sensor_values = [0.1, 0.2, 0.4, 0.2]

        car = CarFactory.create_palindrome(
            current_date=current_date,
            last_service_date=last_service_date,
            warning_light_on=warning_light_on,
            tire_wear_sensor_values=tire_wear_sensor_values
        )

        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):

        today = datetime.today().date()
        current_date = today
        last_service_date = today.replace(year=today.year - 1) # not more than 2 years = needs servicing
        warning_light_on = False

        tire_wear_sensor_values = [0.1, 0.2, 0.4, 0.2]

        car = CarFactory.create_palindrome(
            current_date=current_date,
            last_service_date=last_service_date,
            warning_light_on=warning_light_on,
            tire_wear_sensor_values=tire_wear_sensor_values
        )

        self.assertFalse(car.needs_service())

    def test_engine_should_not_be_serviced(self):

        today = datetime.today().date()
        current_date = today
        last_service_date = today

        warning_light_on = False

        tire_wear_sensor_values = [0.1, 0.2, 0.4, 0.2]

        car = CarFactory.create_palindrome(
            current_date=current_date,
            last_service_date=last_service_date,
            warning_light_on=warning_light_on,
            tire_wear_sensor_values=tire_wear_sensor_values
        )

        self.assertFalse(car.needs_service())

    def test_tire_should_be_serviced(self):

        today = datetime.today().date()
        current_date = today
        last_service_date = today

        warning_light_on = False

        tire_wear_sensor_values = [0.1, 0.3, 0.2, 0.9]

        car = CarFactory.create_palindrome(
            current_date=current_date,
            last_service_date=last_service_date,
            warning_light_on=warning_light_on,
            tire_wear_sensor_values=tire_wear_sensor_values
        )

        self.assertTrue(car.needs_service())

    def test_tire_should_not_be_serviced(self):

        today = datetime.today().date()
        current_date = today
        last_service_date = today

        warning_light_on = False

        tire_wear_sensor_values = [0.1, 0.2, 0.4, 0.2]

        car = CarFactory.create_palindrome(
            current_date=current_date,
            last_service_date=last_service_date,
            warning_light_on=warning_light_on,
            tire_wear_sensor_values=tire_wear_sensor_values
        )

        self.assertFalse(car.needs_service())


#=======================================================
# rorschach

''' Service Criteria

rorschach= willoughby engine + Nubbin Battery
        willoughby engine = only when the warning indicator is on
        nubbin Battery = once every 4 years
'''
class TestRorschach(unittest.TestCase):

    def test_battery_should_be_serviced(self):

        today = datetime.today().date()
        current_date = today
        last_service_date = today.replace(year=today.year - 5) # more than 4 years = needs servicing
        
        current_mileage = 0
        last_service_mileage = 0

        tire_wear_sensor_values = [0.1, 0.2, 0.4, 0.2]

        car = CarFactory.create_rorschach(
            current_date=current_date,
            last_service_date=last_service_date,
            current_mileage=current_mileage,
            last_service_mileage=last_service_mileage,
            tire_wear_sensor_values=tire_wear_sensor_values
        )

        self.assertTrue(car.needs_service())

    def test_engine_should_be_serviced(self):

        today = datetime.today().date()
        current_date = today
        last_service_date = today

        current_mileage = 60001
        last_service_mileage = 0

        tire_wear_sensor_values = [0.1, 0.2, 0.4, 0.2]

        car = CarFactory.create_rorschach(
            current_date=current_date,
            last_service_date=last_service_date,
            current_mileage=current_mileage,
            last_service_mileage=last_service_mileage,
            tire_wear_sensor_values=tire_wear_sensor_values
        )

        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):

        today = datetime.today().date()
        current_date = today
        last_service_date = today.replace(year=today.year - 3) # not more than 4 years = does not need servicing
        
        current_mileage = 0
        last_service_mileage = 0

        tire_wear_sensor_values = [0.1, 0.2, 0.4, 0.2]

        car = CarFactory.create_rorschach(
            current_date=current_date,
            last_service_date=last_service_date,
            current_mileage=current_mileage,
            last_service_mileage=last_service_mileage,
            tire_wear_sensor_values=tire_wear_sensor_values
        )

        self.assertFalse(car.needs_service())

    def test_engine_should_not_be_serviced(self):

        today = datetime.today().date()
        current_date = today
        last_service_date = today

        current_mileage = 60000
        last_service_mileage = 0

        tire_wear_sensor_values = [0.1, 0.2, 0.4, 0.2]

        car = CarFactory.create_rorschach(
            current_date=current_date,
            last_service_date=last_service_date,
            current_mileage=current_mileage,
            last_service_mileage=last_service_mileage,
            tire_wear_sensor_values=tire_wear_sensor_values
        )

        self.assertFalse(car.needs_service())

    def test_tire_should_be_serviced(self):

        today = datetime.today().date()
        current_date = today
        last_service_date = today

        current_mileage = 0
        last_service_mileage = 0

        tire_wear_sensor_values = [0.8, 0.8, 0.8, 0.7]

        car = CarFactory.create_rorschach(
            current_date=current_date,
            last_service_date=last_service_date,
            current_mileage=current_mileage,
            last_service_mileage=last_service_mileage,
            tire_wear_sensor_values=tire_wear_sensor_values
        )

        self.assertTrue(car.needs_service())

    def test_tire_should_not_be_serviced(self):

        today = datetime.today().date()
        current_date = today
        last_service_date = today

        current_mileage = 0
        last_service_mileage = 0

        tire_wear_sensor_values = [0.1, 0.2, 0.4, 0.2]

        car = CarFactory.create_rorschach(
            current_date=current_date,
            last_service_date=last_service_date,
            current_mileage=current_mileage,
            last_service_mileage=last_service_mileage,
            tire_wear_sensor_values=tire_wear_sensor_values
        )

        self.assertFalse(car.needs_service())



#=======================================================
# thovex

''' Service Criteria

thovex= capulet engine + nubbin Battery
        cpaulet engine = only when the warning indicator is on
        nubbin Battery = once every 4 years
'''
class TestThovex(unittest.TestCase):

    def test_battery_should_be_serviced(self):

        today = datetime.today().date()
        current_date = today
        last_service_date = today.replace(year=today.year - 5) # more than 4 years = needs servicing
        
        current_mileage = 0
        last_service_mileage = 0

        tire_wear_sensor_values = [0.1, 0.2, 0.4, 0.2]

        car = CarFactory.create_thovex(
            current_date=current_date,
            last_service_date=last_service_date,
            current_mileage=current_mileage,
            last_service_mileage=last_service_mileage,
            tire_wear_sensor_values=tire_wear_sensor_values
        )

        self.assertTrue(car.needs_service())

    def test_engine_should_be_serviced(self):

        today = datetime.today().date()
        current_date = today
        last_service_date = today

        current_mileage = 30001
        last_service_mileage = 0

        tire_wear_sensor_values = [0.1, 0.2, 0.4, 0.2]

        car = CarFactory.create_thovex(
            current_date=current_date,
            last_service_date=last_service_date,
            current_mileage=current_mileage,
            last_service_mileage=last_service_mileage,
            tire_wear_sensor_values=tire_wear_sensor_values
        )

        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):

        today = datetime.today().date()
        current_date = today
        last_service_date = today.replace(year=today.year - 3) # not more than 4 years = does not need servicing
        
        current_mileage = 0
        last_service_mileage = 0

        tire_wear_sensor_values = [0.1, 0.2, 0.4, 0.2]

        car = CarFactory.create_thovex(
            current_date=current_date,
            last_service_date=last_service_date,
            current_mileage=current_mileage,
            last_service_mileage=last_service_mileage,
            tire_wear_sensor_values=tire_wear_sensor_values
        )

        self.assertFalse(car.needs_service())

    def test_engine_should_not_be_serviced(self):

        today = datetime.today().date()
        current_date = today
        last_service_date = today

        current_mileage = 30000
        last_service_mileage = 0

        tire_wear_sensor_values = [0.1, 0.2, 0.4, 0.2]

        car = CarFactory.create_thovex(
            current_date=current_date,
            last_service_date=last_service_date,
            current_mileage=current_mileage,
            last_service_mileage=last_service_mileage,
            tire_wear_sensor_values=tire_wear_sensor_values
        )

        self.assertFalse(car.needs_service())

    def test_tire_should_be_serviced(self):

        today = datetime.today().date()
        current_date = today
        last_service_date = today

        current_mileage = 0
        last_service_mileage = 0

        tire_wear_sensor_values = [0.1, 0.3, 0.2, 0.9]

        car = CarFactory.create_thovex(
            current_date=current_date,
            last_service_date=last_service_date,
            current_mileage=current_mileage,
            last_service_mileage=last_service_mileage,
            tire_wear_sensor_values=tire_wear_sensor_values
        )

        self.assertTrue(car.needs_service())

    def test_tire_should_not_be_serviced(self):

        today = datetime.today().date()
        current_date = today
        last_service_date = today

        current_mileage = 0
        last_service_mileage = 0

        tire_wear_sensor_values = [0.1, 0.2, 0.4, 0.2]

        car = CarFactory.create_thovex(
            current_date=current_date,
            last_service_date=last_service_date,
            current_mileage=current_mileage,
            last_service_mileage=last_service_mileage,
            tire_wear_sensor_values=tire_wear_sensor_values
        )

        self.assertFalse(car.needs_service())



if __name__ == '__main__':
    unittest.main()