import os
from datetime import datetime
from decimal import Decimal

import pandas as pd
import pytest

from src.budget_items import BudgetSpending
from src.categorize_data import (
    categorize_income_transaction,
    categorize_needs_transaction,
    categorize_savings_transaction,
    categorize_transactions,
    categorize_wants_transaction,
    compile_transactions_into_dictionary,
    get_date_ranges,
    get_first_day_of_next_month,
    load_data_to_dataframe,
    save_spending_data_as_text_file,
)

INVALID_PATH = os.getcwd() + "/tests/files/invalid.tsv"
TEST_TSV_FILE = os.getcwd() + "/tests/files/spending.tsv"
TEST_TSV_FILE2 = os.getcwd() + "/tests/files/spending2.tsv"
TEST_CLEAN_TSV_FILE = os.getcwd() + "/tests/files/cleaned_spending.tsv"
TEST_SPENDING_FILE = os.getcwd() + "/tests/files/spending.txt"


@pytest.fixture(autouse=True)
def remove_clean_tsv_file_after_test():
    yield
    if os.path.exists(TEST_CLEAN_TSV_FILE):
        os.remove(TEST_CLEAN_TSV_FILE)
    if os.path.exists(TEST_SPENDING_FILE):
        os.remove(TEST_SPENDING_FILE)


def get_expected_budget_spending2():
    """Returns the expected BudgetSpending instance from /tests/files/spending2.tsv"""
    expected_budget_spending = BudgetSpending("April 2023")
    expected_budget_spending.needs.car_insurance = Decimal("145.60")
    expected_budget_spending.needs.dental_insurance = Decimal("0.00")
    expected_budget_spending.needs.electric_bill = Decimal("16.35")
    expected_budget_spending.needs.emergencies = Decimal("125.99")
    expected_budget_spending.needs.gasoline = Decimal("68.32")
    expected_budget_spending.needs.groceries = Decimal("389.44")
    expected_budget_spending.needs.health_insurance = Decimal("0.00")
    expected_budget_spending.needs.internet_bill = Decimal("69.99")
    expected_budget_spending.needs.laundry = Decimal("0.00")
    expected_budget_spending.needs.misc = Decimal("251.98")
    expected_budget_spending.needs.mortgage = Decimal("0.00")
    expected_budget_spending.needs.other_insurance = Decimal("0.00")
    expected_budget_spending.needs.rent = Decimal("2000.00")
    expected_budget_spending.needs.renters_insurance = Decimal("68.32")
    expected_budget_spending.needs.student_loans = Decimal("145.60")
    expected_budget_spending.needs.taxes = Decimal("400.00")
    expected_budget_spending.needs.vision_insurance = Decimal("0.00")
    expected_budget_spending.wants.free_spending = Decimal("235.93")
    expected_budget_spending.wants.misc = Decimal("44.44")
    expected_budget_spending.wants.subscriptions = Decimal("28.98")
    expected_budget_spending.wants.vacation_spending = Decimal("444.44")
    expected_budget_spending.savings.crypto = Decimal("110.00")
    expected_budget_spending.savings.emergency_fund = Decimal("200.00")
    expected_budget_spending.savings.investing = Decimal("100.00")
    expected_budget_spending.savings.misc = Decimal("55.55")
    expected_budget_spending.savings.retirement = Decimal("700.00")
    expected_budget_spending.income.earnings = Decimal("6000.00")
    expected_budget_spending.income.tax_returns = Decimal("500.00")
    expected_budget_spending.reimbursements.bills = Decimal("40.00")
    expected_budget_spending.reimbursements.credit_card_rewards = Decimal("13.99")
    expected_budget_spending.reimbursements.free_spending = Decimal("45.60")
    expected_budget_spending.reimbursements.rent = Decimal("1000.00")
    return expected_budget_spending


class TestCategorizeData:
    @pytest.mark.parametrize(
        "date,expected_date",
        [
            (datetime(2023, 4, 1), datetime(2023, 5, 1)),
            (datetime(2022, 12, 25), datetime(2023, 1, 1)),
            (datetime(2021, 11, 30), datetime(2021, 12, 1)),
            (datetime(2020, 2, 29), datetime(2020, 3, 1)),
            (datetime(2020, 1, 31), datetime(2020, 2, 1)),
        ],
    )
    def test_get_first_day_of_next_month(self, date, expected_date):
        """Tests get_first_day_of_next_month() returns correct the datetime object representing the 1st day of
        the next month."""

        assert get_first_day_of_next_month(date) == expected_date

    @pytest.mark.parametrize(
        "years,months,expected_ranges",
        [
            (
                None,
                None,
                {
                    "January 2021": ("01/01/2021", "02/01/2021"),
                    "February 2021": ("02/01/2021", "03/01/2021"),
                    "March 2021": ("03/01/2021", "04/01/2021"),
                    "April 2021": ("04/01/2021", "05/01/2021"),
                    "May 2021": ("05/01/2021", "06/01/2021"),
                    "June 2021": ("06/01/2021", "07/01/2021"),
                    "July 2021": ("07/01/2021", "08/01/2021"),
                    "August 2021": ("08/01/2021", "09/01/2021"),
                    "September 2021": ("09/01/2021", "10/01/2021"),
                    "October 2021": ("10/01/2021", "11/01/2021"),
                    "November 2021": ("11/01/2021", "12/01/2021"),
                    "December 2021": ("12/01/2021", "01/01/2022"),
                    "January 2022": ("01/01/2022", "02/01/2022"),
                    "February 2022": ("02/01/2022", "03/01/2022"),
                    "March 2022": ("03/01/2022", "04/01/2022"),
                    "April 2022": ("04/01/2022", "05/01/2022"),
                    "May 2022": ("05/01/2022", "06/01/2022"),
                    "June 2022": ("06/01/2022", "07/01/2022"),
                    "July 2022": ("07/01/2022", "08/01/2022"),
                    "August 2022": ("08/01/2022", "09/01/2022"),
                    "September 2022": ("09/01/2022", "10/01/2022"),
                    "October 2022": ("10/01/2022", "11/01/2022"),
                    "November 2022": ("11/01/2022", "12/01/2022"),
                    "December 2022": ("12/01/2022", "01/01/2023"),
                    "January 2023": ("01/01/2023", "02/01/2023"),
                    "February 2023": ("02/01/2023", "03/01/2023"),
                    "March 2023": ("03/01/2023", "04/01/2023"),
                    "April 2023": ("04/01/2023", "05/01/2023"),
                },
            ),  # Use default values
            (
                ["2020"],
                ["January", "March", "December"],
                {
                    "January 2020": ("01/01/2020", "02/01/2020"),
                    "March 2020": ("03/01/2020", "04/01/2020"),
                    "December 2020": ("12/01/2020", "01/01/2021"),
                },
            ),
            (
                ["2021", "2022"],
                ["December", "June", "January"],
                {
                    "December 2021": ("12/01/2021", "01/01/2022"),
                    "June 2021": ("06/01/2021", "07/01/2021"),
                    "January 2021": ("01/01/2021", "02/01/2021"),
                    "December 2022": ("12/01/2022", "01/01/2023"),
                    "June 2022": ("06/01/2022", "07/01/2022"),
                    "January 2022": ("01/01/2022", "02/01/2022"),
                },
            ),
            (
                ["2021", "2025"],
                ["December", "January", "June"],
                {
                    "December 2021": ("12/01/2021", "01/01/2022"),
                    "January 2021": ("01/01/2021", "02/01/2021"),
                    "June 2021": ("06/01/2021", "07/01/2021"),
                },
            ),
            (["2030"], ["January"], {}),
        ],
    )
    def test_get_date_ranges(self, years, months, expected_ranges):
        """Tests get_date_ranges() correctly returns a dictionary of tuples representing the start date and the end date
        in format MM/DD/YYYY."""

        assert get_date_ranges(years, months) == expected_ranges

    def test_load_data_to_dataframe(self):
        """Tests load_data_to_dataframe() correctly loads the cleaned TSV file into a pandas.DataFrame."""

        df = load_data_to_dataframe(TEST_TSV_FILE, TEST_CLEAN_TSV_FILE)
        assert isinstance(df, pd.DataFrame)

        with open(TEST_CLEAN_TSV_FILE, "r") as file:
            df_rows, df_cols = df.shape

            # The header line in the tsv file becomes the column names in the DataFrame, so there is 1 less row
            assert df_rows == len(file.readlines()) - 1
            assert df_cols == 7

        assert isinstance(df["Description"][2], str)
        assert isinstance(df["Category"][2], str)
        assert isinstance(df["Subcategory"][2], str)
        assert isinstance(df["Payment"][2], str)
        assert isinstance(df["Date"][2], pd.Timestamp)
        assert isinstance(df["Gains/Expenses"][2], str)
        assert isinstance(df["Checking Balance"][2], str)

    def test_categorize_needs_transaction(self):
        """Tests categorize_needs_transaction() parses a Needs transaction correctly."""

        df = load_data_to_dataframe(TEST_TSV_FILE2, TEST_CLEAN_TSV_FILE)
        budget_spending = BudgetSpending()

        # Set up expected BudgetSpending instance
        expected_budget_spending = BudgetSpending()
        expected_budget_spending.needs = get_expected_budget_spending2().needs

        for index, transaction in df.iterrows():
            category = transaction["Category"]

            if category == "Needs":
                categorize_needs_transaction(transaction, budget_spending)

        print(budget_spending)

        assert budget_spending == expected_budget_spending

    def test_categorize_wants_transaction(self):
        """Tests categorize_wants_transaction() parses a Wants transaction correctly."""

        df = load_data_to_dataframe(TEST_TSV_FILE2, TEST_CLEAN_TSV_FILE)
        budget_spending = BudgetSpending()

        # Set up expected BudgetSpending instance
        expected_budget_spending = BudgetSpending()
        expected_budget_spending.wants = get_expected_budget_spending2().wants

        for index, transaction in df.iterrows():
            category = transaction["Category"]

            if category == "Wants":
                categorize_wants_transaction(transaction, budget_spending)

        assert budget_spending == expected_budget_spending

    def test_categorize_savings_transaction(self):
        """Tests categorize_savings_transaction() parses a Savings transaction correctly."""

        df = load_data_to_dataframe(TEST_TSV_FILE2, TEST_CLEAN_TSV_FILE)
        budget_spending = BudgetSpending()

        # Set up expected BudgetSpending instance
        expected_budget_spending = BudgetSpending()
        expected_budget_spending.savings = get_expected_budget_spending2().savings

        for index, transaction in df.iterrows():
            category = transaction["Category"]

            if category == "Savings":
                categorize_savings_transaction(transaction, budget_spending)

        assert budget_spending == expected_budget_spending

    def test_categorize_income_transaction(self):
        """Tests categorize_income_transaction() parses an Income transaction correctly."""

        df = load_data_to_dataframe(TEST_TSV_FILE2, TEST_CLEAN_TSV_FILE)
        budget_spending = BudgetSpending()

        # Set up expected BudgetSpending instance
        expected_budget_spending = BudgetSpending()
        expected_budget_spending.income = get_expected_budget_spending2().income
        expected_budget_spending.reimbursements = get_expected_budget_spending2().reimbursements

        for index, transaction in df.iterrows():
            category = transaction["Category"]

            if category == "Income":
                categorize_income_transaction(transaction, budget_spending)

        assert budget_spending == expected_budget_spending

    def test_categorize_transactions(self):
        """Tests categorize_income_transaction() parses all transactions correctly."""

        df = load_data_to_dataframe(TEST_TSV_FILE2, TEST_CLEAN_TSV_FILE)
        date_ranges = {"April 2023": ("04/01/2023", "05/01/2023"), "January 2030": ("01/01/2030", "02/01/2030")}

        # Check that passing in an empty DataFrame returns None
        assert categorize_transactions(pd.DataFrame(), date_ranges) is None

        # Check that supplying dates that have no data returns None
        assert categorize_transactions(df, date_ranges, year="2030", month="January") is None

        expected_budget_spending = get_expected_budget_spending2()
        budget_spending = categorize_transactions(df, date_ranges, year="2023", month="April")

        assert expected_budget_spending == budget_spending

    def test_compile_transactions_into_dictionary(self):
        """Tests compile_transactions_into_dictionary() parses all transactions into a dictionary correctly."""

        df = load_data_to_dataframe(TEST_TSV_FILE2, TEST_CLEAN_TSV_FILE)
        budget_dict = compile_transactions_into_dictionary(df)
        expected_budget_spending = get_expected_budget_spending2()
        assert budget_dict["2023"]["April"] == expected_budget_spending

    def test_compile_transactions_into_dictionary_multithreading(self):
        """Tests compile_transactions_into_dictionary(use_threading=True) parses all transactions into a
        dictionary correctly."""

        df = load_data_to_dataframe(TEST_TSV_FILE2, TEST_CLEAN_TSV_FILE)
        budget_dict = compile_transactions_into_dictionary(df, use_threading=True)
        expected_budget_spending = get_expected_budget_spending2()
        assert budget_dict["2023"]["April"] == expected_budget_spending

    def test_compile_transactions_into_dictionary_multiprocessing(self):
        """Tests compile_transactions_into_dictionary(use_multithreading=True) parses all transactions into a
        dictionary correctly."""

        df = load_data_to_dataframe(TEST_TSV_FILE2, TEST_CLEAN_TSV_FILE)
        budget_dict = compile_transactions_into_dictionary(df, use_multiprocessing=True)
        expected_budget_spending = get_expected_budget_spending2()
        assert budget_dict["2023"]["April"] == expected_budget_spending

    def test_save_spending_data_as_text_file(self):
        """Verifies that save_spending_data_as_text_file() correctly writes data to a new file."""

        df = load_data_to_dataframe(TEST_TSV_FILE2, TEST_CLEAN_TSV_FILE)
        budget_dict = compile_transactions_into_dictionary(df)
        save_spending_data_as_text_file(budget_dict, TEST_SPENDING_FILE)

        assert os.path.exists(TEST_SPENDING_FILE)
        assert os.path.getsize(TEST_SPENDING_FILE) > 0

        with open(TEST_SPENDING_FILE, "r") as file:
            file_contents = file.readlines()
            assert str(budget_dict["2023"]["April"]) + "\n" == "".join(file_contents)
