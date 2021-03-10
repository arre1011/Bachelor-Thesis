# import datetime
# import pandas as pd
# from pandas_datareader import data
#
#
# shares = 17528000000
#
# netIncome = "57411000000.00"
#
# dividendsPaid = "-14119000000.00"
#
# sharePrice = 115
#
# ebit = "69964000000"
#
# maketCap = shares * sharePrice
#
# print(maketCap)
#
# earnings = float(netIncome) + float(dividendsPaid)
#
# print(earnings)
#
# pricePerErnings = maketCap/earnings
#
#
# print(pricePerErnings)
#
# earningsPerShare = earnings/shares
#
# print(earningsPerShare)

totalAssets = 323888000000

totalLiab = 258549000000

shares = 17528000000

sharePrice = 115

BookValue = (totalAssets - totalLiab) / shares

print(BookValue)

BookRatioPerShahre = sharePrice / BookValue

print(BookRatioPerShahre)

