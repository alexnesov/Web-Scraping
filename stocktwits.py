import pandas as pd
import requests
from bs4 import BeautifulSoup
import re


csvfile = pd.read_csv('Stock_indices_NASDAQ.csv')
listOfStocks = csvfile["Symbol"]

listOfStocks_A = listOfStocks[0:5]
listOfStocks_B = listOfStocks[21:41]

# Initiating the dictionnary with it's column names (stock's ticker)
dict_stocks = {}
dict_stocks['Symbol'] = []
dict_stocks['Watchers'] = []

def find_n_watchers():
    for stock in listOfStocks_A:
        print(f"Sending a HTTP request to CNN for {stock}. . .")
        try:
            request = requests.get(f"https://stocktwits.com/symbol/{stock}")
            print(f'{stock} found!')
            content = request.content
            soup = BeautifulSoup(content, "html.parser")
            elem = soup.find("div", class_='st_HebiDD2 st_yCtClNI st_2mehCkH st_3PPn_WF')
            elem = str(elem)
            string_start = "><strong>"
            string_end = "</strong><br/>Watchers"
            n_watchers = re.search('%s(.*)%s' % (string_start, string_end), elem).group(1).replace(",",".")
            dict_stocks['Symbol'].append(stock)
            dict_stocks['Watchers'].append(n_watchers)
        except:
            print(f"Issue encountered with: {stock}")



if __name__ == "__main__":
    find_n_watchers()
    DFWatchers = pd.DataFrame.from_dict(dict_stocks)






