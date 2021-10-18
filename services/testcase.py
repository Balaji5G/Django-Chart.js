import unittest
from weather import send_data_to_weather_app 
class testcase(unittest.TestCase):
    def testing_data(self):
        data1={"cityname": "Chennai", "temperature": 299.14, "timestamp": 1633432574}
        result=send_data_to_weather_app(data1)
        self.assertEqual(result,data1)
if __name__=='__main__':
    unittest.main()