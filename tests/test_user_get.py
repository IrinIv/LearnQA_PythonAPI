from lib.base_case import BaseCase
from lib.assertions import Assertions
from lib.my_requests import MyRequests
import allure


@allure.epic("Test Cases to check GET method")
class TestUserGet(BaseCase):
    @allure.description("This test case verifies that not authorized user can only see the username")
    def test_get_user_details_not_auth(self):
        response = MyRequests.get("/user/2")
        Assertions.assert_json_has_key(response, "username")
        Assertions.assert_json_has_no_key(response, "email")
        Assertions.assert_json_has_no_key(response, "firstName")
        Assertions.assert_json_has_no_key(response, "lastName")

    @allure.description("This test case verifies that authorized user can see all required fields")
    def test_get_user_details_auth_as_same_user(self):
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }

        response1 = MyRequests.post("/user/login", data=data)

        auth_sid = self.get_cookie(response1, "auth_sid")
        token = self.get_header(response1, "x-csrf-token")
        user_id_from_auth_method = self.get_json_value(response1, "user_id")

        response2 = MyRequests.get(f"/user/{user_id_from_auth_method}",
                                   headers={"x-csrf-token": token},
                                   cookies={"auth_sid": auth_sid})

        expected_fields = ["username", "email", "firstName", "lastName"]

        Assertions.assert_json_has_keys(response2, expected_fields)

    @allure.description("This test case verifies that authorized user can see only username of another user")
    def test_get_user_details_auth_as_another_user(self):
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }

        response2 = MyRequests.post("/user/login", data=data)

        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")

        # new user was registered right before this test
        new_user_id = 6572

        response3 = MyRequests.get(f"/user/{new_user_id}",
                                   headers={"x-csrf-token": token},
                                   cookies={"auth_sid": auth_sid})

        Assertions.assert_code_status(response3, 200)
        Assertions.assert_json_has_key(response3, "username")
        Assertions.assert_json_has_no_key(response3, "email")
        Assertions.assert_json_has_no_key(response3, "firstName")
        Assertions.assert_json_has_no_key(response3, "lastName")
