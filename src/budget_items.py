from decimal import Decimal


class Category:
    @property
    def subcategories(self):
        return {key: value for (key, value) in vars(self).items()}

    @property
    def total_value(self):
        total_value = Decimal("0.00")

        for key, value in self.subcategories.items():
            total_value += value

        return total_value

    def __str__(self):
        attributes_list = []

        for key, value in sorted(self.subcategories.items()):
            key = key.replace("_", " ").title()
            attribute_string = f"\t{key} = ${value:,}"
            attributes_list.append(attribute_string)

        attributes_list.append(f"\tTOTAL = ${self.total_value:,}")

        return "\n".join(attributes_list)


class Needs(Category):
    def __init__(self):
        self.car_insurance = Decimal("0.00")
        self.dental_insurance = Decimal("0.00")
        self.electric_bill = Decimal("0.00")
        self.emergencies = Decimal("0.00")
        self.gasoline = Decimal("0.00")
        self.groceries = Decimal("0.00")
        self.health_insurance = Decimal("0.00")
        self.internet_bill = Decimal("0.00")
        self.laundry = Decimal("0.00")
        self.misc = Decimal("0.00")
        self.mortgage = Decimal("0.00")
        self.other_insurance = Decimal("0.00")
        self.rent = Decimal("0.00")
        self.renters_insurance = Decimal("0.00")
        self.student_loans = Decimal("0.00")
        self.taxes = Decimal("0.00")
        self.vision_insurance = Decimal("0.00")


class Wants(Category):
    def __init__(self):
        self.free_spending = Decimal("0.00")
        self.misc = Decimal("0.00")
        self.subscriptions = Decimal("0.00")
        self.vacation_spending = Decimal("0.00")


class Savings(Category):
    def __init__(self):
        self.crypto = Decimal("0.00")
        self.emergency_fund = Decimal("0.00")
        self.investing = Decimal("0.00")
        self.misc = Decimal("0.00")
        self.retirement = Decimal("0.00")


class Income(Category):
    def __init__(self):
        self.earnings = Decimal("0.00")
        self.tax_returns = Decimal("0.00")


class Reimbursements(Category):
    def __init__(self):
        self.bills = Decimal("0.00")
        self.credit_card_rewards = Decimal("0.00")
        self.free_spending = Decimal("0.00")
        self.rent = Decimal("0.00")


class BudgetSpending:
    def __init__(self, name=""):
        self.name = name
        self.needs = Needs()
        self.wants = Wants()
        self.savings = Savings()
        self.income = Income()
        self.reimbursements = Reimbursements()

    @property
    def categories(self):
        return {key: value for (key, value) in vars(self).items() if isinstance(value, Category)}

    @property
    def total_spending(self):
        return (
            self.needs.total_value + self.wants.total_value + self.savings.total_value - self.reimbursements.total_value
        )

    @property
    def total_income(self):
        return self.income.total_value

    @property
    def deficit_or_surplus(self):
        return self.total_income - self.total_spending

    def __str__(self):
        budget_spending_string = []

        budget_spending_string.append(self.name)

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
        budget_spending_string.append("Reimbursements:")
        budget_spending_string.append(str(self.reimbursements))

        budget_spending_string.append("-" * 40)
        budget_spending_string.append(f"TOTAL SPENDING = ${self.total_spending:,}")

        if self.deficit_or_surplus < 0:
            budget_spending_string.append(f"DEFICIT = ${abs(self.deficit_or_surplus):,}")
        else:
            budget_spending_string.append(f"SURPLUS = ${self.deficit_or_surplus:,}")

        budget_spending_string.append("*" * 40)

        return "\n".join(budget_spending_string)
