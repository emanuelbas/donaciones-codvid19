import unittest
import app


class TestAplicacionArriba(unittest.TestCase):

    def setUp(self):
        self.app = app.create_app()
        self.app.testing = True
        self.app = self.app.test_client(self)
        

    def test_flask_arriba(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()