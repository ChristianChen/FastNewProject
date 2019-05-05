import unittest

from src.gakki import gakki


class GakkiTest(unittest.TestCase):

    def test_can_display_usage_when_no_arguments_inputted(self):
        result = gakki()
        self.assertNotEqual(0, result['code'])
        self.assertEqual('''Usage:
gakki <java|python|node> [optional libraries]''', result['msg'])
        print(result)


if __name__ == '__main__':
    unittest.main()
