import json

import pytest
import requests


class TestUserAgent:
    user_agents = [
        {'User-Agent': "Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 ("
                       "KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
         'platform': 'Mobile', 'browser': 'No', 'device': 'Android'},
        {'User-Agent': "Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) "
                       "CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1",
         'platform': 'Mobile', 'browser': 'Chrome', 'device': 'iOS'},
        {'User-Agent': "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
         'platform': 'Googlebot', 'browser': 'Unknown', 'device': 'Unknown'},
        {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                       "Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0",
         'platform': 'Web', 'browser': 'Chrome', 'device': 'No'},
        {'User-Agent': "Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, "
                       "like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1",
         'platform': 'Mobile', 'browser': 'No', 'device': 'iPhone'},

    ]

    @pytest.mark.parametrize("user_agent", user_agents)
    def test_user_agent(self, user_agent):
        url = "https://playground.learnqa.ru/ajax/api/user_agent_check"
        data = user_agent
        response = requests.get(url, headers=data)

        response_dict = response.json()
        print(response_dict)

        expected_platform_value = user_agent['platform']
        print(expected_platform_value)
        expected_browser_value = user_agent['browser']
        print(expected_browser_value)
        expected_device_value = user_agent['device']
        print(expected_device_value)

        actual_platform_value = response_dict["platform"]
        print(actual_platform_value)
        actual_browser_value = response_dict["browser"]
        print(actual_browser_value)
        actual_device_value = response_dict["device"]
        print(actual_device_value)

        assert actual_platform_value == expected_platform_value
        assert actual_browser_value == expected_browser_value
        assert actual_device_value == expected_device_value

# python3 -m pytest -s tests/ex13.py
