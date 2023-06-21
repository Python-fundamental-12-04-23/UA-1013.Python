import unittest
from lesson14 import read_user_json
import HtmlTestRunner


class Testlesson(unittest.TestCase):

    def setUp(self):
        print("\tsetUp")

    def tearDown(self) -> None:
        print("\ttearDown")

    @classmethod
    def setUpClass(cls) -> None:
        print("setUpClass")

    @classmethod
    def tearDownClass(cls) -> None:
        print("\t\tTest")
        print("tearDownClass")

    def test_read_user_json_file_fiil(self):
        actual = read_user_json("test")
        self.assertIsNone(actual)

    def test_read_user_json(self):
        print("\t\tTest")
        actual = read_user_json("data/user.json")
        expected = {
            'age': 33,
            'children': [{'age': 3, 'firstName': 'Vira'},
                         {'age': 5, 'firstName': 'Maksym'}],
            'firstName': 'Ivan',
            'hobbies': ['reading', 'traveling', 'singing'],
            'lastName': 'King'
        }
        self.assertEqual(actual.get("age"), 33)
        self.assertIs(type(actual.get("age")), int)
        self.assertDictEqual(actual, expected)

    def test_read_user_json_error(self):
        print("\t\tTest")
        actual = read_user_json("data/user.json")
        expected = {
            'age': 33,
            'children': [{'age': 3, 'firstName': 'Vira'},
                         {'age': 5, 'firstName': 'Maksym'}],
            'firstName': 'Ivan',
            'hobbies': ['reading', 'traveling', 'singing'],
            'lastName': 'King'
        }
        self.assertDictEqual(actual, expected)


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner())
