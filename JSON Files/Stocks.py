import pandas as pd
import os
stock_symbol = "CIPLA"
url = "https://www.nseindia.com/api/quote-equity?symbol=" + stock_symbol
print(url)
df = pd.read_json(r'D:\JSON Files\CIPLA.json')
print(df)
df.to_csv(r'D:\JSON Files\CIPLA.csv', index=False)
os.getcwd()
