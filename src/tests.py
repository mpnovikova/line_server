import unittest

from line_service import LineService


class TestLineService(unittest.TestCase):
    def setUp(self):
        self.filepath = 'odyssey.txt'
        self.cachesize = 100
        self.line_service = LineService(filepath=self.filepath, cachesize=self.cachesize)
        try:
            f = open(self.filepath, "r")
            self.test_lines = f.readlines()
            f.close()
        except OSError:
            self.test_lines = []

    def test_get_line(self):
        self.assertEqual(self.line_service.get_line(145), self.test_lines[145])

    def test_index(self):
        self.assertEqual(len(self.line_service.index), self.cachesize)
        expected_indices = [i for i in range(len(self.test_lines) - 100, len(self.test_lines))]
        print(list(reversed(expected_indices)))
        print(list(self.line_service.index.keys()))


if __name__ == '__main__':
    unittest.main()
