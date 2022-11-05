from src.http_methods import Http_methods

base_url = "https://petstore.swagger.io/v2"


class Petstore_api():

    @staticmethod
    def add_new_pet():
        post_resource = "/pet"

        json_add_new_pet = {
            "name": "Charlie",
            "photoUrls": ["ullamco cupidatat enim cillum consectetur",
                          "exercitation aute magna deserunt"],
            "id": 71988172, "category": {"id": -75971216, "name": "dog"},
            "tags": [{"id": 60895543, "name": "dolor aliqua pariatur"},
                     {"id": -31720605, "name": "velit reprehe"}],
            "status": "available"
        }

        post_url = base_url + post_resource
        result_post = Http_methods.post(post_url, json_add_new_pet)
        return result_post

    @staticmethod
    def get_new_pet(pet_id):
        get_resource = f"/pet/{pet_id}"
        get_url = base_url + get_resource
        result_get = Http_methods.get(get_url)
        return result_get

    @staticmethod
    def put_new_pet(pet_id):
        put_resource = "/pet"

        json_update_existing_pet = {
            "name": "Garfield",
            "photoUrls": ["ullamco cupidatat enim cillum consectetur",
                          "exercitation aute magna deserunt"],
            "id": pet_id, "category": {"id": -75971216, "name": "cat"},
            "tags": [{"id": 60895543, "name": "dolor aliqua pariatur"},
                     {"id": -31720605, "name": "velit reprehe"}],
            "status": "available"
        }

        put_url = base_url + put_resource
        result_put = Http_methods.put(put_url, json_update_existing_pet)
        return result_put

    @staticmethod
    def delete_new_pet(pet_id):
        delete_resource = f"/pet/{pet_id}"
        delete_url = base_url + delete_resource
        result_delete = Http_methods.delete(delete_url)
        return result_delete
