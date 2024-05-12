import unittest
from python_test.src.module.my_sum import my_sum

class TestMySum(unittest.TestCase):
    def test_my_sum(self):
        return self.assertEqual(my_sum(1,2),3)