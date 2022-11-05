from requests import Response
from src.checking import Checking
from src.api import Petstore_api


class Test_add_pet():
    result_post: Response = Petstore_api.add_new_pet()
    check_post = result_post.json()
    pet_id = check_post["id"]

    def test_add_new_pet(self):
        print("Метод POST")
        # assert self.result_post.status_code == 200
        Checking.check_status_code(self.result_post, 200)
        assert self.check_post["name"] == "Charlie"

        print("Метод GET POST")
        result_get: Response = Petstore_api.get_new_pet(self.pet_id)
        print(result_get)
        result_get_1 = Petstore_api.get_new_pet(self.pet_id)
        print(result_get_1)

        check_get = result_get.json()
        assert result_get.status_code == 200
        assert check_get["id"] == self.pet_id

    def test_update_new_pet(self):
        print("Метод PUT")
        result_put: Response = Petstore_api.put_new_pet(self.pet_id)
        check_put = result_put.json()
        assert result_put.status_code == 200
        assert check_put["name"] == "Garfield"
        assert check_put["category"]["name"] == "cat"

        print("Метод GET PUT")
        result_get: Response = Petstore_api.get_new_pet(self.pet_id)
        check_get = result_get.json()
        assert result_get.status_code == 200
        assert check_get["name"] == check_put["name"]
        assert check_get["category"]["name"] == check_put["category"]["name"]

    def test_delete_new_pet(self):
        print("Метод DELETE")
        result_delete: Response = Petstore_api.delete_new_pet(self.pet_id)
        check_delete = result_delete.json()
        assert result_delete.status_code == 200
        assert check_delete["type"] == "unknown"

        print("Метод GET DELETE")
        result_get: Response = Petstore_api.get_new_pet(self.pet_id)
        check_get = result_get.json()
        assert result_get.status_code == 404
        assert check_get["code"] == 1
        assert check_get["message"] == "Pet not found"
