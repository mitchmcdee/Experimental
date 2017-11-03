import requests
import concurrent.futures
from bs4 import BeautifulSoup

def load_url(url, timeout):
    print("Scraping solutions from " + url)
    return requests.get(url, timeout = timeout)

base = 'https://wordbrain.org/'
puzzles = ['Ant', 'Spider', 'Snail', 'Crab', 'Frog', 'Turtle', 'Penguin',
          'Snake', 'Rat', 'Sheep', 'Shark', 'Cat', 'Elephant', 'Whale',
          'Octopus', 'Pig', 'Lion', 'Squirrel', 'Owl', 'Monkey', 'Student',
          'Clown', 'Waiter', 'Policeman', 'Chef', 'Teacher', 'Doctor',
          'Astronaut', 'Scientist', 'Alien', 'Dinosaur', 'Dragon', 'Monster',
          'Robot', 'Unicorn', 'Minotaur', 'Bigfoot', 'Yeti', 'Griffin',
          'Kraken', 'Mummy', 'Werewolf', 'Ghost', 'Zombie', 'Vampire',
          'Robot Zombie', 'Fairy', 'Martian', 'Cyborg', 'Mermaid']

# Ensure we have a unique set of words
words = set()
urls = []

# Loop over the given puzzles, adding their urls
for puzzle in puzzles:
    if puzzle not in ['Ant', 'Spider', 'Snail', 'Crab', 'Frog', 'Turtle']:
        for level in range(1, 21):
            url = base + puzzle + '/?table_filter=' + puzzle + '.' + str(level) + '..word'
            urls.append(url)
    else:
        url = base + puzzle
        urls.append(url)

print(urls)

with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
    future_to_url = {executor.submit(load_url, url, 100): url for url in urls}
    for future in concurrent.futures.as_completed(future_to_url):
        url = future_to_url[future]
        data = future.result()
        soup = BeautifulSoup(data.text, 'html.parser')
        puzzle = soup.title.text.split(' - ')[0]
        print('Adding words from', puzzle)

        if soup.tbody is None:
            upperRange = 21
            if puzzle in ['Ant', 'Spider']:
                upperRange = 11

            solutions = []
            for level in range(1, upperRange):
                solution = soup.find('strong', {'id': 'level-' + str(level)}).parent.text
                solutions.append(solution.split('\n')[-1])

        else:
            solutions = [a.text for a in soup.tbody.findAll('a')]

        [words.add(s.lower()) for s in solutions]

print("Writing to file")
# Write set to a file
with open('scrapedWords.txt','w') as f:
    f.write(('\n').join(sorted(words)))

print("Done!")