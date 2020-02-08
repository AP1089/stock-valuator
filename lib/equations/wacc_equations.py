class WaccEquations:

    def __init__(self, total_liabilities, total_shareholder_equity,
                 rate_of_avg_debt, beta):
        self._total_liabilities = total_liabilities
        self._total_shareholder_equity = total_shareholder_equity
        self._rate_of_avg_debt = rate_of_avg_debt
        self._beta = beta

    def run(self):
        return self.wacc_first_half() + self.wacc_second_half()

    def wacc_first_half(self):
        denominator = (self._total_liabilities + self._total_shareholder_equity)
        return (self._total_liabilities / denominator) * self._rate_of_avg_debt * (1 - .35)

    def wacc_second_half(self):
        denominator = (self._total_liabilities + self._total_shareholder_equity)
        return (self._total_shareholder_equity / denominator) * self._beta
