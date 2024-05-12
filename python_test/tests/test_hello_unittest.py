from unittest import TestCase
from python_test.src.module import hello_unittest

class TestHelloUnitTest(TestCase):
    def test_hello_unittest(self):
        self.assertEqual(hello_unittest.say_hello(),"hello unittest")

