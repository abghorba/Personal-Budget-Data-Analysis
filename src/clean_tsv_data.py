import os

RAW_TSV_FILEPATH = os.getcwd() + "/data/spending.tsv"
CLEANED_TSV_FILEPATH = os.getcwd() + "/data/cleaned_spending.tsv"


def clean_tsv_file():
    """
    Reads the spending.tsv file and cleans it.

    :return: Returns the cleaned data as a list of TSV lines.
    """

    print(f"Cleaning raw data file {RAW_TSV_FILEPATH}")

    cleaned_tsv_lines = []

    # Import raw data as a TSV file
    with open(RAW_TSV_FILEPATH, "r") as file:
        spending_file = file.readlines()

        for line_index, line in enumerate(spending_file):
            current_line = line.replace("\t", "", 1).split("\t")[:7]
            cleaned_line = []

            for item_index, item in enumerate(current_line):
                item = item.strip()

                # Everything on index 7 and beyond is junk
                if item_index >= 7:
                    break

                # These are monetary values and need extra cleaning
                if item_index in [5, 6] and line_index >= 1:
                    # Placeholder value, just convert to 0
                    if "-" in item:
                        item = "0"

                    # Not a placeholder value, so remove unnecessary characters
                    else:
                        item = item.replace("$", "").replace(",", "").replace("(", "").replace(")", "").strip()

                cleaned_line.append(item)

            assert len(cleaned_line) == 7
            cleaned_tsv_lines.append("\t".join(cleaned_line))

        assert len(cleaned_tsv_lines) == len(spending_file)
        cleaned_tsv_lines.pop()

    return cleaned_tsv_lines


def export_cleaned_data_to_tsv(cleaned_tsv_lines_list):
    """
    Exports the cleaned TSV lines list as cleaned_spending.tsv file.

    :param cleaned_tsv_lines_list: Cleaned list of TSV lines.
    :return: None
    """

    print(f"Exporting the cleaned data to {CLEANED_TSV_FILEPATH}")

    # Export cleaned data into CSV format
    with open(CLEANED_TSV_FILEPATH, "w") as file:
        for line in cleaned_tsv_lines_list:
            file.write(line + "\n")


def clean_data():
    """
    Driver function to clean the spending.tsv file and export it as cleaned_spending.tsv file.

    :return: True if failure; False otherwise.
    """

    try:
        cleaned_tsv_lines = clean_tsv_file()
        export_cleaned_data_to_tsv(cleaned_tsv_lines_list=cleaned_tsv_lines)
        return os.path.getsize(CLEANED_TSV_FILEPATH) == 0

    except Exception as e:
        print(str(e))
        return True
