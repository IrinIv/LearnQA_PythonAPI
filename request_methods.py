import requests

#1. Делает http-запрос любого типа без параметра method
print("#1:")
response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type")
print(response.text + "\n")


#2. Делает http-запрос не из списка. Например, HEAD
print("#2:")
response = requests.head("https://playground.learnqa.ru/ajax/api/compare_query_type", data={'method': 'HEAD'})
print(response.text)
print(response.status_code)
print("\n")

#3. Делает запрос с правильным значением method
print("#3:")
response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params={'method': 'GET'})
print(response.text + "\n")

#4. С помощью цикла проверяет все возможные сочетания реальных типов запроса и значений параметра method.
print("#4:")
request_methods = ["POST", 'GET', 'PUT', 'DELETE']

for i in range(len(request_methods)):
     if request_methods[i] == "POST":
         for index in range(len(request_methods)):
            response = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data={'method': {request_methods[index]}})
            print(response.text + "\n")

     elif request_methods[i] == 'GET':
         for index in range(len(request_methods)):
            response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params={'method': {request_methods[index]}})
            print(response.text + "\n")

     elif request_methods[i] == 'PUT':
         for index in range(len(request_methods)):
            response = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", data={'method': {request_methods[index]}})
            print(response.text + "\n")

     elif request_methods[i] == 'DELETE':
         for index in range(len(request_methods)):
            response = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type", data={'method': {request_methods[index]}})
            print(response.text + "\n")

