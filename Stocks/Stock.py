from DB.DB_Api.Get import Functions as DBFunctions
from Ratios import ratios_functions as RatiosFunctions


class Stock:

    def __init__(self, symbole, quarterly, object_number ):
        self.symbole = symbole
        self.quarterly = quarterly
        self.objectNumber = object_number
        self.totalLiabilities = DBFunctions.get_total_liabilities(symbole, quarterly)
        self.pricePerEarnings = RatiosFunctions.price_per_earnings(symbole, quarterly, object_number)
