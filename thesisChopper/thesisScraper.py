import requests
from bs4 import BeautifulSoup
from yattag import Doc

with open('thesisSource.html', 'r') as f:
    source = f.read()

soup = BeautifulSoup(source, 'html5lib')
projects = soup.findAll('h3', {'class': 'projecttitle'})

doc, tag, text = Doc().tagtext()

for p in projects:
    projectTitle = p.text.split(' - ')[1]
    projectTable = p.find_next_sibling('table')
    projectInfo = zip([h.text.strip() for h in projectTable.findAll('th')],
                      [d.text.strip() for d in projectTable.findAll('td')])
    
    with tag('hr'):
        with tag('p'):
            with tag('details'):
                with tag('summary'):
                    text(projectTitle)      

                for header, info in projectInfo:
                    if not header or not info:
                        continue    

                    with tag('details'):
                        with tag('summary'):
                            text(header)
                        text(info)

with open('thesisOutput.html', 'w') as f:
    f.write(doc.getvalue())