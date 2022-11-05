import requests

class Http_methods:

    @staticmethod
    def get(url):
        result = requests.get(url)
        return result

    @staticmethod
    def post(url, body):
        result = requests.post(url, json=body)
        return result

    @staticmethod
    def put(url, body):
        result = requests.put(url, json=body)
        return result

    @staticmethod
    def delete(url):
        result = requests.delete(url)
        return result
