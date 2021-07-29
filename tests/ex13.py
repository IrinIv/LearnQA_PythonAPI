import pytest
import requests


# @pytest.mark.parametrize('device', 'browser', 'platform')
def test_user_agent():
    response = requests.get("https://playground.learnqa.ru/ajax/api/user_agent_check",
                            headers={
                                "User-Agent": "Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) "
                                              "AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30"})

    print(response.text)

    user_agent_platform = 'platform'
    actual_platform_value = response.json().get(user_agent_platform)
    print(actual_platform_value)
    expected_platform_value = 'Mobile'

    user_agent_browser = 'browser'
    actual_browser_value = response.json().get(user_agent_browser)
    print(actual_browser_value)
    expected_browser_value = 'No'

    user_agent_device = 'device'
    actual_device_value = response.json().get(user_agent_device)
    print(actual_device_value)
    expected_device_value = 'Android'

    assert actual_platform_value == expected_platform_value, "The platform value is not correct"
    assert actual_browser_value == expected_browser_value, "The browser value is not correct"
    assert actual_device_value == expected_device_value, "The device value is not correct"


