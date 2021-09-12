import unittest

import main # import main.py

class MainTest(unittest.TestCase):
    def test_helloworld(self):
        ret = main.helloworld("Test")
        self.assertEqual(ret, "Hello World, Sang-hyun!")


if __name__ == "__main__":
    unittest.main()