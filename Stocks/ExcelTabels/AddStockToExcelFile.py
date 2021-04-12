from Stocks.Stock import Stock
from Stocks import Helper_functions
from openpyxl import load_workbook


def ckeck_if_nono(stock):
    if stock.symbole == "null":
        return False
    elif stock.returnOnInvestment == "null":
        return False
    elif stock.totalLiabilities == "null":
        return False
    elif stock.pricePerEarnings == "null":
        return False
    elif stock.capitalExpenditures == "null":
        return False
    elif stock.bookValuePerShare == "null":
        return False
    elif stock.pricePerBookRatioPerShare == "null":
        return False
    elif stock.esgRating == "null":
        return False
    elif stock.totalAssets == "null":
        return False
    elif stock.retainedEarnings == "null":
        return False
    elif stock.totalCurrentAssets == "null":
        return False
    elif stock.totalAssets == "null":
        return False
    elif stock.netIncome == "null":
        return False
    elif stock.changeToNetincome == "null":
        return False
    elif stock.capitalExpenditures == "null":
        return False
    elif stock.changeReceivables == "null":
        return False
    elif stock.incomeBeforeTax == "null":
        return False
    elif stock.ebit == "null":
        return False
    elif stock.grossProfit == "null":
        return False
    elif stock.totalRevenue == "null":
        return False
    elif stock.costOfRevenue == "null":
        return False

    return True


def add_new_stock_to_excel_file(tickerList, quartilList):

    for ticker in tickerList:
        dateList = Helper_functions.get_list_of_dates(ticker)
        i = 0
        while i < len(dateList):
            stock = Stock(ticker, dateList[i], quartilList[i])
            print(ticker + "   " + dateList[i])

            stockHaveNoneAtributte = ckeck_if_nono(stock)
            if stockHaveNoneAtributte == True:
                new_row_data = ["1",
                                str(stock.symbole),
                                str(stock.quarterly),
                                str(stock.returnOnInvestment),
                                str(stock.totalLiabilities),
                                str(stock.pricePerEarnings),
                                str(stock.capitalExpenditures),
                                str(stock.bookValuePerShare),
                                str(stock.pricePerBookRatioPerShare),
                                str(stock.esgRating),
                                str(stock.totalAssets),
                                str(stock.retainedEarnings),
                                str(stock.totalCurrentAssets),
                                str(stock.totalAssets),
                                str(stock.netIncome),
                                str(stock.changeToNetincome),
                                str(stock.capitalExpenditures),
                                str(stock.changeReceivables),
                                str(stock.incomeBeforeTax),
                                str(stock.ebit),
                                str(stock.grossProfit),
                                str(stock.totalRevenue),
                                str(stock.costOfRevenue),
                                str(stock.sector)]

                wb = load_workbook(r'C:\Users\rmarn\PycharmProjects\pythonProject\Stocks\ExcelTabels\StocksTest.xlsx')
                ws = wb.worksheets[0]
                ws.append(new_row_data)
                wb.save(r'C:\Users\rmarn\PycharmProjects\pythonProject\Stocks\ExcelTabels\StocksTest.xlsx')
            else:
                print("Object has a None Attribute")

            i += 1


tickerList = [  'ACN', 'QCOM', 'DHR', 'VZ', 'NVDA']
quartilList = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

add_new_stock_to_excel_file(tickerList, quartilList)

tickerList = ['AAPL','AMZN', 'GOOGL', 'AAPL', 'MSFT', 'V', 'MA', 'PG', 'CMCSA', 'KO', 'ADBE', 'NKE', 'PEP', 'T', 'CRM',
 'INTC', 'ORCL', 'CSCO', 'TMO', 'ACN', 'QCOM', 'DHR', 'VZ', 'NVDA']











