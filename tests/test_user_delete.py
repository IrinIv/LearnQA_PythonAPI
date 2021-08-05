from lib.base_case import BaseCase
from lib.assertions import Assertions
from lib.my_requests import MyRequests


class TestUserDelete(BaseCase):
    def test_delete_user_with_id_2(self):
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }

        response = MyRequests.post("/user/login", data=data)
        auth_sid = self.get_cookie(response, "auth_sid")
        token = self.get_header(response, "x-csrf-token")

        response1 = MyRequests.delete(f"/user/2",
                                      headers={"x-csrf-token": token},
                                      cookies={"auth_sid": auth_sid}
                                      )

        Assertions.assert_code_status(response1, 400)

    def test_delete_auth_user(self):
        register_data = self.prepare_registration_data()
        response = MyRequests.post("/user/", data=register_data)

        email = register_data['email']
        password = register_data['password']

        login_data = {
            'email': email,
            'password': password
        }

        response1 = MyRequests.post("/user/login", data=login_data)

        auth_sid = self.get_cookie(response1, "auth_sid")
        token = self.get_header(response1, "x-csrf-token")
        user_id_from_auth_method = self.get_json_value(response1, "user_id")

        response2 = MyRequests.delete(f"/user/{user_id_from_auth_method}",
                                      headers={"x-csrf-token": token},
                                      cookies={"auth_sid": auth_sid}
                                      )

        Assertions.assert_code_status(response2, 200)

        response3 = MyRequests.get(f"/user/{user_id_from_auth_method}")

        Assertions.assert_code_status(response3, 404)
        assert response3.text == "User not found"

    def test_delete_not_auth_user(self):
        register_data = self.prepare_registration_data()
        response = MyRequests.post("/user/", data=register_data)

        email = register_data['email']
        password = register_data['password']

        login_data = {
            'email': email,
            'password': password
        }

        response1 = MyRequests.post("/user/login", data=login_data)

        auth_sid = self.get_cookie(response1, "auth_sid")
        token = self.get_header(response1, "x-csrf-token")
        user_id = self.get_json_value(response1, "user_id")

        print(user_id)
        wrong_user_id = 6584

        response2 = MyRequests.delete(f"/user/{wrong_user_id}",
                                      headers={"x-csrf-token": token},
                                      cookies={"auth_sid": auth_sid}
                                      )


        response3 = MyRequests.get(f"/user/{wrong_user_id}")

        Assertions.assert_code_status(response3, 200)


