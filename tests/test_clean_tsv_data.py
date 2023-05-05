import os
import random
from datetime import datetime
from decimal import Decimal

import pytest

from src.clean_tsv_data import clean_data, clean_tsv_file, export_cleaned_data_to_tsv

INVALID_PATH = os.getcwd() + "/tests/files/invalid.tsv"
TEST_TSV_FILE = os.getcwd() + "/tests/files/spending.tsv"
TEST_CLEAN_TSV_FILE = os.getcwd() + "/tests/files/cleaned_spending.tsv"


@pytest.fixture(autouse=True)
def remove_clean_tsv_file_after_test():
    yield
    if os.path.exists(TEST_CLEAN_TSV_FILE):
        os.remove(TEST_CLEAN_TSV_FILE)


class TestCleanTSVData:
    def test_clean_tsv_file(self):
        """Verifies that clean_tsv_file() cleans a raw spending.tsv correctly."""

        tsv_file_contents = clean_tsv_file(raw_filepath=TEST_TSV_FILE)

        assert isinstance(tsv_file_contents, list)

        # Check the header line
        header_line = tsv_file_contents[0]
        assert not header_line[0].isspace()
        assert not header_line[-1].isspace()

        header_line = header_line.split("\t")
        assert len(header_line) == 7
        assert header_line[0] == "Description"
        assert header_line[1] == "Category"
        assert header_line[2] == "Subcategory"
        assert header_line[3] == "Payment"
        assert header_line[4] == "Date"
        assert header_line[5] == "Gains/Expenses"
        assert header_line[6] == "Checking Balance"

        # Check this beginning balance line
        beginning_balance_line = tsv_file_contents[1]
        assert not beginning_balance_line[0].isspace()
        assert not beginning_balance_line[-1].isspace()

        beginning_balance_line = beginning_balance_line.split("\t")
        assert len(beginning_balance_line) == 7
        assert beginning_balance_line[0] == "Beginning Balance"
        assert beginning_balance_line[1] == "None"
        assert beginning_balance_line[2] == "None"
        assert beginning_balance_line[3] == "None"
        assert beginning_balance_line[4] == "2/28/2021"
        assert beginning_balance_line[5] == "1317.17"
        assert beginning_balance_line[6] == "1317.17"

        # Check random lines
        for iteration in range(100):
            random_index = random.randint(2, len(tsv_file_contents) - 1)
            random_line = tsv_file_contents[random_index]
            assert not random_line[0].isspace()
            assert not random_line[-1].isspace()

            random_line = random_line.split("\t")
            assert len(random_line) == 7

            for index, entry in enumerate(random_line):
                assert not entry[0].isspace()
                assert not entry[-1].isspace()

                # Date entry
                if index == 4:
                    # Ensure the entry is in the correct format and can be type-casted to datetime object
                    datetime.strptime(entry, "%m/%d/%Y")

                # Monetary entries
                if index in [5, 6]:
                    assert "$" not in entry
                    assert "," not in entry
                    assert "(" not in entry
                    assert ")" not in entry

                    # Ensure this entry can be type-casted to a Decimal
                    Decimal(entry)

    def test_export_cleaned_data_to_tsv(self):
        """Verifies that export_cleaned_data_to_tsv() correctly writes data to a new file."""

        tsv_file_contents = clean_tsv_file(raw_filepath=TEST_TSV_FILE)
        export_cleaned_data_to_tsv(tsv_file_contents, cleaned_tsv_filepath=TEST_CLEAN_TSV_FILE)

        assert os.path.exists(TEST_CLEAN_TSV_FILE)
        assert os.path.getsize(TEST_CLEAN_TSV_FILE) > 0

        with open(TEST_CLEAN_TSV_FILE, "r") as file:
            clean_tsv_file_contents = file.readlines()

            for index, line in enumerate(clean_tsv_file_contents):
                assert tsv_file_contents[index] == line.strip("\n")

    @pytest.mark.parametrize(
        "raw_filepath,cleaned_tsv_filepath,expected_value",
        [
            (INVALID_PATH, TEST_CLEAN_TSV_FILE, True),
            (TEST_TSV_FILE, "", True),
            (TEST_TSV_FILE, TEST_CLEAN_TSV_FILE, False),
        ],
    )
    def test_clean_data(self, raw_filepath, cleaned_tsv_filepath, expected_value):
        """Verifies that clean_data() correctly returns True if there is a failure, and False if successful."""

        assert clean_data(raw_filepath=raw_filepath, cleaned_tsv_filepath=cleaned_tsv_filepath) == expected_value
