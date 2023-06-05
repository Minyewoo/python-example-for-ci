import unittest
from hello_world import get_hello_world

class HelloWorldTestCase(unittest.TestCase):
    def test_returns_normally(self):
        try:
            get_hello_world()
        except:
            self.fail("get_hello_world() raised unexpectedly!")

    def test_returned_string(self):
        self.assertEqual(
            first=get_hello_world(),
            second='Hello World!',
            msg='wrong hello world string',
        )