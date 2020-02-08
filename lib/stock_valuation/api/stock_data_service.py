import json
import os
from lib.stock_valuation.model.stock_data_model import StockDataModel
from lib.util import Util


class StockDataService:

    def __init__(self, ticker):
        self._ticker = ticker

    def get_ticker_data(self):
        script_dir = os.path.dirname(__file__)
        file_path = os.path.join(script_dir, 'mock_stock_data.json')
        with open(file_path, "r") as fp:
            data = json.load(fp)

            index = 0
            for d in data:

                if d == self._ticker:
                    return self.convert_data_to_model(self._ticker, data[self._ticker])
                elif index == len(data) - 1:
                    return None
                index += 1

    @staticmethod
    def convert_data_to_model(ticker, mock_data):

        return StockDataModel(ticker,
                              mock_data["Name"],
                              Util.convert_number_to_float(mock_data["FreeCashFlow"]),
                              Util.convert_number_to_float(mock_data["TotalLiabilities"]),
                              Util.convert_number_to_float(mock_data["TotalShareholderEquity"]),
                              Util.convert_number_to_float(mock_data["RateOfAvgDebt"]),
                              Util.convert_number_to_float(mock_data["Beta"]),
                              Util.convert_number_to_float(mock_data["SharesOutstanding"]))
