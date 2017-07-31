import grequests
import requests
from bs4 import BeautifulSoup

# root url format
root = 'https://cdn.hackerrank.com/hackerrank/static/contests/capture-the-flag/infinite/'

# first page
visited = set('qds.html')
stack = [requests.get(root + 'qds.html').text]

phrases = []
while len(stack) != 0:
    html = stack.pop()
    soup = BeautifulSoup(html, 'html.parser')

    # get phrase
    if soup.font:
        phrase = soup.font.contents[1]
        phrases.append(phrase)
        print(phrase)

    # get more links
    links = []
    for link in soup.find_all('a'):
        link = link.get('href')

        if link in visited:
            continue

        visited.add(link)
        links.append(grequests.get(root + link))
        print(link)

    # add all links responses to stack
    [stack.append(link.text) for link in grequests.map(links)]

[print(phrase) for phrase in sorted(phrases)]