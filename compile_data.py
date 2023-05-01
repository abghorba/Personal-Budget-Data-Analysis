import pandas as pd
from clean_tsv_data import clean_data, CLEANED_TSV_FILEPATH
from budget_items import BudgetSpending


def load_data_to_dataframe(verbose=False):
    """
    Cleans the data from spending.tsv and loads into a DataFrame object.

    :param verbose: True to print out the DataFrame; False otherwise.
    :return: DataFrame object containing the data from cleaned_spending.tsv.
    """

    if clean_data():
        raise RuntimeError("Something went wrong when trying to clean the data!")

    df = pd.read_table(CLEANED_TSV_FILEPATH, sep="\t")

    df['Date'] = pd.to_datetime(df['Date'], format='%m/%d/%Y')
    df['Gains/Expenses'] = pd.to_numeric(df['Gains/Expenses'])
    df['Checking Balance'] = pd.to_numeric(df['Checking Balance'])

    if verbose:
        print(df)

    return df


def categorize_spending(spending_df, date_range=["1/1/2021, 1/1/2022"]):
    """

    :param spending_df: DataFrame object containing the data from cleaned_spending.tsv
    :param date_range: [minimum date to include, maximum date to exclude]
    :return: BudgetSpending object
    """

    budget = BudgetSpending()
    filtered_spending_df = spending_df[(spending_df["Date"] >= date_range[0]) & (spending_df["Date"] < date_range[1])]

    for index, transaction in filtered_spending_df.iterrows():

        if transaction["Category"] == "Needs":
            pass

        elif transaction["Category"] == "Wants":
            pass

        elif transaction["Category"] == "Savings":
            pass


def main():

    spending_df = load_data_to_dataframe(verbose=False)
    date_range = ["4/1/2023", "5/1/2023"]
    categorize_spending(spending_df, date_range)

if __name__ == "__main__":
    main()
