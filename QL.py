import time
import requests

now = round(time.time())
two_days_ago = round(now - 172800)

URL = "https://api.stackexchange.com/2.2/questions"

response = requests.get(URL, params={"fromdate": two_days_ago, "todate": now, "order": "desc", "sort": "creation", "tagged": "python", "site": "stackoverflow"})
ids = ''
resp = response.json()
items = resp['items']
for item in items:
    title = item['title']
    link = item['link']
    print(f'Вопрос: {title}\nСсылка на вопрос: {link}\n')
