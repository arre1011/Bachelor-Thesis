import pandas as pd
from Stocks.Stock import Stock
from Stocks import Helper_functions




#
# tickerList = [ 'NVDA']
#
# quartilList = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
#
# KGVList = []
# pricePerShare = []
# pricePerBook = []
# data = []
# for ticker in tickerList:
#     dateList = Helper_functions.get_list_of_dates(ticker)
#     i = 0
#     while i < len(dateList):
#         Stock1 = Stock(ticker, dateList[i], quartilList[i])
#         KGVList.append(str(Stock1.pricePerEarnings))
#         pricePerShare.append(str(Stock1.stockPrice))
#         pricePerBook.append(str(Stock1.pricePerBookRatioPerShare))
#         print("Company:                             " + ticker)
#         print("     Date:                                " + dateList[i])
#         # print("capitalExpenditures:                 " + Stock1.capitalExpenditures)
#         # print("     Stcok Price:                         " + str(Stock1.stockPrice))
#         # print("Return on Investment:                " + Stock1.returnOnInvestment)
#         # print("     TotalLiabilities:                    " + str(Stock1.totalLiabilities))
#         print("Price per earnings:                  " + str(Stock1.pricePerEarnings))
#         # print("     Book Value per Share:                " + str(Stock1.bookValuePerShare))
#         # print("Price per Book Ratio per Share:       " + str(Stock1.pricePerBookRatioPerShare))
#         i += 1
#
# columnKGV = tickerList[0] + " KGV"
# columnPricePerShare = tickerList[0] + " PPShare"
# columnPricePerBook = tickerList[0] + " PPBook"
#
# data = {columnKGV: KGVList,
#         columnPricePerShare: pricePerShare,
#         columnPricePerBook: pricePerBook}
#
# df = pd.DataFrame(data)
#
# df.drop([], axis=1)
# writer = pd.ExcelWriter(r'C:\Users\rmarn\PycharmProjects\pythonProject\Stocks\ExcelTabels\Test.xlsx')
#
# df.to_excel(writer, tickerList[0])
# writer.save()

#
#
df = pd.read_excel(r"C:\Users\rmarn\PycharmProjects\pythonProject\Stocks\ExcelTabels\Test.xlsx", index_col=0)

print(df)

column_1 = df["NVDA KGV"]
column_2 = df["NVDA PPShare"]
correlation = column_1.corr(column_2)
print(correlation)

column_1 = df["NVDA PPBook"]
column_2 = df["NVDA PPShare"]
correlation = column_1.corr(column_2)
print(correlation)



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
#


