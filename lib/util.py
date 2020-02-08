class Util:
    @staticmethod
    def convert_number_to_float(number):
        if type(number) == str:
            return float(number.replace(',', ''))
        elif type(number) == int:
            return float(number)
        elif type(number) == float:
            return number
        else:
            print("error converting to double")

    @staticmethod
    def round_decimal_two_places(number):
        return round(number, 2)
