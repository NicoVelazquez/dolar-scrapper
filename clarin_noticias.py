from bs4 import BeautifulSoup
import requests


def clarin_eco():
    try:
        news = []

        url = 'https://www.clarin.com/rss/economia/'
        r = requests.get(url)
        s = BeautifulSoup(r.text, "html.parser")

        items = s.findAll("item")

        for item in items:
            title = item.find("title").text
            description = item.find("description").text
            date = item.find("pubdate").text
            link = item.find("guid").text
            image = item.find("enclosure")['url']
            section = 'economía'

            news.append({'title': title, 'description': description, 'date': date, 'link': link,
                         'image': image, 'section': section})

        return news
    except Exception as e:
        print(e)


def clarin_pol():
    try:
        news = []

        url = 'https://www.clarin.com/rss/politica/'
        r = requests.get(url)
        s = BeautifulSoup(r.text, "html.parser")

        items = s.findAll("item")

        for item in items:
            title = item.find("title").text
            description = item.find("description").text
            date = item.find("pubdate").text
            link = item.find("guid").text
            image = item.find("enclosure")['url']
            section = 'politica'

            news.append({'title': title, 'description': description, 'date': date, 'link': link,
                         'image': image, 'section': section})

        return news
    except Exception as e:
        print(e)


if __name__ == "__main__":
    news = clarin_eco()
    print(news)

    x = requests.post('http://localhost:3000/news/add-economy', json=news)
    print(x)

    news = clarin_pol()
    print(news)

    x = requests.post('http://localhost:3000/news/add-politic', json=news)
    print(x)
