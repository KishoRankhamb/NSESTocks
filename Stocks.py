import pandas as pd
import os
from bs4 import BeautifulSoup
import warnings
warnings.filterwarnings('ignore')
stock_symbol = "TCS"
url = "https://www.nseindia.com/api/quote-equity?symbol=" + stock_symbol
print(url)
soup = BeautifulSoup(url, "html.parser")
print(soup)
df = pd.read_json(r'C:\Users\Administrator\PycharmProjects\Stock\TCS.json')
print(df)
df.to_csv(r"C:\Users\Administrator\PycharmProjects\Stock\TCS.csv", index=False)
os.getcwd()
