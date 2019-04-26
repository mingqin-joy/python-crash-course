from unittest import TestCase, main
#import unittest

from PythonCrashCourse.Chapter11.name_function import get_formatted_name

# class NameTestCase(unittest.TestCase):


class NameTestCase(TestCase):
    def test_first_last_name(self):
        formatted_name = get_formatted_name(
            'janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_middle_last_name(self):
        formatted_name = get_formatted_name(
            'wolfgang', 'mozart')
        self.assertEqual(formatted_name, 'Janis Joplin')


# unittest.main()
main()
