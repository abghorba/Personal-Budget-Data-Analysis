from copy import deepcopy
from decimal import Decimal

import pytest

from src.budget_items import BudgetSpending, Category, Income, Needs, Reimbursements, Savings, Wants


class TestCategoryClasses:
    # Set up Category instance
    test_category_obj = Category()
    test_category_obj_str = "\tTOTAL = $0.00"

    # Set up Needs instances
    test_needs_obj = Needs()
    test_needs_obj.car_insurance = Decimal("139.00")
    test_needs_obj.electric_bill = Decimal("79.99")
    test_needs_obj.gasoline = Decimal("125.73")
    test_needs_obj.groceries = Decimal("421.23")
    test_needs_obj.internet_bill = Decimal("73.99")
    test_needs_obj.rent = Decimal("1500")
    test_needs_obj_str = (
        "\tCar Insurance = $139.00"
        "\n\tDental Insurance = $0.00"
        "\n\tElectric Bill = $79.99"
        "\n\tEmergencies = $0.00"
        "\n\tGasoline = $125.73"
        "\n\tGroceries = $421.23"
        "\n\tHealth Insurance = $0.00"
        "\n\tInternet Bill = $73.99"
        "\n\tLaundry = $0.00"
        "\n\tMisc = $0.00"
        "\n\tMortgage = $0.00"
        "\n\tOther Insurance = $0.00"
        "\n\tRent = $1,500.00"
        "\n\tRenters Insurance = $0.00"
        "\n\tStudent Loans = $0.00"
        "\n\tTaxes = $0.00"
        "\n\tVision Insurance = $0.00"
        "\n\tTOTAL = $2,339.94"
    )

    empty_needs_obj = Needs()

    # Set up Wants instances
    test_wants_obj = Wants()
    test_wants_obj.free_spending = Decimal("637.22")
    test_wants_obj.subscriptions = Decimal("62.78")
    test_wants_obj_str = (
        "\tFree Spending = $637.22"
        "\n\tMisc = $0.00"
        "\n\tSubscriptions = $62.78"
        "\n\tVacation Spending = $0.00"
        "\n\tTOTAL = $700.00"
    )

    empty_wants_obj = Wants()

    # Set up Savings instances
    test_savings_obj = Savings()
    test_savings_obj.emergency_fund = Decimal("200")
    test_savings_obj.investing = Decimal("1000")
    test_savings_obj.retirement = Decimal("350")
    test_savings_obj_str = (
        "\tCrypto = $0.00"
        "\n\tEmergency Fund = $200.00"
        "\n\tInvesting = $1,000.00"
        "\n\tMisc = $0.00"
        "\n\tRetirement = $350.00"
        "\n\tTOTAL = $1,550.00"
    )

    empty_savings_obj = Savings()

    # Set up Income instances
    test_income_obj = Income()
    test_income_obj.earnings = Decimal("3211.66")
    test_income_obj_str = "\tEarnings = $3,211.66" "\n\tTax Returns = $0.00" "\n\tTOTAL = $3,211.66"

    empty_income_obj = Savings()

    # Set up Reimbursements instances
    test_reimbursements_obj = Reimbursements()
    test_reimbursements_obj.bills = Decimal("25.33")
    test_reimbursements_obj.free_spending = Decimal("50")
    test_reimbursements_obj_str = (
        "\tBills = $25.33"
        "\n\tCredit Card Rewards = $0.00"
        "\n\tFree Spending = $50.00"
        "\n\tRent = $0.00"
        "\n\tTOTAL = $75.33"
    )

    empty_reimbursements_obj = Reimbursements()

    @pytest.mark.parametrize(
        "category",
        [test_category_obj, test_needs_obj, test_wants_obj, test_savings_obj, test_income_obj, test_reimbursements_obj],
    )
    def test_subcategories_property(self, category):
        """Tests Category.subcategories property."""

        subcategories = category.subcategories

        if isinstance(category, Needs):
            assert len(subcategories) == 17
            assert "car_insurance" in subcategories
            assert category.car_insurance == subcategories["car_insurance"]
            assert "dental_insurance" in subcategories
            assert category.dental_insurance == subcategories["dental_insurance"]
            assert "electric_bill" in subcategories
            assert category.electric_bill == subcategories["electric_bill"]
            assert "emergencies" in subcategories
            assert category.emergencies == subcategories["emergencies"]
            assert "gasoline" in subcategories
            assert category.gasoline == subcategories["gasoline"]
            assert "groceries" in subcategories
            assert category.groceries == subcategories["groceries"]
            assert "health_insurance" in subcategories
            assert category.health_insurance == subcategories["health_insurance"]
            assert "internet_bill" in subcategories
            assert category.internet_bill == subcategories["internet_bill"]
            assert "laundry" in subcategories
            assert category.laundry == subcategories["laundry"]
            assert "misc" in subcategories
            assert category.misc == subcategories["misc"]
            assert "mortgage" in subcategories
            assert category.mortgage == subcategories["mortgage"]
            assert "other_insurance" in subcategories
            assert category.other_insurance == subcategories["other_insurance"]
            assert "rent" in subcategories
            assert category.rent == subcategories["rent"]
            assert "renters_insurance" in subcategories
            assert category.renters_insurance == subcategories["renters_insurance"]
            assert "student_loans" in subcategories
            assert category.student_loans == subcategories["student_loans"]
            assert "taxes" in subcategories
            assert category.taxes == subcategories["taxes"]
            assert "vision_insurance" in subcategories
            assert category.vision_insurance == subcategories["vision_insurance"]

        elif isinstance(category, Wants):
            assert len(subcategories) == 4
            assert "free_spending" in subcategories
            assert category.free_spending == subcategories["free_spending"]
            assert "misc" in subcategories
            assert category.misc == subcategories["misc"]
            assert "subscriptions" in subcategories
            assert category.subscriptions == subcategories["subscriptions"]
            assert "vacation_spending" in subcategories
            assert category.vacation_spending == subcategories["vacation_spending"]

        elif isinstance(category, Savings):
            assert len(subcategories) == 5
            assert "crypto" in subcategories
            assert category.crypto == subcategories["crypto"]
            assert "emergency_fund" in subcategories
            assert category.emergency_fund == subcategories["emergency_fund"]
            assert "investing" in subcategories
            assert category.investing == subcategories["investing"]
            assert "misc" in subcategories
            assert category.misc == subcategories["misc"]
            assert "retirement" in subcategories
            assert category.retirement == subcategories["retirement"]

        elif isinstance(category, Income):
            assert len(subcategories) == 2
            assert "earnings" in subcategories
            assert category.earnings == subcategories["earnings"]
            assert "tax_returns" in subcategories
            assert category.tax_returns == subcategories["tax_returns"]

        elif isinstance(category, Reimbursements):
            assert len(subcategories) == 4
            assert "bills" in subcategories
            assert category.bills == subcategories["bills"]
            assert "credit_card_rewards" in subcategories
            assert category.credit_card_rewards == subcategories["credit_card_rewards"]
            assert "free_spending" in subcategories
            assert category.free_spending == subcategories["free_spending"]
            assert "rent" in subcategories
            assert category.rent == subcategories["rent"]

        else:
            assert len(subcategories) == 0

    @pytest.mark.parametrize(
        "category,expected_value",
        [
            (test_category_obj, Decimal("0.00")),
            (test_needs_obj, Decimal("2339.94")),
            (test_wants_obj, Decimal("700.00")),
            (test_savings_obj, Decimal("1550.00")),
            (test_income_obj, Decimal("3211.66")),
            (test_reimbursements_obj, Decimal("75.33")),
            (empty_needs_obj, Decimal("0.00")),
            (empty_wants_obj, Decimal("0.00")),
            (empty_savings_obj, Decimal("0.00")),
            (empty_income_obj, Decimal("0.00")),
            (empty_reimbursements_obj, Decimal("0.00")),
        ],
    )
    def test_total_value_property(self, category, expected_value):
        """Tests Category.total_value property."""

        assert category.total_value == expected_value

    @pytest.mark.parametrize(
        "category,expected_value",
        [
            (test_category_obj, True),
            (test_needs_obj, False),
            (test_wants_obj, False),
            (test_savings_obj, False),
            (test_income_obj, False),
            (test_reimbursements_obj, False),
            (empty_needs_obj, True),
            (empty_wants_obj, True),
            (empty_savings_obj, True),
            (empty_income_obj, True),
            (empty_reimbursements_obj, True),
        ],
    )
    def test_all_zeroes_property(self, category, expected_value):
        """Test Category.all_zeroes property."""

        assert category.all_zeroes == expected_value

    @pytest.mark.parametrize(
        "category,expected_value",
        [
            (test_category_obj, test_category_obj_str),
            (test_needs_obj, test_needs_obj_str),
            (test_wants_obj, test_wants_obj_str),
            (test_savings_obj, test_savings_obj_str),
            (test_income_obj, test_income_obj_str),
            (test_reimbursements_obj, test_reimbursements_obj_str),
        ],
    )
    def test_to_str(self, category, expected_value):
        """Tests that Category.__str__() is overwritten and returns correct values."""

        assert str(category) == expected_value


class TestBudgetSpendingClass:
    # Set up BudgetSpending instances
    test_budget_spending_obj_deficit = BudgetSpending("Test")

    # Set up Needs
    test_budget_spending_obj_deficit.needs.car_insurance = Decimal("139.00")
    test_budget_spending_obj_deficit.needs.electric_bill = Decimal("79.99")
    test_budget_spending_obj_deficit.needs.gasoline = Decimal("125.73")
    test_budget_spending_obj_deficit.needs.groceries = Decimal("421.23")
    test_budget_spending_obj_deficit.needs.internet_bill = Decimal("73.99")
    test_budget_spending_obj_deficit.needs.rent = Decimal("1500")

    # Set up Wants
    test_budget_spending_obj_deficit.wants.free_spending = Decimal("637.22")
    test_budget_spending_obj_deficit.wants.subscriptions = Decimal("62.78")

    # Set up Savings
    test_budget_spending_obj_deficit.savings.emergency_fund = Decimal("200")
    test_budget_spending_obj_deficit.savings.investing = Decimal("1000")
    test_budget_spending_obj_deficit.savings.retirement = Decimal("350")

    # Set up Income
    test_budget_spending_obj_deficit.income.earnings = Decimal("3211.66")

    # Set up Reimbursements
    test_budget_spending_obj_deficit.reimbursements.bills = Decimal("25.33")
    test_budget_spending_obj_deficit.reimbursements.free_spending = Decimal("50")

    test_budget_spending_obj_deficit_str = (
        "Test"
        "\n****************************************"
        "\nIncome:"
        "\n\tEarnings = $3,211.66"
        "\n\tTax Returns = $0.00"
        "\n\tTOTAL = $3,211.66"
        "\n----------------------------------------"
        "\nNeeds:"
        "\n\tCar Insurance = $139.00"
        "\n\tDental Insurance = $0.00"
        "\n\tElectric Bill = $79.99"
        "\n\tEmergencies = $0.00"
        "\n\tGasoline = $125.73"
        "\n\tGroceries = $421.23"
        "\n\tHealth Insurance = $0.00"
        "\n\tInternet Bill = $73.99"
        "\n\tLaundry = $0.00"
        "\n\tMisc = $0.00"
        "\n\tMortgage = $0.00"
        "\n\tOther Insurance = $0.00"
        "\n\tRent = $1,500.00"
        "\n\tRenters Insurance = $0.00"
        "\n\tStudent Loans = $0.00"
        "\n\tTaxes = $0.00"
        "\n\tVision Insurance = $0.00"
        "\n\tTOTAL = $2,339.94"
        "\n----------------------------------------"
        "\nWants:"
        "\n\tFree Spending = $637.22"
        "\n\tMisc = $0.00"
        "\n\tSubscriptions = $62.78"
        "\n\tVacation Spending = $0.00"
        "\n\tTOTAL = $700.00"
        "\n----------------------------------------"
        "\nSavings:"
        "\n\tCrypto = $0.00"
        "\n\tEmergency Fund = $200.00"
        "\n\tInvesting = $1,000.00"
        "\n\tMisc = $0.00"
        "\n\tRetirement = $350.00"
        "\n\tTOTAL = $1,550.00"
        "\n----------------------------------------"
        "\nReimbursements:"
        "\n\tBills = $25.33"
        "\n\tCredit Card Rewards = $0.00"
        "\n\tFree Spending = $50.00"
        "\n\tRent = $0.00"
        "\n\tTOTAL = $75.33"
        "\n----------------------------------------"
        "\nTOTAL SPENDING = $4,514.61"
        "\nDEFICIT = $1,302.95"
        "\n****************************************"
    )

    # Set up a BudgetSpending object to have a surplus
    test_budget_spending_obj_surplus = deepcopy(test_budget_spending_obj_deficit)
    test_budget_spending_obj_surplus.needs.rent = Decimal("1400.00")
    test_budget_spending_obj_surplus.income.earnings = Decimal("5000.00")

    test_budget_spending_obj_surplus_str = (
        "Test"
        "\n****************************************"
        "\nIncome:"
        "\n\tEarnings = $5,000.00"
        "\n\tTax Returns = $0.00"
        "\n\tTOTAL = $5,000.00"
        "\n----------------------------------------"
        "\nNeeds:"
        "\n\tCar Insurance = $139.00"
        "\n\tDental Insurance = $0.00"
        "\n\tElectric Bill = $79.99"
        "\n\tEmergencies = $0.00"
        "\n\tGasoline = $125.73"
        "\n\tGroceries = $421.23"
        "\n\tHealth Insurance = $0.00"
        "\n\tInternet Bill = $73.99"
        "\n\tLaundry = $0.00"
        "\n\tMisc = $0.00"
        "\n\tMortgage = $0.00"
        "\n\tOther Insurance = $0.00"
        "\n\tRent = $1,400.00"
        "\n\tRenters Insurance = $0.00"
        "\n\tStudent Loans = $0.00"
        "\n\tTaxes = $0.00"
        "\n\tVision Insurance = $0.00"
        "\n\tTOTAL = $2,239.94"
        "\n----------------------------------------"
        "\nWants:"
        "\n\tFree Spending = $637.22"
        "\n\tMisc = $0.00"
        "\n\tSubscriptions = $62.78"
        "\n\tVacation Spending = $0.00"
        "\n\tTOTAL = $700.00"
        "\n----------------------------------------"
        "\nSavings:"
        "\n\tCrypto = $0.00"
        "\n\tEmergency Fund = $200.00"
        "\n\tInvesting = $1,000.00"
        "\n\tMisc = $0.00"
        "\n\tRetirement = $350.00"
        "\n\tTOTAL = $1,550.00"
        "\n----------------------------------------"
        "\nReimbursements:"
        "\n\tBills = $25.33"
        "\n\tCredit Card Rewards = $0.00"
        "\n\tFree Spending = $50.00"
        "\n\tRent = $0.00"
        "\n\tTOTAL = $75.33"
        "\n----------------------------------------"
        "\nTOTAL SPENDING = $4,414.61"
        "\nSURPLUS = $585.39"
        "\n****************************************"
    )

    # Set up an empty BudgetSpending object
    empty_budget_spending_obj = BudgetSpending("Empty")

    empty_budget_spending_obj_str = (
        "Empty"
        "\n****************************************"
        "\nIncome:"
        "\n\tEarnings = $0.00"
        "\n\tTax Returns = $0.00"
        "\n\tTOTAL = $0.00"
        "\n----------------------------------------"
        "\nNeeds:"
        "\n\tCar Insurance = $0.00"
        "\n\tDental Insurance = $0.00"
        "\n\tElectric Bill = $0.00"
        "\n\tEmergencies = $0.00"
        "\n\tGasoline = $0.00"
        "\n\tGroceries = $0.00"
        "\n\tHealth Insurance = $0.00"
        "\n\tInternet Bill = $0.00"
        "\n\tLaundry = $0.00"
        "\n\tMisc = $0.00"
        "\n\tMortgage = $0.00"
        "\n\tOther Insurance = $0.00"
        "\n\tRent = $0.00"
        "\n\tRenters Insurance = $0.00"
        "\n\tStudent Loans = $0.00"
        "\n\tTaxes = $0.00"
        "\n\tVision Insurance = $0.00"
        "\n\tTOTAL = $0.00"
        "\n----------------------------------------"
        "\nWants:"
        "\n\tFree Spending = $0.00"
        "\n\tMisc = $0.00"
        "\n\tSubscriptions = $0.00"
        "\n\tVacation Spending = $0.00"
        "\n\tTOTAL = $0.00"
        "\n----------------------------------------"
        "\nSavings:"
        "\n\tCrypto = $0.00"
        "\n\tEmergency Fund = $0.00"
        "\n\tInvesting = $0.00"
        "\n\tMisc = $0.00"
        "\n\tRetirement = $0.00"
        "\n\tTOTAL = $0.00"
        "\n----------------------------------------"
        "\nReimbursements:"
        "\n\tBills = $0.00"
        "\n\tCredit Card Rewards = $0.00"
        "\n\tFree Spending = $0.00"
        "\n\tRent = $0.00"
        "\n\tTOTAL = $0.00"
        "\n----------------------------------------"
        "\nTOTAL SPENDING = $0.00"
        "\nSURPLUS = $0.00"
        "\n****************************************"
    )

    @pytest.mark.parametrize(
        "budget_spending,expected_value",
        [
            (test_budget_spending_obj_deficit, True),
            (test_budget_spending_obj_surplus, True),
            (empty_budget_spending_obj, False),
        ],
    )
    def test_categories_property(self, budget_spending, expected_value):
        """Tests BudgetSpending.categories property."""

        categories = budget_spending.categories

        assert len(categories) == 5
        assert "needs" in categories
        assert isinstance(categories["needs"], Needs)
        assert "wants" in categories
        assert isinstance(categories["wants"], Wants)
        assert "savings" in categories
        assert isinstance(categories["savings"], Savings)
        assert "income" in categories
        assert isinstance(categories["income"], Income)
        assert "reimbursements" in categories
        assert isinstance(categories["reimbursements"], Reimbursements)

    @pytest.mark.parametrize(
        "budget_spending,expected_value",
        [
            (test_budget_spending_obj_deficit, Decimal("4514.61")),
            (test_budget_spending_obj_surplus, Decimal("4414.61")),
            (empty_budget_spending_obj, Decimal("0.00")),
        ],
    )
    def test_total_spending_property(self, budget_spending, expected_value):
        """Tests BudgetSpending.total_spending property."""

        assert budget_spending.total_spending == expected_value

    @pytest.mark.parametrize(
        "budget_spending,expected_value",
        [
            (test_budget_spending_obj_deficit, Decimal("3211.66")),
            (test_budget_spending_obj_surplus, Decimal("5000.00")),
            (empty_budget_spending_obj, Decimal("0.00")),
        ],
    )
    def test_total_income_property(self, budget_spending, expected_value):
        """Tests BudgetSpending.total_income property."""

        assert budget_spending.total_income == expected_value

    @pytest.mark.parametrize(
        "budget_spending,expected_value",
        [
            (test_budget_spending_obj_deficit, Decimal("-1302.95")),
            (test_budget_spending_obj_surplus, Decimal("585.39")),
            (empty_budget_spending_obj, Decimal("0.00")),
        ],
    )
    def test_deficit_or_surplus_property(self, budget_spending, expected_value):
        """Tests BudgetSpending.deficit_or_surplus property."""

        assert budget_spending.deficit_or_surplus == expected_value

    @pytest.mark.parametrize(
        "budget_spending,expected_value",
        [
            (test_budget_spending_obj_deficit, False),
            (test_budget_spending_obj_surplus, False),
            (empty_budget_spending_obj, True),
        ],
    )
    def test_all_zeroes_property(self, budget_spending, expected_value):
        """Tests BudgetSpending.all_zeroes property."""

        assert budget_spending.all_zeroes == expected_value

    @pytest.mark.parametrize(
        "budget_spending,expected_value",
        [
            (test_budget_spending_obj_deficit, test_budget_spending_obj_deficit_str),
            (test_budget_spending_obj_surplus, test_budget_spending_obj_surplus_str),
            (empty_budget_spending_obj, empty_budget_spending_obj_str),
        ],
    )
    def test_to_str(self, budget_spending, expected_value):
        """Tests that BudgetSpending.__str__() is overwritten and returns correct values."""

        assert str(budget_spending) == expected_value
