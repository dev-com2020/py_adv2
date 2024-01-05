import cube
import unittest


class TestCube(unittest.TestCase):
    def test_0(self):
        self.assertEqual(cube.cube(0), 0)


if __name__ == '__main__':
    unittest.main()