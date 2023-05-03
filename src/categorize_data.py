import os
import time
from datetime import datetime, timedelta
from decimal import Decimal

import pandas as pd

from src.budget_items import BudgetSpending
from src.clean_tsv_data import CLEANED_TSV_FILEPATH, clean_data

SPENDING_DATA_TXT_FILEPATH = os.getcwd() + "/data/spending_data.txt"
YEARS = ["2021", "2022", "2023"]
MONTHS = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]


def get_first_day_of_next_month(input_dt):
    """
    For a given datetime object, return the 1st of the next month.

    :param input_dt: Datetime object
    :return: Datetime object representing the 1st of next month
    """

    # Replace day number with 1
    input_dt = input_dt.replace(day=1)

    # Add 32 days to the input datetime
    input_dt = input_dt + timedelta(days=32)

    # Replace day number with 1
    first_of_next_month = input_dt.replace(day=1)

    return first_of_next_month


def load_data_to_dataframe(verbose=False):
    """
    Cleans the data from spending.tsv and loads into a DataFrame object.

    :param verbose: True to print out the DataFrame; False otherwise.
    :return: DataFrame object containing the data from cleaned_spending.tsv.
    """

    if not isinstance(verbose, bool):
        raise TypeError("verbose is not a bool type")

    if clean_data():
        raise RuntimeError("Something went wrong when trying to clean the data!")

    print("Creating pandas DataFrame with cleaned data")

    df = pd.read_table(CLEANED_TSV_FILEPATH, sep="\t", dtype=str)

    df["Date"] = pd.to_datetime(df["Date"], format="%m/%d/%Y")

    if verbose:
        print(df)

    return df


def categorize_needs_spending(transaction, budget_spending_obj, verbose=False):
    """
    Categorizes the "Needs" transactions in the given spending DataFrame and records results in the given
    BudgetSpending instance.

    :param transaction: Row from the Budget DataFrame
    :param budget_spending_obj: BudgetSpending instance
    :param verbose: True to print extra logging; False otherwise
    :return: Nothing, the information is parsed into budget_spending_obj.needs
    """

    if not isinstance(transaction, pd.Series):
        raise TypeError("transaction is not a pandas.Series instance")

    if not isinstance(budget_spending_obj, BudgetSpending):
        raise TypeError("budget_spending_obj is not a BudgetSpending instance")

    if not isinstance(verbose, bool):
        raise TypeError("verbose is not a bool type")

    category = transaction["Category"]
    subcategory = transaction["Subcategory"]
    description = transaction["Description"]
    amount = Decimal(transaction["Gains/Expenses"])

    if verbose:
        print(f"Categorizing {description} transaction on {transaction['Date']}")

    if category != "Needs":
        raise RuntimeError("Not a Needs row!")

    if subcategory == "Car Insurance":
        budget_spending_obj.needs.car_insurance += amount

    elif subcategory == "Electric Bill":
        budget_spending_obj.needs.electric_bill += amount

    elif subcategory == "Emergency":
        budget_spending_obj.needs.emergencies += amount

    elif subcategory == "Gas":
        budget_spending_obj.needs.gasoline += amount

    elif subcategory == "Groceries":
        budget_spending_obj.needs.groceries += amount

    elif subcategory == "Internet Bill":
        budget_spending_obj.needs.internet_bill += amount

    elif subcategory == "Rent":
        budget_spending_obj.needs.rent += amount

    elif subcategory == "Renter's Insurance":
        budget_spending_obj.needs.renters_insurance += amount

    elif subcategory == "Student Loans":
        budget_spending_obj.needs.student_loans += amount

    elif subcategory == "Taxes":
        budget_spending_obj.needs.student_loans += amount

    elif subcategory == "Laundry":
        budget_spending_obj.needs.laundry += amount

    elif subcategory == "Misc.":
        budget_spending_obj.needs.misc += amount

    else:
        print(f"{subcategory} not a known Needs subcategory, adding to Misc.")
        budget_spending_obj.needs.misc += amount


def categorize_wants_spending(transaction, budget_spending_obj, verbose=False):
    """
    Categorizes the "Wants" transactions in the given spending DataFrame and records results in the given
    BudgetSpending instance.

    :param transaction: Row from the Budget DataFrame
    :param budget_spending_obj: BudgetSpending instance
    :param verbose: True to print extra logging; False otherwise
    :return: Nothing, the information is parsed into budget_spending_obj.wants
    """

    if not isinstance(transaction, pd.Series):
        raise TypeError("transaction is not a pandas.Series instance")

    if not isinstance(budget_spending_obj, BudgetSpending):
        raise TypeError("budget_spending_obj is not a BudgetSpending instance")

    if not isinstance(verbose, bool):
        raise TypeError("verbose is not a bool type")

    category = transaction["Category"]
    subcategory = transaction["Subcategory"]
    description = transaction["Description"]
    amount = Decimal(transaction["Gains/Expenses"])

    if verbose:
        print(f"Categorizing {description} transaction on {transaction['Date']}")

    if category != "Wants":
        raise RuntimeError("Not a Wants row!")

    if subcategory == "Free Spending":
        budget_spending_obj.wants.free_spending += amount

    elif subcategory == "Subscriptions":
        budget_spending_obj.wants.subscriptions += amount

    elif subcategory == "Vacation Spending":
        budget_spending_obj.wants.vacation_spending += amount

    else:
        print(f"{subcategory} not a known Wants subcategory, adding to Misc.")
        budget_spending_obj.wants.misc += amount


def categorize_savings_spending(transaction, budget_spending_obj, verbose=False):
    """
    Categorizes the "Savings" transactions in the given spending DataFrame and records results in the given
    BudgetSpending instance.

    :param transaction: Row from the Budget DataFrame
    :param budget_spending_obj: BudgetSpending instance
    :param verbose: True to print extra logging; False otherwise
    :return: Nothing, the information is parsed into budget_spending_obj.savings
    """

    if not isinstance(transaction, pd.Series):
        raise TypeError("transaction is not a pandas.Series instance")

    if not isinstance(budget_spending_obj, BudgetSpending):
        raise TypeError("budget_spending_obj is not a BudgetSpending instance")

    if not isinstance(verbose, bool):
        raise TypeError("verbose is not a bool type")

    category = transaction["Category"]
    subcategory = transaction["Subcategory"]
    description = transaction["Description"]
    amount = Decimal(transaction["Gains/Expenses"])

    if verbose:
        print(f"Categorizing {description} transaction on {transaction['Date']}")

    if category != "Savings":
        raise RuntimeError("Not a Savings row!")

    if subcategory == "Crypto Savings":
        budget_spending_obj.savings.crypto += amount

    elif subcategory == "Emergency Savings":
        budget_spending_obj.savings.emergency_fund += amount

    elif subcategory == "Retirement":
        budget_spending_obj.savings.retirement += amount

    elif subcategory == "Taxable Brokerage":
        budget_spending_obj.savings.investing += amount

    else:
        print(f"{subcategory} not a known Savings subcategory, adding to Misc.")
        budget_spending_obj.savings.misc += amount


def categorize_income(transaction, budget_spending_obj, verbose=False):
    """
    Categorizes the "Income" transactions in the given transaction and parses results into the given
    BudgetSpending instance.

    :param transaction:
    :param budget_spending_obj:
    :param verbose: True to print extra logging; False otherwise
    :return: Nothing, the information is stored in budget_spending_obj.income and
             budget_spending_obj.reimbursements
    """

    if not isinstance(transaction, pd.Series):
        raise TypeError("transaction is not a pandas.Series instance")

    if not isinstance(budget_spending_obj, BudgetSpending):
        raise TypeError("budget_spending_obj is not a BudgetSpending instance")

    if not isinstance(verbose, bool):
        raise TypeError("verbose is not a bool type")

    category = transaction["Category"]
    subcategory = transaction["Subcategory"]
    description = transaction["Description"]
    amount = Decimal(transaction["Gains/Expenses"])

    if verbose:
        print(f"Categorizing {description} transaction on {transaction['Date']}")

    if category != "Income":
        raise RuntimeError("Not an Income row!")

    if subcategory == "Earnings":
        budget_spending_obj.income.earnings += amount

    elif subcategory == "Tax Return":
        budget_spending_obj.income.tax_returns += amount

    elif subcategory == "Reimbursements":
        if description == "Bill Reimbursement":
            budget_spending_obj.reimbursements.bills += amount

        elif "CC" in description:
            budget_spending_obj.reimbursements.credit_card_rewards += amount

        elif description == "Rent":
            budget_spending_obj.reimbursements.rent += amount

        else:
            budget_spending_obj.reimbursements.free_spending += amount

    else:
        print(f"No known {subcategory} Income subcategory.")


def categorize_data(budget_df, name="", date_range_start="1/1/2022", date_range_end="1/1/2023", verbose=False):
    """
    Categorizes spending/income data into their respective Category classes in a BudgetSpending instance.

    :param budget_df: DataFrame object containing the data from cleaned_spending.tsv
    :param name: Name of the BudgetSpending instance
    :param date_range_start: Start date (inclusive) to filter by
    :param date_range_end: End date (exclusive) to filter by
    :param verbose: True to print extra logging; False otherwise
    :return: BudgetSpending instance
    """

    print(f"Categorizing each transaction for {name}")

    budget_spending = BudgetSpending(name)

    # Restrict the DataFrame to the specified date range
    budget_df = budget_df[(budget_df["Date"] >= date_range_start) & (budget_df["Date"] < date_range_end)]

    # No need for Placeholders
    budget_df = budget_df[(budget_df["Subcategory"] != "Placeholder")]

    for index, transaction in budget_df.iterrows():
        category = transaction["Category"]

        if category == "Needs":
            categorize_needs_spending(transaction, budget_spending, verbose=verbose)

        elif category == "Wants":
            categorize_wants_spending(transaction, budget_spending, verbose=verbose)

        elif category == "Savings":
            categorize_savings_spending(transaction, budget_spending, verbose=verbose)

        elif category == "Income":
            categorize_income(transaction, budget_spending, verbose=verbose)

    return budget_spending


def compile_all_spending(years=None, months=None):
    """
    Compiles all the spending and loads the information into a dictionary.

    :param years: List of strings containing the year. Ex. ["2021", "2022"]
    :param months: List of strings containing month names. Ex. ["January", "April", "May"]
    :return: Dictionary containing BudgetSpending instances formatted as
             dict[year][month] --> BudgetSpending
    """

    if months is None:
        months = MONTHS

    if years is None:
        years = YEARS

    budget_df = load_data_to_dataframe(verbose=False)
    budget_dict = {}

    # For each month and year, categorize the spending as dict[year][month] --> BudgetSpending object
    for year in years:
        budget_dict[year] = {}

        for month in months:
            today = datetime.now()
            date_string = f"{month} {year}"
            range_start = datetime.strptime(date_string, "%B %Y")

            # Skip any future time frames
            if range_start.month >= today.month and range_start.year >= today.year:
                continue

            range_end = get_first_day_of_next_month(range_start)

            # Format the dates
            date_range_start = range_start.strftime("%m/%d/%Y")
            date_range_end = range_end.strftime("%m/%d/%Y")

            budget_dict[year][month] = categorize_data(budget_df, date_string, date_range_start, date_range_end)

    print("Each transaction has been categorized for all specified months and years")

    return budget_dict


def save_spending_data_as_text_file(budget_dict):
    """
    For a given Budget Dictionary, saves the data into a human-readable text file.

    :param budget_dict: Dictionary containing monthly budget spending
    :return: None; Output located in spending_data.txt
    """

    print(f"Saving categorized data into .txt file at {SPENDING_DATA_TXT_FILEPATH}")

    with open(SPENDING_DATA_TXT_FILEPATH, "w") as file:
        for year in budget_dict:
            for month in budget_dict[year]:
                file.write(str(budget_dict[year][month]) + "\n")

    # Wait a couple seconds for the file to be written
    time.sleep(3)
