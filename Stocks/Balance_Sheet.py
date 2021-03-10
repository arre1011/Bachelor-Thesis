from DB.DB_Api.Get import Functions as f


class BalanceSheet:

    def __init__(self, symbole, quarterly):
        self.symbole = symbole
        self.quarterly = quarterly
        self.total_liabilities = f.get_total_liabilities(symbole, quarterly)


