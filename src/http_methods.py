import requests
import allure

class Http_methods:

    @staticmethod
    def get(url):
        with allure.step("GET"):
            result = requests.get(url)
            return result

    @staticmethod
    def post(url, body):
        with allure.step("POST"):
            result = requests.post(url, json=body)
            return result

    @staticmethod
    def put(url, body):
        with allure.step("PUT"):
            result = requests.put(url, json=body)
            return result

    @staticmethod
    def delete(url):
        with allure.step("DELETE"):
            result = requests.delete(url)
            return result
