class Category:

    @property
    def total_value(self):
        total_value = 0
        attributes = vars(self)

        for key, value in attributes.items():
            total_value += value

        return total_value


class Needs(Category):
    def __init__(self):
        self.mortgage = 0
        self.rent = 0
        self.groceries = 0
        self.gasoline = 0
        self.car_insurance = 0
        self.health_insurance = 0
        self.laundry = 0
        self.other_insurance = 0
        self.apartment_utilities = 0
        self.electric_bill = 0
        self.internet_bill = 0
        self.renters_insurance = 0
        self.dental_insurance = 0
        self.vision_insurance = 0
        self.student_loans = 0
        self.emergencies = 0


class Wants(Category):
    def __init__(self):
        self.free_spending = 0
        self.subscriptions = 0
        self.vacation_spending = 0


class Savings(Category):
    def __init__(self):
        self.crypto = 0
        self.emergency_fund = 0
        self.retirement = 0
        self.investing = 0


class BudgetSpending:
    def __init__(self):
        self.needs = Needs()
        self.wants = Wants()
        self.savings = Savings()


if __name__ == "__main__":

    monthly_spending = BudgetSpending()

    monthly_spending.needs.electric_bill = 10
    monthly_spending.needs.health_insurance = 72.15
    monthly_spending.needs.rent = 1500.72

    monthly_spending.wants.free_spending = 499.99
    monthly_spending.wants.subscriptions = 222.11

    monthly_spending.savings.retirement = 250.00
    monthly_spending.savings.emergency_fund = 100

    print(monthly_spending.needs.total_value)
    print(monthly_spending.wants.total_value)
    print(monthly_spending.savings.total_value)
