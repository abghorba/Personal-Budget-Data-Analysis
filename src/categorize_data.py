import pandas as pd

from src.budget_items import BudgetSpending
from src.clean_tsv_data import CLEANED_TSV_FILEPATH, clean_data


def load_data_to_dataframe(verbose=False):
    """
    Cleans the data from spending.tsv and loads into a DataFrame object.

    :param verbose: True to print out the DataFrame; False otherwise.
    :return: DataFrame object containing the data from cleaned_spending.tsv.
    """

    if clean_data():
        raise RuntimeError("Something went wrong when trying to clean the data!")

    df = pd.read_table(CLEANED_TSV_FILEPATH, sep="\t")

    df["Date"] = pd.to_datetime(df["Date"], format="%m/%d/%Y")
    df["Gains/Expenses"] = abs(pd.to_numeric(df["Gains/Expenses"]))
    df["Checking Balance"] = pd.to_numeric(df["Checking Balance"])

    if verbose:
        print(df)

    return df


def categorize_needs_spending(budget_df, budget_spending_obj):
    """
    Categorizes the "Needs" transactions in the given spending DataFrame and records results in the given
    BudgetSpending instance.

    :param budget_df:
    :param budget_spending_obj:
    :return: Nothing, the information is stored in budget_spending_obj
    """

    for index, transaction in budget_df.iterrows():
        category = transaction["Category"]
        subcategory = transaction["Subcategory"]
        description = transaction["Description"]
        amount = transaction["Gains/Expenses"]

        if category == "Needs":
            if subcategory == "Bills":
                if description == "Car Insurance":
                    budget_spending_obj.needs.car_insurance += amount

                elif description in ["ECSI Loans", "Federal Loans"]:
                    budget_spending_obj.needs.student_loans += amount

                elif description == "Electric Bill":
                    budget_spending_obj.needs.electric_bill += amount

                elif description in ["Federal Taxes", "Tax Preparation Fee"]:
                    budget_spending_obj.needs.taxes += amount

                elif description == "Internet Bill":
                    budget_spending_obj.needs.internet_bill += amount

                elif description == "Rent":
                    budget_spending_obj.needs.rent += amount

                elif description == "Renter's Insurance":
                    budget_spending_obj.needs.renters_insurance += amount

                else:
                    print(f"{description} is not a known Needs > Bills description, adding to Misc.")
                    budget_spending_obj.needs.misc += amount

            elif subcategory == "Emergency":
                budget_spending_obj.needs.emergencies += amount

            elif subcategory == "Gas":
                budget_spending_obj.needs.gasoline += amount

            elif subcategory == "Groceries":
                budget_spending_obj.needs.groceries += amount

            elif subcategory == "Laundry":
                budget_spending_obj.needs.laundry += amount

            else:
                print(f"{subcategory} not a known Needs subcategory, adding to Misc.")
                budget_spending_obj.needs.misc += amount


def categorize_wants_spending(budget_df, budget_spending_obj):
    """
    Categorizes the "Wants" transactions in the given spending DataFrame and records results in the given
    BudgetSpending instance.

    :param budget_df:
    :param budget_spending_obj:
    :return: Nothing, the information is stored in budget_spending_obj
    """

    for index, transaction in budget_df.iterrows():
        category = transaction["Category"]
        subcategory = transaction["Subcategory"]
        description = transaction["Description"]
        amount = transaction["Gains/Expenses"]

        if category == "Wants":
            if subcategory == "Free Spending":
                budget_spending_obj.wants.free_spending += amount

            elif subcategory == "Subscriptions":
                budget_spending_obj.wants.subscriptions += amount

            elif subcategory == "Vacation Spending":
                budget_spending_obj.wants.vacation_spending += amount

            else:
                print(f"{subcategory} not a known Wants subcategory, adding to Misc.")
                budget_spending_obj.wants.misc += amount


def categorize_savings_spending(budget_df, budget_spending_obj):
    """
    Categorizes the "Savings" transactions in the given spending DataFrame and records results in the given
    BudgetSpending instance.

    :param budget_df:
    :param budget_spending_obj:
    :return: Nothing, the information is stored in budget_spending_obj
    """

    for index, transaction in budget_df.iterrows():
        category = transaction["Category"]
        subcategory = transaction["Subcategory"]
        description = transaction["Description"]
        amount = transaction["Gains/Expenses"]

        if category == "Savings":
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


def categorize_income(budget_df, budget_spending_obj):
    """
    Categorizes the "Income" transactions in the given spending DataFrame and records results in the given
    BudgetSpending instance.

    :param budget_df:
    :param budget_spending_obj:
    :return: Nothing, the information is stored in budget_spending_obj
    """

    for index, transaction in budget_df.iterrows():
        category = transaction["Category"]
        subcategory = transaction["Subcategory"]
        description = transaction["Description"]
        amount = transaction["Gains/Expenses"]

        if category == "Income":
            if subcategory == "Earnings":
                budget_spending_obj.income.earnings += amount

            elif subcategory == "Tax Return":
                budget_spending_obj.income.tax_returns += amount

            elif subcategory == "Rewards":
                budget_spending_obj.income.rewards += amount


def categorize_data(budget_df, date_range_start="1/1/2022", date_range_end="1/1/2023"):
    """
    Categorizes spending/income data into their respective Category classes in a BudgetSpending instance.

    :param budget_df: DataFrame object containing the data from cleaned_spending.tsv
    :param date_range_start: Start date (inclusive) to filter by
    :param date_range_end: End date (exclusive) to filter by
    :return: BudgetSpending instance
    """

    budget_spending = BudgetSpending()

    # Restrict the DataFrame to the specified date range
    budget_df = budget_df[(budget_df["Date"] >= date_range_start) & (budget_df["Date"] < date_range_end)]

    # No need for Placeholders
    budget_df = budget_df[(budget_df["Subcategory"] != "Placeholder")]

    categorize_needs_spending(budget_df, budget_spending)
    categorize_wants_spending(budget_df, budget_spending)
    categorize_savings_spending(budget_df, budget_spending)
    categorize_income(budget_df, budget_spending)

    return budget_spending


def main():
    budget_df = load_data_to_dataframe(verbose=True)
    date_range_start = "4/1/2023"
    date_range_end = "5/1/2023"
    budget_spending = categorize_data(budget_df, date_range_start, date_range_end)

    print(budget_spending)


if __name__ == "__main__":
    main()
