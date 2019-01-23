import unittest
from advent_one import sum_of_list


class TestAdventOne(unittest.TestCase):

        def test_sum_of_list(self):
                example_list = [1, -2, 3, 1]
                example_result = 3
                self.assertEqual(sum_of_list(example_list), example_result)

        def test_uncastable_value_discarded(self):
                list_containing_bad_value = [1, -2, "trombone", 3, 1]
                example_result = 3
                self.assertEqual(
                        sum_of_list(list_containing_bad_value),
                        example_result
                )

