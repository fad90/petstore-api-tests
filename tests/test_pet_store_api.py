from src.api import Petstore_api
from src.checking import Checking
import allure

@allure.epic("Test create pet")
class Test_add_pet():
    result_post = Petstore_api.add_new_pet()
    check_post = result_post.json()
    pet_id = check_post["id"]

    @allure.description("Test add pet")
    def test_add_new_pet(self):
        print("Метод POST")
        Checking.check_status_code(self.result_post, 200)
        Checking.check_required_fields(self.result_post, ['id', 'category', 'name', 'photoUrls', 'tags', 'status'])

        print("Метод GET POST")
        result_get = Petstore_api.get_new_pet(self.pet_id)
        Checking.check_status_code(result_get, 200)
        Checking.check_json_value(result_get, "name", "Charlie")
        Checking.check_json_value(result_get, "id", self.pet_id)

    @allure.description("Test update pet")
    def test_update_new_pet(self):
        print("Метод PUT")
        result_put = Petstore_api.put_new_pet(self.pet_id)
        Checking.check_status_code(result_put, 200)
        Checking.check_required_fields(result_put, ['id', 'category', 'name', 'photoUrls', 'tags', 'status'])

        print("Метод GET PUT")
        result_get = Petstore_api.get_new_pet(self.pet_id)
        Checking.check_status_code(result_get, 200)
        Checking.check_json_value(result_get, "name", "Garfield")
        Checking.check_json_value(result_get, "status", "pending")

    @allure.description("Test delete pet")
    def test_delete_new_pet(self):
        print("Метод DELETE")
        result_delete = Petstore_api.delete_new_pet(self.pet_id)
        Checking.check_status_code(result_delete, 200)
        Checking.check_required_fields(result_delete, ["code", "type", "message"])

        print("Метод GET DELETE")
        result_get = Petstore_api.get_new_pet(self.pet_id)
        Checking.check_status_code(result_get, 404)
        Checking.check_json_value(result_get, "code", 1)
        Checking.check_json_value(result_get, "message", "Pet not found")
