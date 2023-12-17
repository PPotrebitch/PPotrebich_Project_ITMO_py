import requests
import json
import webbrowser

My_key = "iOvaXlO978Sa4EmFnAfZuCeohbnWWLZHzXZLmsXr"
url = f'https://api.nasa.gov/planetary/apod?api_key={My_key}'
response = requests.get(url)
result = json.loads(response.text)
# print(result)

img = result["hdurl"]
print(img)
webbrowser.open(f'{img}', new=2)

