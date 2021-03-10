import yahoo_fin.stock_info as si
import pandas as pd
import pprint

quote = si.get_quote_table("aapl")

quote["PE Ratio (TTM)"]

val = si.get_stats_valuation("aapl")

val = val.iloc[:,:2]

val.columns = ["Attribute", "Recent"]

val = float(val[val.Attribute.str.contains("Trailing P/E")].iloc[0,1])

pprint.pprint(quote)

