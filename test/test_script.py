import unittest
import operaciones

class TestOperaciones(unittest.TestCase):

    def test_suma(self):
        self.assertEqual(operaciones.suma(3, 2), 5)
        self.assertEqual(operaciones.suma(-1, 1), 0)
        self.assertEqual(operaciones.suma(-1, -1), -2)

if __name__ == '__main__':
    unittest.main()
