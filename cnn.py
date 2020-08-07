import pandas as pd
import requests
from bs4 import BeautifulSoup

csvfile = pd.read_csv('Stock_indices_NASDAQ.csv')
listOfStocks = csvfile["Symbol"]

listOfStocks_A = listOfStocks[0:5]
listOfStocks_B = listOfStocks[21:41]

# Initiating the dictionnary with it's column names (stock's ticker)
dict_stocks = {}
dict_stocks.fromkeys(listOfStocks, None)

def find_competitors():
    for stock in listOfStocks_A:
        print(f"Sending a HTTP request to CNN for {stock}. . .")
        try:
            print(f'{stock} found!')
            request = requests.get(f"https://money.cnn.com/quote/competitors/competitors.html?symb={stock}")
            content = request.content
            soup = BeautifulSoup(content, "html.parser")
            bundle = soup.find_all("a", class_='wsod_symbol')

            string_start = '">'
            string_end = '</a>'

            symbols = []
            for i in bundle[3:]:
                i = str(i)
                symb = i[i.find(string_start)+len(string_start):i.rfind(string_end)]
                symbols.append(symb)
                dict_stocks[stock] = symbols
        except:
            print(f"Issue encountered with: {stock}")



if __name__ == "__main__":
    # set_server_connection(listOfStocks_B)
    # We choose "orient" as an argument otherwise we get a ValueError telling us that "array must be same length"
    find_competitors()
    CompetitorsDF = pd.DataFrame.from_dict(dict_stocks, orient="Index")



