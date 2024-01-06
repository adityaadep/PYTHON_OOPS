class Bill():
    """
    Objects that contains the data about a bill ,such as
    total amount and period of the bill
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:
    """
    Create a flatmate person who lives in
    a Flat and pays a share of the Bill
    """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, Bill, flatmate2):
        coefficient = self.days_in_house/(self.days_in_house+flatmate2.days_in_house)
        return round(coefficient * Bill.amount)
