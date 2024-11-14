#테스트!
import unittest
from app.app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_hello_world(self):
        response = self.client.get('/')
        self.assertEqual(response.data, b'Hello, World!')

if __name__ == '__main__':
    unittest.main()
