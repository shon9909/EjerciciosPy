import unittest
from EjerciciosPy.Ejer2 import par
class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, par(20))
if __name__ == '__main__':
    unittest.main()
