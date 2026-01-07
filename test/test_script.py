import unittest
import script

class Testscript(unittest.TestCase):

    def test_suma(self):
        self.assertEqual(script.suma(3, 2), 5)
        self.assertEqual(script.suma(-1, 1), 0)
        self.assertEqual(script.suma(-1, -1), -2)

    def test_resta(self):
        self.assertEqual(script.resta(10, 5), 5)
        self.assertEqual(script.resta(5, 10), -5)

    def test_multiplicacion(self):
        self.assertEqual(script.multiplicacion(3, 3), 9)
        self.assertEqual(script.multiplicacion(10, 0), 0)

    def test_division(self):
        self.assertEqual(script.division(10, 2), 5)
        self.assertEqual(script.division(5, 2), 2.5)
        # Testeamos el caso borde de división por cero tal como lo definiste en tu código
        self.assertEqual(script.division(5, 0), "Error: No se puede dividir por cero.")

    def test_media(self):
        self.assertEqual(script.media(10, 20), 15)
        self.assertEqual(script.media(5, 5), 5)

if __name__ == '__main__':
    unittest.main()
