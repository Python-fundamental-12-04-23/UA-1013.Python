import unittest
from functions import greeting_by_name as greeting_by_name_correct
from functions import get_symbol_position as get_symbol_position_correct
from functions import merge as merge_correct
from functions_with_errors import greeting_by_name, get_symbol_position, merge


class TestFunctions(unittest.TestCase):

    def test_greeting_by_name(self):
        name = "Oleksandr"
        expected_output = "Hello Oleksandr!"
        self.assertEqual(greeting_by_name_correct(name), expected_output)

    def test_get_symbol_position_correct(self):
        text = "Hello world!"
        symbol = "o"
        expected_output = 5
        self.assertEqual(get_symbol_position_correct(text, symbol), expected_output)

    def test_get_symbol_position_incorrect(self):
        text = "Hello world!"
        symbol = "oo"
        expected_output = "Error! Symbol can be a string with only one letter"
        self.assertEqual(get_symbol_position(text, symbol), expected_output)

    def test_get_symbol_position_not_found(self):
        text = "Hello world!"
        symbol = "q"
        expected_output = "Not found"
        self.assertEqual(get_symbol_position(text, symbol), expected_output)

    def test_merge_correct(self):
        dict1 = {"a": 1, "b": 2}
        dict2 = {"c": 3, "d": 4}
        expected_output = {"a": 1, "b": 2, "c": 3, "d": 4}
        self.assertDictEqual(merge_correct(dict1, dict2), expected_output)

    def test_merge_dict_immu_correct(self):
        dict1 = {"a": 1, "b": 2}
        dict2 = {"c": 3, "d": 4}
        merge(dict1, dict2)
        self.assertDictEqual(dict1, {"a": 1, "b": 2})

    def test_merge_dict_immu_incorrect(self):
        dict1 = {"a": 1, "b": 2}
        dict2 = {"c": 3, "d": 4}
        merge(dict1, dict2)
        self.assertNotEqual(dict1, {"a": 1, "b": 2, "c": 3, "d": 4})

if __name__ == '__main__':
    unittest.main()
