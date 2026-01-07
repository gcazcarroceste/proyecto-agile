import unittest
import script

class TestScript(unittest.TestCase):

    def test_suma(self):
        self.assertEqual(script.suma(1, 1), 1)
        self.assertEqual(script.suma(-1, 1), 0)
        self.assertEqual(script.suma(-1, -1), -2)

if __name__ == '__main__':
    unittest.main()
