import os
import unittest

from src.gakki import Gakki
from src.gakki import gakki

PROJECT_NAME = 'for_test'


class GakkiTest(unittest.TestCase):

    def tearDown(self):
        print('Tearing down!')
        if os.path.exists(PROJECT_NAME):
            os.rmdir(PROJECT_NAME)
            print('Removed temporary folder:%s' % PROJECT_NAME)

    def test_can_display_usage_when_no_arguments_inputted(self):
        result = gakki()
        self.assertNotEqual(0, result['code'])
        self.assertEqual('''Usage:
gakki project_name <java|python|node> [optional libraries]''', result['msg'])
        print(result)

    def test_can_create_java_with_gradle_as_default_project(self):
        result = gakki(Gakki(PROJECT_NAME))
        self.assertEqual(0, result['code'])
        print(result)


if __name__ == '__main__':
    unittest.main()
