import requests
from bs4 import BeautifulSoup

def scrape_titles(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    titles = [h2.text.strip() for h2 in soup.find_all('h2')]
    return titles

if __name__ == '__main__':
    url = 'https://news.ycombinator.com/'
    print(f"Scraping titles from {url} ...")
    titles = scrape_titles(url)
    for i, title in enumerate(titles[:10], 1):
        print(f"{i}. {title}")
