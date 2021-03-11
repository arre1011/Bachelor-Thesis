import pandas as pd
from pandas_datareader import data

tickers = 'AMZN'
end_date = '2011-12-31'
start_date = end_date.replace('30', '01')
start_date = end_date.replace('31', '01')
print("##########################"+start_date)
historicalPrices = data.DataReader(tickers, start=start_date, end=end_date, data_source='yahoo')

print