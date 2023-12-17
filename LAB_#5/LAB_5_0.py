from pprint import pprint
import requests
import json

url = 'http://api.steampowered.com/ISteamNews/GetNewsForApp/v0002/'
payload ={
        'appid': '570',
        'count': '1',
        'lengght': 300,
        'format': 'json'
        }

response = requests.get(url, payload)


result = json.loads(response.text)
print(result)
res = result['appnews']['newsitems']

News = {
        'title': res[0]['title'],
        'url_news': res[0]['url'],
        'news_contents': res[0]['contents']
        }
pprint(News,  sort_dicts=False)