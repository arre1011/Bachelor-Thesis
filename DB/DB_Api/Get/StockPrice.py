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
    #print("#########" + date)
    end_date = date
    start_date = ""
    if '31' in end_date:
        start_date = date.replace('31', '01')
    elif '30' in end_date:
        start_date = date.replace('30', '01')
    # elif '29' in end_date:
    #     start_date = date.replace('29', '01')
    # elif '28' in end_date:
    #     start_date = date.replace('28', '01')
    # print("*********************" + start_date)

    historicalPrices = data.DataReader(tickers, start=start_date, end=end_date, data_source='yahoo')

    avarage = calculate_avarage_price_per(historicalPrices)

    return str(avarage)
