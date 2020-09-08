import unittest
from EjerciciosPy.Ejerc3 import caracter
class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual("an", caracter("amen"))
if __name__ == '__main__':
    unittest.main()
