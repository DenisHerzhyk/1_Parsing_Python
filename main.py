import requests

link = "https://browser-info.ru/"
response = requests.get(link)

with open('1.html','w', encoding='utf-8') as file:
    file.write(response.text)