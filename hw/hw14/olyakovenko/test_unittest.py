import unittest
# from functions import *
from functions_with_errors import *


class TestStringMethods(unittest.TestCase):

    """To run test cases you should uncomment import of necessary module"""

    def test_greeting_by_name(self):
        name = 'Alex'
        result = greeting_by_name(name)
        self.assertEqual(result, f"Hello {name}!")

    def test_get_symbol_position(self):
        text = 'Hello, World'
        symbol = 'o'
        result = get_symbol_position(text, symbol)
        self.assertEqual(result, 5, "When symbol is present in string")

    def test_get_symbol_position_incorrect_symbol_len(self):
        text = 'Hello, World'
        symbol = 'oo'
        result = get_symbol_position(text, symbol)
        self.assertEqual(result, "Error! Symbol can be string with only one letter", "When symbol is incorrect")

    def test_get_symbol_position_incorrect_symbol_negative(self):
        text = 'Hello, World'
        symbol = 'a'
        result = get_symbol_position(text, symbol)
        self.assertEqual(result, "Not found", "When symbol was not found")

    def test_merge(self):
        dict1 = {"model": "Volkswagen Amarok 2.0", "max_speed": 179}
        dict2 = {"model": "Toyota Camry", "max_speed": 163}
        dict3 = dict1.copy()
        dict4 = dict2.copy()
        dict3.update(dict4)
        result = merge(dict1, dict2)
        self.assertDictEqual(result, dict3)

    def test_merge_dict_1_immutability(self):
        dict1 = {"model": "Volkswagen Amarok 2.0", "max_speed": 179}
        dict2 = {"model": "Toyota Camry", "max_speed": 163}
        dict3 = dict1.copy()
        dict4 = dict2.copy()
        merge(dict1, dict2)
        self.assertDictEqual(dict1, dict3, 'dict1 immutability is Failed')


    def test_merge_dict_2_immutability(self):
        dict1 = {"model": "Volkswagen Amarok 2.0", "max_speed": 179}
        dict2 = {"model": "Toyota Camry", "max_speed": 163}
        dict3 = dict1.copy()
        dict4 = dict2.copy()
        merge(dict1, dict2)
        self.assertDictEqual(dict2, dict4, 'dict2 immutability is Failed')


if __name__ == '__main__':
    unittest.main()
