import requests


def test_headers():
    response = requests.get("https://playground.learnqa.ru/api/homework_header")
    actual_headers = response.headers.values()
    print(actual_headers)
    headers_name = 'x-secret-homework-header'
    actual_headers_hw_value = response.headers.get(headers_name)

    print(actual_headers_hw_value)
    expected_headers_value = 'Some secret value'

    assert actual_headers_hw_value == expected_headers_value, f"The headers with name '{headers_name}' does not exist in the response"



