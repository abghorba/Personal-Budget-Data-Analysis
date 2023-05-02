import os
from datetime import datetime, timedelta

from src.categorize_data import categorize_data, load_data_to_dataframe

SPENDING_DATA_TXT_FILEPATH = os.getcwd() + "/data/spending_data.txt"


def get_first_day_of_next_month(input_dt):
    """
    For a given datetime object, return the 1st of the next month.

    :param input_dt: Datetime object
    :return: Datetime object representing the 1st of next menth
    """

    # Replace day number with 1
    input_dt = input_dt.replace(day=1)

    # Add 32 days to the input datetime
    input_dt = input_dt + timedelta(days=32)

    # Replace day number with 1
    first_of_next_month = input_dt.replace(day=1)

    return first_of_next_month


def compile_all_spending():
    """
    Compiles all the spending and loads the information into a dictionary.

    :return: Dictionary containing BudgetSpending instances formatted as
             dict[year][month] --> BudgetSpending
    """

    budget_df = load_data_to_dataframe(verbose=False)

    # dict[year][month] --> BudgetSpending object
    budget_dict = {
        "2021": {
            "January": None,
            "February": None,
            "March": None,
            "April": None,
            "May": None,
            "June": None,
            "July": None,
            "August": None,
            "September": None,
            "October": None,
            "November": None,
            "December": None,
        },
        "2022": {
            "January": None,
            "February": None,
            "March": None,
            "April": None,
            "May": None,
            "June": None,
            "July": None,
            "August": None,
            "September": None,
            "October": None,
            "November": None,
            "December": None,
        },
        "2023": {
            "January": None,
            "February": None,
            "March": None,
            "April": None,
            "May": None,
            "June": None,
            "July": None,
            "August": None,
            "September": None,
            "October": None,
            "November": None,
            "December": None,
        },
    }

    # For each month, categorize the spending
    for year in budget_dict:
        for month in budget_dict[year]:
            date_string = f"{month} {year}"
            range_start = datetime.strptime(date_string, "%B %Y")
            range_end = get_first_day_of_next_month(range_start)

            # Format the dates
            date_range_start = range_start.strftime("%m/%d/%Y")
            date_range_end = range_end.strftime("%m/%d/%Y")

            # print(f"START = {range_start}, END = {range_end}")
            budget_dict[year][month] = categorize_data(budget_df, date_range_start, date_range_end)

    return budget_dict


def save_spending_data_as_text_file(budget_dict):
    """
    For a given Budget Dictionary, saves the data into a human-readable text file.

    :param budget_dict: Dictionary containing monthly budget spending
    :return: None; Output located in spending_data.txt
    """

    with open(SPENDING_DATA_TXT_FILEPATH, "w") as file:
        for year in budget_dict:
            for month in budget_dict[year]:
                date_string = f"{month} {year}"
                file.write(date_string + "\n")
                file.write(str(budget_dict[year][month]) + "\n")


def main():
    budget_dict = compile_all_spending()
    save_spending_data_as_text_file(budget_dict)

    # At this point, we can do whatever data analysis we'd like
    for year in budget_dict:
        for month in budget_dict[year]:
            pass


if __name__ == "__main__":
    main()
