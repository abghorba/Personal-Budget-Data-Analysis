import os
from decimal import Decimal

import pytest

from src.analysis import SpendingAnalyzer, calculate_predicted_value, calculate_regression_coefficients
from src.categorize_data import perform_data_compilation
from tests.utilities import (
    TEST_CLEAN_TSV_FILE,
    TEST_SPENDING_FILE,
    TEST_TSV_FILE1,
    TEST_TSV_FILE2,
    TEST_TSV_FILE3,
    get_expected_analysis_dict1,
    get_expected_analysis_dict2,
    get_expected_analysis_dict3,
    get_expected_data_points1,
    get_expected_data_points2,
    get_expected_data_points3,
)


@pytest.fixture(autouse=True)
def remove_test_files():
    yield
    if os.path.exists(TEST_CLEAN_TSV_FILE):
        os.remove(TEST_CLEAN_TSV_FILE)
    if os.path.exists(TEST_SPENDING_FILE):
        os.remove(TEST_SPENDING_FILE)


@pytest.mark.parametrize(
    "data,expected_values",
    [
        ([Decimal("50")], (Decimal("0"), Decimal("0"))),
        ([Decimal("0"), Decimal("0"), Decimal("0"), Decimal("0"), Decimal("0")], (Decimal("0"), Decimal("0"))),
        ([Decimal("10.00"), Decimal("10.00"), Decimal("10.00"), Decimal("10.00")], (Decimal("0"), Decimal("10.00"))),
        ([Decimal("10"), Decimal("8"), Decimal("6")], (Decimal("-2"), Decimal("10"))),
        ([Decimal("1"), Decimal("5"), Decimal("9.00"), Decimal("13"), Decimal("17.00")], (Decimal("4"), Decimal("1"))),
        (
            [
                Decimal("111.11"),
                Decimal("333.33"),
                Decimal("222.22"),
                Decimal("555.55"),
                Decimal("444.44"),
                Decimal("777.77"),
                Decimal("666.66"),
                Decimal("999.99"),
                Decimal("888.88"),
            ],
            (Decimal("103.70"), Decimal("140.75")),
        ),
        (
            [
                Decimal("363.23"),
                Decimal("100.23"),
                Decimal("214.55"),
                Decimal("70.23"),
                Decimal("-311.11"),
                Decimal("226.21"),
                Decimal("214.32"),
                Decimal("-99.92"),
                Decimal("99.95"),
                Decimal("-404.44"),
                Decimal("166.66"),
                Decimal("-266.66"),
                Decimal("-467.88"),
                Decimal("-180.05"),
                Decimal("-231.13"),
            ],
            (Decimal("-37.66"), Decimal("229.90")),
        ),
    ],
)
def test_calculate_regression_coefficients(data, expected_values):
    """Tests calculate_regression_coefficients() correctly calculates the least-squares coefficients."""

    assert calculate_regression_coefficients(data) == expected_values


@pytest.mark.parametrize(
    "x_coordinate,slope,y_intercept,expected_value",
    [
        (Decimal("0"), Decimal("0"), Decimal("0"), Decimal("0")),
        (Decimal("10"), Decimal("0"), Decimal("10.00"), Decimal("10.00")),
        (Decimal("50"), Decimal("-2"), Decimal("10"), Decimal("-90")),
        (Decimal("100"), Decimal("103.70"), Decimal("140.75"), Decimal("10510.75")),
        (Decimal("-50"), Decimal("-37.66"), Decimal("229.90"), Decimal("2112.90")),
    ],
)
def test_calculate_predicted_value(x_coordinate, slope, y_intercept, expected_value):
    """Tests calculate_predicted_value() correctly calculates value of the line given by the slope and y_intercept at
    the point x_coordinate."""

    assert calculate_predicted_value(x_coordinate, slope, y_intercept) == expected_value


class TestSpendingAnalyzer:
    @pytest.mark.parametrize(
        "raw_filepath,expected_data_points_dict",
        [
            (TEST_TSV_FILE1, get_expected_data_points1()),
            (TEST_TSV_FILE2, get_expected_data_points2()),
            (TEST_TSV_FILE3, get_expected_data_points3()),
        ],
    )
    def test_gather_all_data_points(self, raw_filepath, expected_data_points_dict):
        """Tests SpendingAnalyzer._gather_all_data_points() compiles the data points correctly."""

        budget_dict = perform_data_compilation(
            raw_filepath=raw_filepath, cleaned_filepath=TEST_CLEAN_TSV_FILE, cleaned_txt_filepath=TEST_SPENDING_FILE
        )
        analyzer = SpendingAnalyzer(budget_dict)

        assert analyzer._data_points == expected_data_points_dict

    @pytest.mark.parametrize(
        "raw_filepath,expected_analysis_dict",
        [
            (TEST_TSV_FILE1, get_expected_analysis_dict1()),
            (TEST_TSV_FILE2, get_expected_analysis_dict2()),
            (TEST_TSV_FILE3, get_expected_analysis_dict3()),
        ],
    )
    def test_get_analysis(self, raw_filepath, expected_analysis_dict):
        budget_dict = perform_data_compilation(
            raw_filepath=raw_filepath, cleaned_filepath=TEST_CLEAN_TSV_FILE, cleaned_txt_filepath=TEST_SPENDING_FILE
        )
        analyzer = SpendingAnalyzer(budget_dict)

        assert analyzer.analysis == expected_analysis_dict

    @pytest.mark.parametrize(
        "year,month,timeframe,expected_value",
        [
            ("2021", "March", "lifetime", 0),
            ("2021", "March", "2021", 0),
            ("2022", "January", "2022", 0),
            ("2023", "January", "2023", 0),
            ("2023", "January", "2022", 12),
            ("2022", "January", "lifetime", 10),
            ("2023", "January", "lifetime", 22),
            ("2020", "April", "lifetime", -11),
            ("2020", "April", "lifetime", -11),
            ("2025", "April", "lifetime", 49),
            ("2025", "April", "2023", 27),
        ],
    )
    def test_get_x_coordinate_for_month_and_year(self, year, month, timeframe, expected_value):
        """Tests SpendingAnalyzer.get_x_coordinate_for_month_and_year() calculates the x_coordinate pertaining to
        the requested month."""

        budget_dict = perform_data_compilation(
            raw_filepath=TEST_TSV_FILE3, cleaned_filepath=TEST_CLEAN_TSV_FILE, cleaned_txt_filepath=TEST_SPENDING_FILE
        )
        analyzer = SpendingAnalyzer(budget_dict)

        assert analyzer.get_x_coordinate_for_month_and_year(year, month, timeframe) == expected_value

    @pytest.mark.parametrize(
        "year,month,timeframe,expected_value1,expected_value2,expected_value3",
        [
            ("2021", "March", "lifetime", Decimal("677.15"), Decimal("1212.42"), Decimal("51.28")),
            ("2023", "January", "2022", Decimal("2406.76"), Decimal("1209.88"), Decimal("-100.02")),
            ("2022", "January", "lifetime", Decimal("1326.85"), Decimal("1151.02"), Decimal("151.78")),
            ("2020", "April", "lifetime", Decimal("-37.52"), Decimal("1279.96"), Decimal("-59.27")),
            ("2025", "April", "lifetime", Decimal("3860.68"), Decimal("911.56"), Decimal("543.73")),
        ],
    )
    def test_get_expected_value(self, year, month, timeframe, expected_value1, expected_value2, expected_value3):
        """Tests SpendingAnalyzer.get_expected_value() calculates the expected value for the month using the linear
        regression coefficients."""

        budget_dict = perform_data_compilation(
            raw_filepath=TEST_TSV_FILE3, cleaned_filepath=TEST_CLEAN_TSV_FILE, cleaned_txt_filepath=TEST_SPENDING_FILE
        )
        analyzer = SpendingAnalyzer(budget_dict)

        assert (
            analyzer.get_expected_value(year, month, timeframe, category="needs", subcategory="rent") == expected_value1
        )
        assert (
            analyzer.get_expected_value(year, month, timeframe, category="wants", subcategory="free_spending")
            == expected_value2
        )
        assert (
            analyzer.get_expected_value(year, month, timeframe, category="savings", subcategory="retirement")
            == expected_value3
        )
