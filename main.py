import json
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import time


def get_first_news():
    headers = {
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"
    }

    url = "https://doska.ykt.ru/avto/legkovye_avto/prodau?&region=yakutsk&minPrice=10+000&maxPrice=250+000"
    r = requests.get(url=url, headers=headers)

    soup = BeautifulSoup(r.text, "lxml")
    articles_cards = soup.find_all('div', class_='d-post d-post--auth', limit=25)

    news_dict = {}
    for article in articles_cards:
        article_title = article.find("div", class_="d-post_desc").text.strip()
        article_desc = article.find("div", class_="d-post_price").text.strip()
        article_url1 = article.find('a', class_='d-post_link').get("href")
        article_url = f'https://doska.ykt.ru{article_url1}'
        article_id = article_url.split("/")[-1]
        article_date = article.find("span", class_="d-post_date").text.strip()
        # print(f"{article_title} | {article_url} | {article_date_timestamp}")

        news_dict[article_id] = {
            "article_title": article_title,
            "article_url": article_url,
            "article_desc": article_desc,
            "article_date": article_date
        }

    with open("news_dict.json", "w") as file:
        json.dump(news_dict, file, indent=4, ensure_ascii=False)


def check_news_update():
    with open("news_dict.json") as file:
        news_dict = json.load(file)

    headers = {
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"
    }

    url = "https://doska.ykt.ru/avto/legkovye_avto/prodau?&region=yakutsk&minPrice=10+000&maxPrice=250+000"
    r = requests.get(url=url, headers=headers)

    soup = BeautifulSoup(r.text, "lxml")
    articles_cards = soup.find_all('div', class_='d-post d-post--auth')

    fresh_news = {}
    for article in articles_cards:

        article_url1 = article.find('a', class_='d-post_link').get("href")
        article_url = f'https://doska.ykt.ru{article_url1}'
        article_id = article_url.split("/")[-1]

        if article_id in news_dict:
            continue

        else:
            article_title = article.find("div", class_="d-post_desc").text.strip()
            article_desc = article.find("div", class_="d-post_price").text.strip()
            article_date = article.find("span", class_="d-post_date").text.strip()


            news_dict[article_id] = {
                "article_title": article_title,
                "article_url": article_url,
                "article_desc": article_desc,
                "article_date": article_date
            }

            fresh_news[article_id] = {
                "article_title": article_title,
                "article_url": article_url,
                "article_desc": article_desc,
                "article_date": article_date
            }

    with open("news_dict.json", "w") as file:
        json.dump(news_dict, file, indent=4, ensure_ascii=False)
asdasdasd
asdasdasd

    return fresh_news



def main():
    #get_first_news()
    #check_news_update()
    print(check_news_update())


if __name__ == '__main__':
    main()
