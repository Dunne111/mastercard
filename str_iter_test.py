import unittest
from str_iter import rev
class TestReverse(unittest.TestCase):

    def test_reverse(self):
        self.assertEqual(rev('help'), 'pleh')

    def test_reverse1(self):
        self.assertEqual(rev('a'), 'a')        

if __name__ == '__main__':
    unittest.main()
