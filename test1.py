import unittest
from EjerciciosPy.Ejer1 import edad

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(72, edad(0, 1998))
if __name__ == '__main__':
    unittest.main()
