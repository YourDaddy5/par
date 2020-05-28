import requests
from bs4 import BeautifulSoup

URL = "https://drgn.gold"
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0','accept':'*/*'}

def get_html(url,params=None):
    r = requests.get(url)
    return r



def get_content(html):
    soup = BeautifulSoup(html,'html.parser')
    items = soup.find_all('span', class_='link-href domain')
    print(items)

def parce():
    html = get_html(URL)
    if html.status_code == 200:
        get_content(html.text)

    else:
        print('Error')


parce()

