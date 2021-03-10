import pandas as pd
from pandas_datareader import data

def calculate_avarage_price_per(df):
    counter = 0.0
    df_length = df.shape[0]
    i = 0
    while i < df_length:
        counter += float(df.iat[i, 3])
        i += 1
    avarage = counter / df_length

    return avarage


def get_stock_price(symbole, date):
    tickers = symbole
    end_date = date
    start_date = date.replace('30', '01')
    historicalPrices = data.DataReader(tickers, start=start_date, end=end_date, data_source='yahoo')

    avarage = calculate_avarage_price_per(historicalPrices)

    return str(avarage)
    #
    # print("avarage:" + str(avarage))
    # print(historicalPrices.iat[0, 3])
    # print(historicalPrices.iat[1, 3])
    # return result
