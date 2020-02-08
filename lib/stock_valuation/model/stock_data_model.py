class StockDataModel:
    # Leaving growth as a constant.
    _GROWTH = 0.03

    def __init__(self, ticker, name, free_cash_flow, total_liabilities, total_shareholder_equity,
                 rate_of_avg_debt, beta, shares_outstanding):
        self._ticker = ticker
        self._name = name
        self._free_cash_flow = free_cash_flow
        self._total_liabilities = total_liabilities
        self._total_shareholder_equity = total_shareholder_equity
        self._rate_of_avg_debt = rate_of_avg_debt
        self._beta = beta
        self._shares_outstanding = shares_outstanding

    def get_ticker(self):
        return self._ticker

    def get_name(self):
        return self._name

    def get_free_cash_flow(self):
        return self._free_cash_flow

    def get_total_liabilities(self):
        return self._total_liabilities

    def get_total_shareholder_equity(self):
        return self._total_shareholder_equity

    def get_rate_of_avg_debt(self):
        return self._rate_of_avg_debt

    def get_beta(self):
        return self._beta

    def get_shares_outstanding(self):
        return self._shares_outstanding

    def get_growth(self):
        return self._GROWTH
