from lib.base_case import BaseCase
from lib.assertions import Assertions
from lib.my_requests import MyRequests
import allure


@allure.epic("Test Cases to check PUT method")
class TestUserEdit(BaseCase):
    @allure.description("This test case show the whole workflow from register user to check user's details")
    @allure.step("Step #1 - Register user, #2 - Login, #3 - Edit details, #4 - Get user's info")
    def test_edit_just_created_user(self):
        # REGISTER
        register_data = self.prepare_registration_data()
        response1 = MyRequests.post("/user/", data=register_data)

        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        email = register_data['email']
        first_name = register_data['firstName']
        password = register_data['password']
        user_id = self.get_json_value(response1, "id")

        # LOGIN
        login_data = {
            'email': email,
            'password': password
        }

        response2 = MyRequests.post("/user/login", data=login_data)

        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")

        # EDIT
        new_name = "Changed name"
        response3 = MyRequests.put(f"/user/{user_id}",
                                   headers={"x-csrf-token": token},
                                   cookies={"auth_sid": auth_sid},
                                   data={"firstName": new_name}
                                   )

        Assertions.assert_code_status(response3, 200)

        # GET
        response4 = MyRequests.get(f"/user/{user_id}",
                                   headers={"x-csrf-token": token},
                                   cookies={"auth_sid": auth_sid}
                                   )

        Assertions.assert_json_value_by_name(
            response4,
            "firstName",
            new_name,
            "Wrong name of the user after edited")

    @allure.description("This test case verifies that not authorized user can not edit info of another user")
    def test_edit_not_authorized_user(self):
        new_name = "Changed name"

        response = MyRequests.put(f"/user/6572", data={"firstName": new_name})

        Assertions.assert_code_status(response, 400)

    @allure.description("This test case verifies that authorized user can not edit info of another user")
    def test_edit_user_details_auth_as_another_user(self):
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }

        response = MyRequests.post("/user/login", data=data)

        auth_sid = self.get_cookie(response, "auth_sid")
        token = self.get_header(response, "x-csrf-token")

        # new user was registered right before this test
        new_user_id = 6598

        new_name = "Changed name"
        response1 = MyRequests.put(f"/user/{new_user_id}",
                                   headers={"x-csrf-token": token},
                                   cookies={"auth_sid": auth_sid},
                                   data={"firstName": new_name}
                                   )

        Assertions.assert_code_status(response1, 400)

    @allure.description("This test case verifies that authorized user can not edit own email address with wrong format")
    def test_edit_wrong_email_format(self):
        register_data = self.prepare_registration_data()
        response = MyRequests.post("/user/", data=register_data)

        email = register_data['email']
        password = register_data['password']

        login_data = {
            'email': email,
            'password': password
        }

        response = MyRequests.post("/user/login", data=login_data)

        auth_sid = self.get_cookie(response, "auth_sid")
        token = self.get_header(response, "x-csrf-token")

        new_email = email.replace("@", "")

        response1 = MyRequests.put(f"/user/login",
                                   headers={"x-csrf-token": token},
                                   cookies={"auth_sid": auth_sid},
                                   data={"email": new_email}
                                   )

        Assertions.assert_code_status(response1, 400)
        assert response1.text == "Wrong HTTP method"

    @allure.description("This test case verifies that authorized user can not edit own name if it's has only 1 "
                        "character")
    def test_edit_user_with_short_firstName(self):
        register_data = self.prepare_registration_data()
        response = MyRequests.post("/user/", data=register_data)

        email = register_data['email']
        password = register_data['password']

        login_data = {
            'email': email,
            'password': password
        }

        response = MyRequests.post("/user/login", data=login_data)

        auth_sid = self.get_cookie(response, "auth_sid")
        token = self.get_header(response, "x-csrf-token")

        new_firstName = 'l'

        response1 = MyRequests.put(f"/user/login",
                                   headers={"x-csrf-token": token},
                                   cookies={"auth_sid": auth_sid},
                                   data={"firstName": new_firstName}
                                   )

        Assertions.assert_code_status(response1, 400)
        assert response1.text == "Wrong HTTP method"
