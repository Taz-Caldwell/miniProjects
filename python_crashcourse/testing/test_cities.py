import unittest
from city_functions import city_country

class CityNamesTestCase(unittest.TestCase):
    '''Tests for city_functions.py'''
    def test_city_country(self):
        '''Do names like 'Santiago, Chile work?'''
        formatted_city_country_name = city_country('santiago', 'chile')
        self.assertEqual(formatted_city_country_name, "Santiago, Chile")

if __name__ == '__main__':
    unittest.main()