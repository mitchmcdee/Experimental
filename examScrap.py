import requests
import concurrent.futures

def load_url(url, timeout):
    return requests.get(url, timeout = timeout)

base = 'https://my.uq.edu.au/files/'
urls = [base + str(i) + '/.pdf' for i in range(50000)]

print('starting')
with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
    future_to_url = {executor.submit(load_url, url, 1000): url for url in urls}
    for future in concurrent.futures.as_completed(future_to_url):
        url = future_to_url[future]
        r = future.result()
        if r.headers['Content-Type'] == 'application/pdf':
            print(url)