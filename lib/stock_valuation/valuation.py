from lib.equations.wacc_equations import WaccEquations
from lib.stock_valuation.api.stock_data_service import StockDataService
from lib.util import Util


class Valuation:

    def __init__(self, ticker):
        self._ticker = ticker.upper()

    def run(self):
        _data = StockDataService(self._ticker)
        _model = _data.get_ticker_data()

        if _model is None:
            return "No Ticker Found :(\r\n\r\nPlease enter a valid stock ticker found in the mock_stock_data file"
        else:
            return self._get_valuation(self, _model)

    @staticmethod
    def _get_valuation(self, _model):
        wacc = self._get_wacc(_model)
        value = _model.get_free_cash_flow() / (wacc - _model.get_growth())
        return "$" + str(Util.round_decimal_two_places(value / _model.get_shares_outstanding()))

    @staticmethod
    def _get_wacc(_model):
        wacc_equations = WaccEquations(_model.get_total_liabilities(),
                                       _model.get_total_shareholder_equity(),
                                       _model.get_rate_of_avg_debt(),
                                       _model.get_beta())

        wacc_value = wacc_equations.run()
        return wacc_value
