import pandas as pd
from Stocks.Stock import Stock
from Stocks import Helper_functions
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
from sklearn.preprocessing import StandardScaler
import statsmodels.api as sm


#
#
# tickerList = [ 'NVDA']
#
# quartilList = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
#
# # Lists of Ratios
#
# KGVList = []
# pricePerShare = []
# pricePerBook = []
# capitalExpenditures = []
# returnOnInvestment = []
# totalLiabilities = []
# bookValuePerShare = []
# dateColumn = []
#
#
# data = []
# for ticker in tickerList:
#     dateList = Helper_functions.get_list_of_dates(ticker)
#     i = 0
#     while i < len(dateList):
#         Stock1 = Stock(ticker, dateList[i], quartilList[i])
#
#         KGVList.append(str(Stock1.pricePerEarnings))
#         pricePerShare.append(str(Stock1.stockPrice))
#         pricePerBook.append(str(Stock1.pricePerBookRatioPerShare))
#         capitalExpenditures.append(Stock1.capitalExpenditures)
#         returnOnInvestment.append(Stock1.returnOnInvestment)
#         totalLiabilities.append(str(Stock1.totalLiabilities))
#         bookValuePerShare.append(str(Stock1.bookValuePerShare))
#         dateColumn.append(dateList[i])
#         i += 1
#
# ColumnKGV = tickerList[0] + " KGV"
# ColumnPricePerShare = tickerList[0] + " PPShare"
# ColumnPricePerBook = tickerList[0] + " PPBook"
# ColumnCapitalExpenditures = tickerList[0] + " capitalExpenditures"
# ColumnReturnOnInvestment = tickerList[0] + " returnOnInvestment"
# ColumnTotalLiabilities = tickerList[0] + " totalLiabilities"
# ColumnBookValuePerShare = tickerList[0] + " bookValuePerShare"
# ColumnDateColumn = tickerList[0] + " dateColumn"
#
# data = {ColumnKGV: KGVList.reverse(),
#         ColumnPricePerShare: pricePerShare.reverse(),
#         ColumnPricePerBook: pricePerBook.reverse(),
#         ColumnCapitalExpenditures: capitalExpenditures.reverse(),
#         ColumnReturnOnInvestment: returnOnInvestment.reverse(),
#         ColumnTotalLiabilities: totalLiabilities.reverse(),
#         ColumnBookValuePerShare: bookValuePerShare.reverse(),
#         ColumnDateColumn: dateColumn.reverse()
#         }
#
# df = pd.DataFrame(data)
#
# df.drop([], axis=1)
# writer = pd.ExcelWriter(r'C:\Users\rmarn\PycharmProjects\pythonProject\Stocks\ExcelTabels\Test.xlsx')
#
# df.to_excel(writer, tickerList[0])
# writer.save()



df = pd.read_excel(r"C:\Users\rmarn\PycharmProjects\pythonProject\Stocks\ExcelTabels\Test.xlsx", index_col=0)

print(df)

# column_1 = df["NVDA KGV"]
# column_2 = df["NVDA PPShare"]
# correlation = column_1.corr(column_2)
# print(correlation)
#
# column_1 = df["NVDA PPBook"]
# column_2 = df["NVDA PPShare"]
# correlation = column_1.corr(column_2)
# print(correlation)

scale = StandardScaler()

x = df[["NVDA KGV", "NVDA KGV",]]
y = df["NVDA PPShare"]

x[["NVDA KGV", "NVDA KGV"]] = scale.fit_transform(x[["NVDA KGV", "NVDA KGV"]])


print(x)

est = sm.OLS(y, x).fit()
est.summary()


#
#
# # Define a dictionary containing Students data
#data = {'Name': ['Jai', 'Princi', 'Gaurav', 'Anuj'],
 #        'Height': [5.3331, 6.2, 5.1, 5.2],
  #       'Qualification': ['Msc', 'MA', 'Msc', 'Msc']}

# # Convert the dictionary into DataFrame
#df = pd.DataFrame(data)
#
# # Using 'Address' as the column name and equating it to the list
# df2 = df.assign(address=['Delhi', 'Bangalore', 'Chennai', 'Patna'])
#
# # Observe the result
# df2
#
# #df.to_csv(r"C:\Users\\rmarn\PycharmProjects\pythonProject\Stocks\ExcelTabels\AMZNv.csv")
#
# df3 = pd.read_excel(r"C:\Users\rmarn\PycharmProjects\pythonProject\Stocks\ExcelTabels\AMZNv.xlsx")
# print("jdsafhjlh")
# print(df3)

# df = pd.read_excel('firstCopy.xls')
# column_2 = column_2.iloc[::-1].reset_index(drop=True)
# print(column_2)
# plt.plot(column_2)
# plt.ylabel('some numbers')
# plt.show()


