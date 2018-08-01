import requests
from bs4 import BeautifulSoup
from yattag import Doc

with open('thesisSource.html', 'r') as f:
    source = f.read()

soup = BeautifulSoup(source, 'html5lib')
projects = soup.findAll('h3', {'class': 'projecttitle'})

doc, tag, text = Doc().tagtext()

for p in projects:
    projectTitle = p.text.split(' - ')[1].strip()

    projectTable = p.find_next_sibling('table')
    projectInfo = zip([h.text.strip() for h in projectTable.findAll('th')],
                      [d.text.strip() for d in projectTable.findAll('td')])
    
    with tag('hr'), tag('p'), tag('details'):
        with tag('summary'):
            text(projectTitle)      

        for header, info in projectInfo:
            if not header or not info:
                continue

            if header == 'Students signed up:' and info != '0':
                print(info, projectTitle)

            with tag('details'):
                with tag('summary'):
                    text(header)
                text(info)

with open('thesisOutput.html', 'w') as f:
    f.write(doc.getvalue())