import grequests
import requests

root = 'https://cdn.hackerrank.com/hackerrank/static/contests/capture-the-flag/secret/'

keys = requests.get(root + 'key.json').json().keys()
requests = [grequests.get(root + 'secret_json/' + key + '.json') for key in keys]
secrets = [dict(response.json())['news_title'] for response in grequests.map(requests)]
[print(secret) for secret in sorted(secrets)]