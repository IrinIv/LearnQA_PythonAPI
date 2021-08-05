import pytest

from lib.base_case import BaseCase
from lib.assertions import Assertions
from lib.my_requests import MyRequests


class TestUserRegister(BaseCase):
    fields = [
        {'required': 'password', 'username': 'learnqa', 'firstName': 'learnqa', 'lastName': 'learnqa', 'email': 'vinkotov@example.com'},
        {'required': 'username', 'password': '123', 'firstName': 'learnqa', 'lastName': 'learnqa', 'email': 'vinkotov@example.com'},
        {'required': 'firstName', 'password': '123', 'username': 'learnqa', 'lastName': 'learnqa', 'email': 'vinkotov@example.com'},
        {'required': 'lastName', 'password': '123', 'username': 'learnqa', 'firstName': 'learnqa', 'email': 'vinkotov@example.com'},
        {'required': 'email', 'password': '123', 'username': 'learnqa', 'firstName': 'learnqa', 'lastName': 'learnqa'}

    ]

    def test_create_user_successfully(self):
        data = self.prepare_registration_data()

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_has_key(response, "id")

    def test_create_user_with_existing_email(self):
        email = 'vinkotov@example.com'
        data = self.prepare_registration_data(email)

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode('utf-8') == f"Users with email '{email}' already exists", \
            f"Unexpected content {response.content}"

    def test_create_user_with_wrong_email_format(self):
        email = 'vinkotovexample.com'
        data = self.prepare_registration_data(email)

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.text == "Invalid email format"

    @pytest.mark.parametrize("field", fields)
    def test_create_user_without_any_field(self, field):

        data = field
        response = MyRequests.post("/user/", data=data)

        print(response.text)

        Assertions.assert_code_status(response, 400)
        assert response.text == f"The following required params are missed: {field['required']}"


    def test_create_user_with_short_firstName(self):
        email = 'vinkotov@example.com'
        firstName = 'l'
        data = self.data_with_short_name(email, firstName)

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.text == f"The value of '{'firstName'}' field is too short"

    def test_create_user_with_long_firstName(self):
        email = 'vinkotov@example.com'
        firstName = 'lhfhdjskalwertyuioqpwerfhdksncvbmfdhfjdksdjdjfjfjfjfjfjeyrirgfldhsnchrmcndbcbdbcbcbcbcbcbcbbcbbcbc' \
                    'sjdhajjjasjkakjdskjhhksjhdjhdjhdasjdhksjhjsdjksakjakjshdaksjdhaskdjhaskjdhaksjdhaksjdhaskjdhaksjdhakjdh' \
                    'ajsdkjadsjkahdkajhdashdakjshdakhdakhdakhdakshdaksdkajhdakjshdkajshdkajshdkjashdakjhdakjhdaskjhdaksjhasdj' \
                    'asdahsdjhasdjhaskjdhaksdhaskjdhaksdhakdhakhdakshdakhdaskhdakdakdaldladalsdalskdalkdalkdaldasldkalsdal' \
                    'sdaksjdkasjdakjdaksjd'

        data = self.data_with_short_name(email, firstName)

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.text == f"The value of '{'firstName'}' field is too long"

# python3 -m pytest -s tests/test_user_register.py -k test_create_user_successfully
