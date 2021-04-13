from bs4 import BeautifulSoup
import requests


# returns [{name, buy, sell}]
def dolar_hoy():
    try:
        quotes = []

        url = 'https://www.dolarhoy.com/'
        r = requests.get(url)
        s = BeautifulSoup(r.text, "html.parser")

        dolar_box = s.find("div", {"class": "tile dolar"})
        quotes_boxes = dolar_box.findAll("div", {"class": "tile is-child"})
        for quote_box in quotes_boxes:
            name = quote_box.find("a").text.strip()
            buy = quote_box.find("div", {"class": "compra"}).find("div", {"class": "val"})
            if buy:
                buy = buy.text.strip()[1:]
            sell = quote_box.find("div", {"class": "venta"}).find("div", {"class": "val"})
            if sell:
                sell = sell.text.strip()[1:]
            quotes.append({'name': name, 'buy': buy, 'sell': sell, 'source': 'Dólar Hoy'})
        return quotes
    except Exception as e:
        print(e)


if __name__ == "__main__":
    quotes_dolar_hoy = dolar_hoy()
    print(quotes_dolar_hoy)

    x = requests.post('http://localhost:3000/dolar/update', json=quotes_dolar_hoy)
    print(x.status_code)
    print(x.content)
