from PyPDF2 import PdfFileMerger
import requests
from io import BytesIO
from bs4 import BeautifulSoup

base = 'http://sites.math.rutgers.edu/~ajl213/CLRS/'
soup = BeautifulSoup(requests.get(base + 'CLRS.html').content, 'html.parser')
merger = PdfFileMerger()

for link in soup.find_all('a'):
    if link['href'][-3:] != 'pdf':
        continue

    url = base + link['href']
    r = requests.get(url)
    f = BytesIO(r.content)
    merger.append(f)
    print("Combined " + url)

merger.write(open("output.pdf", "wb"))
