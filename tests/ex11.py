import requests

def test_cookies():

    response = requests.get("https://playground.learnqa.ru/api/homework_cookie")
    actual_cookie_as_dict = response.cookies.get_dict()

    print(actual_cookie_as_dict)
    actual_cookie_value = actual_cookie_as_dict['HomeWork']
    expected_cookie_value = 'hw_value'
    print(actual_cookie_value)

    assert actual_cookie_value == expected_cookie_value, "The cookie doesn't exist in the response"