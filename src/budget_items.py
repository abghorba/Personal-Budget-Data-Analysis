class Category:

    @property
    def total_value(self):
        total_value = 0
        attributes = vars(self)

        for key, value in attributes.items():
            total_value += value

        return total_value

    def __str__(self):

        attributes_list = []
        attributes = vars(self)

        for key, value in sorted(attributes.items()):

            key = key.replace("_", " ").title()
            attribute_string = f"\t{key} = ${value:,.2f}"
            attributes_list.append(attribute_string)

        attributes_list.append(f"\tTOTAL = ${self.total_value:,.2f}")

        return "\n".join(attributes_list)


class Needs(Category):
    def __init__(self):
        self.car_insurance = 0
        self.dental_insurance = 0
        self.electric_bill = 0
        self.emergencies = 0
        self.gasoline = 0
        self.groceries = 0
        self.health_insurance = 0
        self.internet_bill = 0
        self.laundry = 0
        self.misc = 0
        self.mortgage = 0.00
        self.other_insurance = 0
        self.rent = 0
        self.renters_insurance = 0
        self.student_loans = 0
        self.taxes = 0
        self.vision_insurance = 0


class Wants(Category):
    def __init__(self):
        self.free_spending = 0
        self.misc = 0
        self.subscriptions = 0
        self.vacation_spending = 0


class Savings(Category):
    def __init__(self):
        self.crypto = 0
        self.emergency_fund = 0
        self.investing = 0
        self.misc = 0
        self.retirement = 0


class Income(Category):
    def __init__(self):
        self.earnings = 0
        self.tax_returns = 0
        self.rewards = 0


class BudgetSpending:
    def __init__(self):
        self.needs = Needs()
        self.wants = Wants()
        self.savings = Savings()
        self.income = Income()

    @property
    def total_spending(self):
        return self.needs.total_value + self.wants.total_value + self.savings.total_value

    @property
    def total_income(self):
        return self.income.total_value

    def __str__(self):

        deficit = self.total_income - self.total_spending

        budget_spending_string = []

        budget_spending_string.append("*" * 40)
        budget_spending_string.append("Income:")
        budget_spending_string.append(str(self.income))

        budget_spending_string.append("-" * 40)
        budget_spending_string.append("Needs:")
        budget_spending_string.append(str(self.needs))

        budget_spending_string.append("-" * 40)
        budget_spending_string.append("Wants:")
        budget_spending_string.append(str(self.wants))

        budget_spending_string.append("-" * 40)
        budget_spending_string.append("Savings:")
        budget_spending_string.append(str(self.savings))

        budget_spending_string.append("-" * 40)
        budget_spending_string.append(f"TOTAL SPENDING = ${self.total_spending:,.2f}")

        if deficit < 0:
            budget_spending_string.append(f"DEFICIT = ${abs(deficit):,.2f}")
        else:
            budget_spending_string.append(f"SURPLUS = ${deficit:,.2f}")

        budget_spending_string.append("*" * 40)

        return "\n".join(budget_spending_string)


if __name__ == "__main__":

    monthly_spending = BudgetSpending()

    monthly_spending.needs.electric_bill = 10
    monthly_spending.needs.health_insurance = 72.15
    monthly_spending.needs.rent = 1500.72

    monthly_spending.wants.free_spending = 499.99
    monthly_spending.wants.subscriptions = 222.11

    monthly_spending.savings.retirement = 250.00
    monthly_spending.savings.emergency_fund = 100

    print(monthly_spending)
