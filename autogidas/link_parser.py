from URL_parser import get_url
from bs4 import BeautifulSoup
import json

def parse_ad_links():
    URL = 'https://autogidas.lt/skelbimai/automobiliai/?f_1[0]=&f_model_14[0]=&f_50=kaina_asc&page=1'
    base_url = 'https://autogidas.lt'
    page_url = '/automobiliai/?f_1[0]=&f_model_14[0]=&f_50=kaina_asc&page={page_number}'

    raw_html = get_url(URL)

    html = BeautifulSoup(raw_html, 'html.parser')

    last_page = int(html.select('.paginator a')[5].getText()) + 1

    links = []

    for page_number in range(1, last_page):
        url = base_url + page_url.format(**locals())

        titles = get_hrefs(url)

        for title in titles:
            links.append(title)

    return links

def get_hrefs(url):
    print(f'Parsing {url}')

    raw_html = get_url(url)

    html = BeautifulSoup(raw_html, 'html.parser')

    urls = []

    for item in html.select('a.item-link', href=True):
        urls.append(item['href'])

    return urls

