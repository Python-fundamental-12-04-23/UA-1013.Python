import requests
import json
from requests import Response


class HttpMethods:
    headers = {'Content-Type': 'application/json'}
    cookie = ""

    @staticmethod
    def get(url, body):
        result = requests.post(url, json=body, headers=HttpMethods.headers, cookies=HttpMethods.cookie)
        return result


class NpApi:

    @staticmethod
    def get_information_from_np(key_val, cur_date, base_url):
        json_for_getting_information = {
                "apiKey": key_val,
                "modelName": "InternetDocument",
                "calledMethod": "getDocumentList",
                "methodProperties": {
                    "DateTimeFrom": cur_date,
                    "DateTimeTo": cur_date,
                    "Page": "1",
                    "GetFullList": "1",
                    "DateTime": cur_date
                }
        }
        result_get = HttpMethods.get(base_url, json_for_getting_information)
        print(result_get.text)
        return result_get


class Checking:

    """Method for check status code"""
    @staticmethod
    def check_status_code(response: Response, status_code):
        assert status_code == response.status_code
        if response.status_code == status_code:
            print('Successfully! Status code = ' + str(response.status_code))
        else:
            print('Fail! Status code != ' + str(response.status_code))


    """Method from checking if field exists"""
    @staticmethod
    def check_json_token(response: Response, expected_value):
        token = json.loads(response.text)
        assert list(token) == expected_value
        print('All fields exist')

    """Method for checking values of response fields"""
    @staticmethod
    def check_json_value(response: Response, field_name, expected_value):
        check = response.json()
        check_info = check.get(field_name)
        assert check_info == expected_value
        print(field_name + ' PASS, all field values correct')



