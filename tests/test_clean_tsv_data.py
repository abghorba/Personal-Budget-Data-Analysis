import os
import random
from datetime import datetime
from decimal import Decimal

import pytest

from src.clean_tsv_data import clean_data, clean_tsv_file, export_cleaned_data_to_tsv
from tests.utilities import (
    EXPECTED_CLEANED_TSV_FILE1,
    EXPECTED_CLEANED_TSV_FILE2,
    EXPECTED_CLEANED_TSV_FILE3,
    INVALID_PATH,
    TEST_CLEAN_TSV_FILE,
    TEST_TSV_FILE1,
    TEST_TSV_FILE2,
    TEST_TSV_FILE3,
)


@pytest.fixture(autouse=True)
def remove_test_files():
    yield
    if os.path.exists(TEST_CLEAN_TSV_FILE):
        os.remove(TEST_CLEAN_TSV_FILE)


class TestCleanTSVData:
    @pytest.mark.parametrize("raw_filepath", [TEST_TSV_FILE1, TEST_TSV_FILE2, TEST_TSV_FILE3])
    def test_clean_tsv_file(self, raw_filepath):
        """Verifies that clean_tsv_file() cleans a raw spending.tsv correctly."""

        tsv_file_contents = clean_tsv_file(raw_filepath=raw_filepath)

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

        # Check the beginning balance line
        beginning_balance_line = tsv_file_contents[1]
        assert not beginning_balance_line[0].isspace()
        assert not beginning_balance_line[-1].isspace()

        beginning_balance_line = beginning_balance_line.split("\t")
        assert len(beginning_balance_line) == 7
        assert beginning_balance_line[0] == "Beginning Balance"
        assert beginning_balance_line[1] == "None"
        assert beginning_balance_line[2] == "None"
        assert beginning_balance_line[3] == "None"

        if raw_filepath == TEST_TSV_FILE1:
            assert beginning_balance_line[4] == "4/1/2023"
            assert beginning_balance_line[5] == "2500.00"
            assert beginning_balance_line[6] == "2500.00"

        elif raw_filepath == TEST_TSV_FILE2:
            assert beginning_balance_line[4] == "1/1/2022"
            assert beginning_balance_line[5] == "2277.01"
            assert beginning_balance_line[6] == "2277.01"

        elif raw_filepath == TEST_TSV_FILE3:
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

    @pytest.mark.parametrize(
        "raw_filepath,expected_clean_tsv_filepath",
        [
            (TEST_TSV_FILE1, EXPECTED_CLEANED_TSV_FILE1),
            (TEST_TSV_FILE2, EXPECTED_CLEANED_TSV_FILE2),
            (TEST_TSV_FILE3, EXPECTED_CLEANED_TSV_FILE3),
        ],
    )
    def test_export_cleaned_data_to_tsv(self, raw_filepath, expected_clean_tsv_filepath):
        """Verifies that export_cleaned_data_to_tsv() correctly writes data to a new file."""

        tsv_file_contents = clean_tsv_file(raw_filepath=raw_filepath)
        export_cleaned_data_to_tsv(tsv_file_contents, cleaned_tsv_filepath=TEST_CLEAN_TSV_FILE)

        assert os.path.exists(TEST_CLEAN_TSV_FILE)
        assert os.path.getsize(TEST_CLEAN_TSV_FILE) > 0

        with open(expected_clean_tsv_filepath, "r") as expected_file:
            with open(TEST_CLEAN_TSV_FILE, "r") as test_file:
                assert test_file.readlines() == expected_file.readlines()

    @pytest.mark.parametrize(
        "raw_filepath,cleaned_tsv_filepath,expected_value",
        [
            (INVALID_PATH, TEST_CLEAN_TSV_FILE, True),
            (TEST_TSV_FILE1, "", True),
            (TEST_TSV_FILE1, TEST_CLEAN_TSV_FILE, False),
            (TEST_TSV_FILE2, TEST_CLEAN_TSV_FILE, False),
            (TEST_TSV_FILE3, TEST_CLEAN_TSV_FILE, False),
        ],
    )
    def test_clean_data(self, raw_filepath, cleaned_tsv_filepath, expected_value):
        """Verifies that clean_data() correctly returns True if there is a failure, and False if successful."""

        assert clean_data(raw_filepath=raw_filepath, cleaned_tsv_filepath=cleaned_tsv_filepath) == expected_value
