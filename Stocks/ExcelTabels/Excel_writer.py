import pandas as pd
from Stocks.Stock import Stock
from Stocks import Helper_functions


tickerList = ['AMZN']

quartilList = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

# Lists of Ratios
KGVList = []
pricePerShare = []
pricePerBook = []
capitalExpenditures = []
returnOnInvestment = []
totalLiabilities = []
bookValuePerShare = []
dateColumn = []
tickerColumn = []
esg =[]


data = []
for ticker in tickerList:
    dateList = Helper_functions.get_list_of_dates(ticker)
    i = 0
    while i < len(dateList):
        Stock1 = Stock(ticker, dateList[i], quartilList[i])
        print(ticker + "   " + dateList[i])

        KGVList.append(str(Stock1.pricePerEarnings))
        pricePerShare.append(str(Stock1.stockPrice))
        pricePerBook.append(str(Stock1.pricePerBookRatioPerShare))
        capitalExpenditures.append(Stock1.capitalExpenditures)
        returnOnInvestment.append(Stock1.returnOnInvestment)
        totalLiabilities.append(str(Stock1.totalLiabilities))
        bookValuePerShare.append(str(Stock1.bookValuePerShare))
        dateColumn.append(dateList[i])
        tickerColumn.append(ticker)
        esg.append(Stock1.esgRating)
        i += 1

tickerList = ['']
ColumnKGV = tickerList[0] + "KGV"
ColumnPricePerShare = tickerList[0] + "PPShare"
ColumnPricePerBook = tickerList[0] + "PPBook"
ColumnCapitalExpenditures = tickerList[0] + "capitalExpenditures"
ColumnReturnOnInvestment = tickerList[0] + "returnOnInvestment"
ColumnTotalLiabilities = tickerList[0] + "totalLiabilities"
ColumnBookValuePerShare = tickerList[0] + "bookValuePerShare"
ColumnDateColumn = tickerList[0] + "dateColumn"
ColumnTicker = tickerList[0] + "Ticker"
ColumnESG = tickerList[0] + "ESG"

data = {ColumnKGV: KGVList,
        ColumnPricePerShare: pricePerShare,
        ColumnPricePerBook: pricePerBook,
        ColumnCapitalExpenditures: capitalExpenditures,
        ColumnReturnOnInvestment: returnOnInvestment,
        ColumnTotalLiabilities: totalLiabilities,
        ColumnBookValuePerShare: bookValuePerShare,
        ColumnDateColumn: dateColumn,
        ColumnTicker: tickerColumn,
        ColumnESG: esg
        }

df = pd.DataFrame(data)

df.drop([])
writer = pd.ExcelWriter(r'C:\Users\rmarn\PycharmProjects\pythonProject\Stocks\ExcelTabels\Test2.xlsx')

df.to_excel(writer, index=False)
writer.save()






# df = pd.read_excel('firstCopy.xls')
# column_2 = column_2.iloc[::-1].reset_index(drop=True)
# print(column_2)
# plt.plot(column_2)
# plt.ylabel('some numbers')
# plt.show()


