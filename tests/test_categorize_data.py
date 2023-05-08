import json
import os
from datetime import datetime

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
from tests.utilities import (
    DATE_RANGE_DICT_SPENDING1,
    DATE_RANGE_DICT_SPENDING2,
    DATE_RANGE_DICT_SPENDING3,
    EXPECTED_TEST_SPENDING_FILE1,
    EXPECTED_TEST_SPENDING_FILE2,
    EXPECTED_TEST_SPENDING_FILE3,
    TEST_CLEAN_TSV_FILE,
    TEST_SPENDING_FILE,
    TEST_TSV_FILE1,
    TEST_TSV_FILE2,
    TEST_TSV_FILE3,
    get_expected_budget_dict1,
    get_expected_budget_dict2,
    get_expected_budget_dict3,
    get_expected_budget_spending1,
    get_expected_budget_spending2,
    get_expected_budget_spending3,
)


@pytest.fixture(autouse=True)
def remove_test_files():
    yield
    if os.path.exists(TEST_CLEAN_TSV_FILE):
        os.remove(TEST_CLEAN_TSV_FILE)
    if os.path.exists(TEST_SPENDING_FILE):
        os.remove(TEST_SPENDING_FILE)


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

    @pytest.mark.parametrize("raw_filepath", [TEST_TSV_FILE1, TEST_TSV_FILE2, TEST_TSV_FILE3])
    def test_load_data_to_dataframe(self, raw_filepath):
        """Tests load_data_to_dataframe() correctly loads the cleaned TSV file into a pandas.DataFrame."""

        df = load_data_to_dataframe(raw_filepath, TEST_CLEAN_TSV_FILE)
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

    @pytest.mark.parametrize("raw_filepath", [TEST_TSV_FILE1])
    def test_categorize_needs_transaction(self, raw_filepath):
        """Tests categorize_needs_transaction() parses a Needs transaction correctly."""

        df = load_data_to_dataframe(raw_filepath, TEST_CLEAN_TSV_FILE)
        budget_spending = BudgetSpending()

        # Set up expected BudgetSpending instance
        expected_budget_spending = BudgetSpending()

        if raw_filepath == TEST_TSV_FILE1:
            expected_budget_spending.needs = get_expected_budget_spending1().needs

        elif raw_filepath == TEST_TSV_FILE2:
            expected_budget_spending.needs = get_expected_budget_spending2().needs

        else:
            expected_budget_spending.needs = get_expected_budget_spending3().needs

        for index, transaction in df.iterrows():
            category = transaction["Category"]

            if category == "Needs":
                categorize_needs_transaction(transaction, budget_spending)

        print(budget_spending)

        assert budget_spending == expected_budget_spending

    @pytest.mark.parametrize("raw_filepath", [TEST_TSV_FILE1])
    def test_categorize_wants_transaction(self, raw_filepath):
        """Tests categorize_wants_transaction() parses a Wants transaction correctly."""

        df = load_data_to_dataframe(raw_filepath, TEST_CLEAN_TSV_FILE)
        budget_spending = BudgetSpending()

        # Set up expected BudgetSpending instance
        expected_budget_spending = BudgetSpending()

        if raw_filepath == TEST_TSV_FILE1:
            expected_budget_spending.wants = get_expected_budget_spending1().wants

        elif raw_filepath == TEST_TSV_FILE2:
            expected_budget_spending.wants = get_expected_budget_spending2().wants

        else:
            expected_budget_spending.wants = get_expected_budget_spending3().wants

        for index, transaction in df.iterrows():
            category = transaction["Category"]

            if category == "Wants":
                categorize_wants_transaction(transaction, budget_spending)

        assert budget_spending == expected_budget_spending

    @pytest.mark.parametrize("raw_filepath", [TEST_TSV_FILE1])
    def test_categorize_savings_transaction(self, raw_filepath):
        """Tests categorize_savings_transaction() parses a Savings transaction correctly."""

        df = load_data_to_dataframe(raw_filepath, TEST_CLEAN_TSV_FILE)
        budget_spending = BudgetSpending()

        # Set up expected BudgetSpending instance
        expected_budget_spending = BudgetSpending()

        if raw_filepath == TEST_TSV_FILE1:
            expected_budget_spending.savings = get_expected_budget_spending1().savings

        elif raw_filepath == TEST_TSV_FILE2:
            expected_budget_spending.savings = get_expected_budget_spending2().savings

        else:
            expected_budget_spending.savings = get_expected_budget_spending3().savings

        for index, transaction in df.iterrows():
            category = transaction["Category"]

            if category == "Savings":
                categorize_savings_transaction(transaction, budget_spending)

        assert budget_spending == expected_budget_spending

    @pytest.mark.parametrize("raw_filepath", [TEST_TSV_FILE1])
    def test_categorize_income_transaction(self, raw_filepath):
        """Tests categorize_income_transaction() parses an Income transaction correctly."""

        df = load_data_to_dataframe(raw_filepath, TEST_CLEAN_TSV_FILE)
        budget_spending = BudgetSpending()

        # Set up expected BudgetSpending instance
        expected_budget_spending = BudgetSpending()

        if raw_filepath == TEST_TSV_FILE1:
            expected_budget_spending.income = get_expected_budget_spending1().income
            expected_budget_spending.reimbursements = get_expected_budget_spending1().reimbursements

        elif raw_filepath == TEST_TSV_FILE2:
            expected_budget_spending.income = get_expected_budget_spending2().income
            expected_budget_spending.reimbursements = get_expected_budget_spending2().reimbursements

        else:
            expected_budget_spending.income = get_expected_budget_spending3().income
            expected_budget_spending.reimbursements = get_expected_budget_spending3().reimbursements

        for index, transaction in df.iterrows():
            category = transaction["Category"]

            if category == "Income":
                categorize_income_transaction(transaction, budget_spending)

        assert budget_spending == expected_budget_spending

    @pytest.mark.parametrize(
        "raw_filepath,date_ranges,year,month,budget_df,expected_budget_spending",
        [
            (TEST_TSV_FILE1, DATE_RANGE_DICT_SPENDING1, "2023", "April", pd.DataFrame(), None),
            (TEST_TSV_FILE1, {}, "2023", "April", None, None),
            (TEST_TSV_FILE1, {"May 2023": ("05/01/2023", "06/01/2023")}, "2023", "April", None, None),
            (
                TEST_TSV_FILE1,
                {"April 2023": ("04/01/2023", "05/01/2023"), "May 2023": ("05/01/2023", "06/01/2023")},
                "2023",
                "May",
                None,
                None,
            ),
            (
                TEST_TSV_FILE1,
                DATE_RANGE_DICT_SPENDING1,
                "2023",
                "April",
                None,
                get_expected_budget_spending1(),
            ),
            (
                TEST_TSV_FILE1,
                {"April 2023": ("04/01/2023", "05/01/2023"), "January 2030": ("01/01/2030", "02/01/2030")},
                "2023",
                "April",
                None,
                get_expected_budget_spending1(),
            ),
            (
                TEST_TSV_FILE2,
                DATE_RANGE_DICT_SPENDING2,
                "2022",
                "November",
                None,
                get_expected_budget_spending2(),
            ),
            (
                TEST_TSV_FILE3,
                DATE_RANGE_DICT_SPENDING3,
                "2021",
                "June",
                None,
                get_expected_budget_spending3(),
            ),
        ],
    )
    def test_categorize_transactions(self, raw_filepath, date_ranges, year, month, budget_df, expected_budget_spending):
        """Tests categorize_income_transaction() parses all transactions correctly."""

        if budget_df is None:
            budget_df = load_data_to_dataframe(raw_filepath, TEST_CLEAN_TSV_FILE)

        budget_spending = categorize_transactions(budget_df, date_ranges, year=year, month=month)
        assert expected_budget_spending == budget_spending

    @pytest.mark.parametrize(
        "raw_filepath,expected_budget_dict",
        [
            (TEST_TSV_FILE1, get_expected_budget_dict1()),
            (TEST_TSV_FILE2, get_expected_budget_dict2()),
            (TEST_TSV_FILE3, get_expected_budget_dict3()),
        ],
    )
    def test_compile_transactions_into_dictionary(self, raw_filepath, expected_budget_dict):
        """Tests compile_transactions_into_dictionary() parses all transactions into a dictionary correctly."""

        df = load_data_to_dataframe(raw_filepath, TEST_CLEAN_TSV_FILE)
        budget_dict = compile_transactions_into_dictionary(df)

        for year in expected_budget_dict.keys():
            for month in expected_budget_dict[year].keys():
                assert (
                    budget_dict[year][month] == expected_budget_dict[year][month]
                ), f"{month} {year}\n {budget_dict[year][month]}"

    @pytest.mark.parametrize(
        "raw_filepath,expected_budget_dict",
        [
            (TEST_TSV_FILE1, get_expected_budget_dict1()),
            (TEST_TSV_FILE2, get_expected_budget_dict2()),
            (TEST_TSV_FILE3, get_expected_budget_dict3()),
        ],
    )
    def test_compile_transactions_into_dictionary_multithreading(self, raw_filepath, expected_budget_dict):
        """Tests compile_transactions_into_dictionary(use_threading=True) parses all transactions into a
        dictionary correctly."""

        df = load_data_to_dataframe(raw_filepath, TEST_CLEAN_TSV_FILE)
        budget_dict = compile_transactions_into_dictionary(df, use_threading=True)

        for year in expected_budget_dict.keys():
            for month in expected_budget_dict[year].keys():
                assert budget_dict[year][month] == expected_budget_dict[year][month]

    @pytest.mark.parametrize(
        "raw_filepath,expected_budget_dict",
        [
            (TEST_TSV_FILE1, get_expected_budget_dict1()),
            (TEST_TSV_FILE2, get_expected_budget_dict2()),
            (TEST_TSV_FILE3, get_expected_budget_dict3()),
        ],
    )
    def test_compile_transactions_into_dictionary_multiprocessing(self, raw_filepath, expected_budget_dict):
        """Tests compile_transactions_into_dictionary(use_multithreading=True) parses all transactions into a
        dictionary correctly."""

        df = load_data_to_dataframe(raw_filepath, TEST_CLEAN_TSV_FILE)
        budget_dict = compile_transactions_into_dictionary(df, use_multiprocessing=True)

        for year in expected_budget_dict.keys():
            for month in expected_budget_dict[year].keys():
                assert budget_dict[year][month] == expected_budget_dict[year][month]

    @pytest.mark.parametrize(
        "raw_filepath,expected_spending_txt_filepath",
        [
            (TEST_TSV_FILE1, EXPECTED_TEST_SPENDING_FILE1),
            (TEST_TSV_FILE2, EXPECTED_TEST_SPENDING_FILE2),
            (TEST_TSV_FILE3, EXPECTED_TEST_SPENDING_FILE3),
        ],
    )
    def test_save_spending_data_as_text_file(self, raw_filepath, expected_spending_txt_filepath):
        """Verifies that save_spending_data_as_text_file() correctly writes data to a new file."""

        df = load_data_to_dataframe(raw_filepath, TEST_CLEAN_TSV_FILE)
        budget_dict = compile_transactions_into_dictionary(df)
        save_spending_data_as_text_file(budget_dict, TEST_SPENDING_FILE)

        assert os.path.exists(TEST_SPENDING_FILE)
        assert os.path.getsize(TEST_SPENDING_FILE) > 0

        with open(expected_spending_txt_filepath, "r") as expected_file:
            with open(TEST_SPENDING_FILE, "r") as test_file:
                assert test_file.readlines() == expected_file.readlines()
