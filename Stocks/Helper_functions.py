import pymongo


def get_date_of_share(ticker):
    date = ['2020-03-31', '2020-06-30', '2020-09-30', '2020-12-31', '2020-11-30', '2020-05-31']

    result = ""
    for y in date:
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = myclient["Aktien_DB"]
        mycol = mydb["Aktien"]

        Query = mycol.find({"General.Code": ticker})

        for x in Query:
            try:
                a = x.get('Financials')
                b = a.get('Balance_Sheet')
                e = b.get('yearly')
                z = e.get(y)
                totalLiabilities = z.get("totalLiab")
                result = y
            except:
                print()
    return result

def get_list_of_dates(ticker):
    date = get_date_of_share(ticker)

    if date == '2020-03-31':
        datelist = ['2020-03-31', '2019-03-31', '2018-03-31', '2017-03-31', '2016-03-31', '2015-03-31', '2014-03-31',
                    '2013-03-31', '2012-03-31', '2011-03-31']
        return datelist
    elif date == '2020-06-30':
        datelist = ['2020-06-30', '2019-06-30', '2018-06-30', '2017-06-30', '2016-06-30', '2015-06-30', '2014-06-30',
                    '2013-06-30', '2012-06-30', '2011-06-30']
        return datelist
    elif date == '2020-09-30':
        datelist = ['2020-09-30', '2019-09-30', '2018-09-30', '2017-09-30', '2016-09-30', '2015-09-30', '2014-09-30',
                    '2013-09-30', '2012-09-30', '2011-09-30']
        return datelist
    elif date == '2020-12-31':
        datelist = ['2020-12-31', '2019-12-31', '2018-12-31', '2017-12-31', '2016-12-31', '2015-12-31', '2014-12-31',
                    '2013-12-31', '2012-12-31', '2011-12-31']
        return datelist
    elif date == '2020-11-30':
        datelist = ['2020-11-30', '2019-11-30', '2018-11-30', '2017-11-30', '2016-11-30', '2015-11-30', '2014-11-30',
                    '2013-11-30', '2012-11-30', '2011-11-30', ]
        return datelist
    elif date == '2020-05-31':
        datelist = ['2020-05-31', '2019-05-31', '2018-05-31', '2017-05-31', '2016-05-31', '2015-05-31', '2014-05-31',
                    '2013-05-31', '2012-05-31', '2011-05-31']
        return datelist




