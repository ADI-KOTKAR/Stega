import unittest
import requests

class ApiTests(unittest.TestCase):

    def test(self):
        API_URL = "http://127.0.0.1:5000"
        resp=requests.get("{}/{}".format(API_URL,"working"))
        print(resp.status_code, resp.content)
        self.assertEqual(resp.status_code,200)

if __name__ == '__main__':
    unittest.main()