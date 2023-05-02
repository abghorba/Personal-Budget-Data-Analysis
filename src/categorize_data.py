import pandas as pd

from src.budget_items import BudgetSpending
from src.clean_tsv_data import CLEANED_TSV_FILEPATH, clean_data


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

    df = pd.read_table(CLEANED_TSV_FILEPATH, sep="\t")

    df["Date"] = pd.to_datetime(df["Date"], format="%m/%d/%Y")
    df["Gains/Expenses"] = abs(pd.to_numeric(df["Gains/Expenses"]))
    df["Checking Balance"] = pd.to_numeric(df["Checking Balance"])

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
    amount = transaction["Gains/Expenses"]

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
    amount = transaction["Gains/Expenses"]

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
    amount = transaction["Gains/Expenses"]

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
    amount = transaction["Gains/Expenses"]

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


def categorize_data(budget_df, date_range_start="1/1/2022", date_range_end="1/1/2023", verbose=False):
    """
    Categorizes spending/income data into their respective Category classes in a BudgetSpending instance.

    :param budget_df: DataFrame object containing the data from cleaned_spending.tsv
    :param date_range_start: Start date (inclusive) to filter by
    :param date_range_end: End date (exclusive) to filter by
    :param verbose: True to print extra logging; False otherwise
    :return: BudgetSpending instance
    """

    budget_spending = BudgetSpending()

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
