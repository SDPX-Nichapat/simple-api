import unittest
import app

class TestApp(unittest.TestCase):

    def test_true_when_x_is_17(self):
        response = app.prime(17)
        self.assertEqual(response, "true")

    def test_false_when_x_is_36(self):
        response = app.prime(36)
        self.assertEqual(response, "false")

    def test_true_when_x_is_13219(self):
        response = app.prime(13219)
        self.assertEqual(response, "true")

    def test_get_code(self):
        response = app.getcode()
        self.assertEqual(response, "getcode")

    def test_hello_simple_api(self):
        response = app.hello("simple api")
        self.assertEqual(response, "Hello simple api")

    def test_hello_123(self):
        response = app.hello("123")
        self.assertEqual(response, "Hello 123")

if __name__ == "__main__":
    unittest.main()
