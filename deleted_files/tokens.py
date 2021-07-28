import json
import requests
import time


def findSum(a, b):

    c = a + b

    payload = {'a': {a}, 'b': {b}}
    response = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params=payload)
    token = json.loads(response.text)['token']

    sum = a + c

    payload = {'token': token}
    response1 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params=payload)
    print(response1.json())

    time.sleep(10)

    payload = {'token': token}
    response2 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params=payload)
    print(response2.json())

    return sum


print(findSum(160755, 37459678))
