import unittest
from advent_two import first_reported_list_result


class TestAdventTwo(unittest.TestCase):

        def test_first_repeated_list_result(self):
                example_list = [+3, +3, +4, -2, -4]
                example_result = 10
                start_value = 0
                reached_set = set()
                self.assertEqual(
                        example_result,
                        first_reported_list_result(
                                example_list,
                                start_value,
                                reached_set
                        )
                )





