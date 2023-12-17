from pprint import pprint
import requests
import json

city_name = 'Moscow'
key = 'a66263d7fd194a0cdb3c05924cdaf9e3'
lang = 'ru'
response = requests.post(f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&lang={lang}&units=metric&appid={key}')
result = json.loads(response.text)
print(result)
Box = {'City_name: ': city_name,
       'temp = ': result['main']['temp'],
       'pressure = ': result['main']['pressure'],
       'humidity = ': result['main']['humidity']}
pprint(Box, sort_dicts=False)

