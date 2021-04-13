from bs4 import BeautifulSoup
import requests


# returns [{name, buy, sell}]
def dollar_cronista():
    try:
        quotes = []

        url = 'https://www.cronista.com/MercadosOnline/dolar.html'
        r = requests.get(url)
        s = BeautifulSoup(r.text, "html.parser")

        dollar_box = s.find("div", {"class": "block1"})
        quotes_boxes = dollar_box.findAll("li")

        for quote_box in quotes_boxes:
            name = quote_box.find("span", {"class": "name"}).text.strip()
            buy = quote_box.find("div", {"class": "buy-value"})
            if buy:
                buy = buy.text.strip().replace(",", ".")
            sell = quote_box.find("div", {"class": "sell-value"})
            if sell:
                sell = sell.text.strip().replace(",", ".")
            quotes.append({'name': name, 'buy': buy, 'sell': sell, 'source': 'El Cronista'})
        return quotes
    except Exception as e:
        print(e)


if __name__ == "__main__":
    quotes_dollars = dollar_cronista()
    print(quotes_dollars)

    x = requests.post('http://localhost:3000/dolar/update', json=quotes_dollars)
    print(x)
