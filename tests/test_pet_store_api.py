from requests import Response
from src.api import Petstore_api
from src.checking import Checking


class Test_add_pet():
    result_post: Response = Petstore_api.add_new_pet()
    check_post = result_post.json()
    pet_id = check_post["id"]

    def test_add_new_pet(self):
        print("Метод POST")
        Checking.check_status_code(self.result_post, 200)
        Checking.check_required_fields(self.result_post, ['id', 'category', 'name', 'photoUrls', 'tags', 'status'])

        print("Метод GET POST")
        result_get: Response = Petstore_api.get_new_pet(self.pet_id)
        check_get = result_get.json()
        Checking.check_status_code(result_get, 200)
        Checking.check_json_value(result_get, "name", "Charlie")
        Checking.check_json_value(result_get, "id", self.pet_id)

    def test_update_new_pet(self):
        print("Метод PUT")
        result_put: Response = Petstore_api.put_new_pet(self.pet_id)
        check_put = result_put.json()
        Checking.check_status_code(result_put, 200)
        Checking.check_required_fields(result_put, ['id', 'category', 'name', 'photoUrls', 'tags', 'status'])

        print("Метод GET PUT")
        result_get: Response = Petstore_api.get_new_pet(self.pet_id)
        check_get = result_get.json()
        Checking.check_status_code(result_get, 200)
        Checking.check_json_value(result_get, "name", "Garfield")
        Checking.check_json_value(result_get, "status", "pending")

    def test_delete_new_pet(self):
        print("Метод DELETE")
        result_delete: Response = Petstore_api.delete_new_pet(self.pet_id)
        check_delete = result_delete.json()
        Checking.check_status_code(result_delete, 200)
        # assert result_delete.status_code == 200
        # assert check_delete["type"] == "unknown"
    #
    #     print("Метод GET DELETE")
    #     result_get: Response = Petstore_api.get_new_pet(self.pet_id)
    #     check_get = result_get.json()
    #     assert result_get.status_code == 404
    #     assert check_get["code"] == 1
    #     assert check_get["message"] == "Pet not found"
