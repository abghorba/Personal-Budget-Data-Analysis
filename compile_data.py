import pandas as pd
import os
from clean_tsv_data import clean_data, CLEANED_TSV_FILEPATH


def main():

    if clean_data():
        raise RuntimeError("Something went wrong when trying to clean the data!")

    df = pd.read_table(CLEANED_TSV_FILEPATH, sep="\t")
    print(df)

if __name__ == "__main__":
    main()
