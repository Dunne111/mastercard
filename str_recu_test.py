import unittest
from str_recu import rev
class TestReverse(unittest.TestCase):

    def test_reverse(self):
        self.assertEqual(rev('hello'), 'olleh')


if __name__ == '__main__':
    unittest.main()
