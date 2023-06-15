import unittest
from functions_with_errors import *
from functions import *


class TestStringMethods(unittest.TestCase):

    def test_greeting_name1(self):
        name = "Mykola"
        result = greeting_by_name1(name)
        self.assertEqual(f"Hello {name}!", result)

    def test_greeting_name2(self):
        name = "Alex"
        result = greeting_by_name2(name)
        self.assertEqual(f"Hello {name}!", result)

    #_______________________________________________
    def test_get_symbol_position1(self):
        text = "Hello"
        symbol = "o"
        result = get_symbol_position1(text, symbol)
        self.assertEqual(result, 5)

    def test_get_symbol_position2(self):
        text = "Hello"
        symbol = "o"
        result = get_symbol_position2(text, symbol)
        self.assertEqual(result, 5)

    #_________________________________________________
    def test_merge1(self):
        dict1 = {
            "name": "Alex",
            "age": 29,
            "email": "alexrozenberg@gmail.com"
        }
        dict2 = {
            "name": "Bob",
            "age": 60,
            "email": "has no email"
        }
        dict3 = dict1.copy()
        dict4 = dict2.copy()
        dict3.update(dict4)
        result = merge1(dict1, dict2)
        self.assertDictEqual(result, dict3)

    def test_merge2(self):
        dict1 = {
            "name": "Alex",
            "age": 29,
            "email": "alexrozenberg@gmail.com"
        }
        dict2 = {
            "name": "Bob",
            "age": 60,
            "email": "has no email"
        }
        dict3 = dict1.copy()
        dict4 = dict2.copy()
        merge2(dict1, dict2)
        self.assertDictEqual(dict1, dict3, 'dict1 immutability is FAILED')

    def test_merge3(self):
        dict1 = {
            "name": "Alex",
            "age": 29,
            "email": "alexrozenberg@gmail.com"
        }
        dict2 = {
            "name": "Bob",
            "age": 60,
            "email": "has no email"
        }
        dict3 = dict1.copy()
        dict4 = dict2.copy()
        merge2(dict1, dict2)
        self.assertDictEqual(dict2, dict4, 'dict2 immutability is FAILED')