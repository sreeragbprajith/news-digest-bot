import requests
from bs4 import BeautifulSoup

def get_bbc_news():
    url = "https://www.bbc.com/news"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")

    articles = []

    for item in soup.select("h2")[:5]:
        title = item.get_text(strip=True)
        if title:
            articles.append({
                "title": title,
                "source": "BBC",
                "link": "https://www.bbc.com/news"
            })

    return articles


def get_toi_news():
    url = "https://timesofindia.indiatimes.com/home/headlines"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")

    articles = []

    for item in soup.select("span.w_tle a")[:5]:
        title = item.get_text(strip=True)
        link = "https://timesofindia.indiatimes.com" + item["href"]

        articles.append({
            "title": title,
            "source": "TOI",
            "link": link
        })

    return articles


def get_ht_news():
    url = "https://www.hindustantimes.com/india-news"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")

    articles = []

    for item in soup.select("h3 a")[:5]:
        title = item.get_text(strip=True)
        link = item["href"]

        articles.append({
            "title": title,
            "source": "Hindustan Times",
            "link": link
        })

    return articles


def get_all_news():
    return get_bbc_news() + get_toi_news() + get_ht_news()