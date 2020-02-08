from lib.stock_valuation.valuation import Valuation


def main():
    # Note:
    # 1. This program is using fake data and should not be used to predict actual stock prices.
    # 2. User can only search the stocks that are in the lib/stock_valuation/api/mock_stock_data.json file:
    # -> AAPL, JPM, GILD, COP.
    # Search a ticker below!
    _ticker = "AAPL"
    valuation = Valuation(_ticker)
    value = valuation.run()
    print(value)


if __name__ == "__main__":
    main()
