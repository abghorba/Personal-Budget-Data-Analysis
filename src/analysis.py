from datetime import datetime
from decimal import Decimal

import numpy as np

from src.categorize_data import MONTHS, YEARS


def calculate_regression_coefficients(data):
    """
    Calculates the slope and y-intercept of the least squares linear regression line. The data points are assembled as

        0 --> data[0],
        1 --> data[1],
        ...
        n --> data[n]

    :param data: A list of Decimals
    :return: (slope, y_intercept)
    """

    # Need at least two points to make a line
    if len(data) < 2:
        print(
            f"WARNING: Cannot calculate a linear regression coefficient with the provided data of length "
            f"{len(data)}."
        )
        return 0, 0

    x_coordinates = np.array([Decimal(index) for index in range(len(data))])
    y_coordinates = np.array(data)
    number_of_data_points = np.size(x_coordinates)

    # Mean of x and y vector
    mean_x = np.mean(x_coordinates)
    mean_y = np.mean(y_coordinates)

    # Calculate cross-deviation and deviation about x
    sum_cross_deviations_xy = np.sum(y_coordinates * x_coordinates) - number_of_data_points * mean_y * mean_x
    sum_squared_deviations_xx = np.sum(x_coordinates * x_coordinates) - number_of_data_points * mean_x * mean_x

    # Calculate regression coefficients
    slope = round(sum_cross_deviations_xy / sum_squared_deviations_xx, 2)
    y_intercept = round(mean_y - slope * mean_x, 2)

    return slope, y_intercept


def calculate_predicted_value(x_coordinate, slope, y_intercept):
    """
    Given a slope and y_intercept, calculate the value of the y_coordinate with equation:

        y_coordinate = slope * x_coordinate + y_intercept

    :param x_coordinate: Data point to calculate with
    :param slope: Slope of a line
    :param y_intercept: Y-intercept of a line
    :return: y_coordinate
    """

    return slope * x_coordinate + y_intercept


class SpendingAnalyzer:
    def __init__(self, budget_dict):
        self.budget_dict = budget_dict
        self.categories_to_subcategories = {}
        self._data_points = self._gather_all_data_points()
        self.analysis = self.get_analysis()

    def _gather_all_data_points(self):
        """
        Gathers all the data points from the budget_dict.

        data_points = {
            "lifetime": {
                "category": {
                    "subcategory": List of all data points in ascending order by date,
                },
                "first_date": Tuple (year, month)
            },
            "year": {
                "category": {
                    "subcategory": List of all data points in ascending order by date,
                },
                "first_date": Tuple (year, month)
            }
        }

        :return: Dict of data points
        """

        data_points = {"lifetime": {}}

        for year in sorted(self.budget_dict, key=YEARS.index):
            data_points.update({year: {}})

            for month in sorted(self.budget_dict[year], key=MONTHS.index):
                budget_spending = self.budget_dict[year][month]

                if "first_date" not in data_points["lifetime"]:
                    data_points["lifetime"]["first_date"] = (year, month)

                if "first_date" not in data_points[year]:
                    data_points[year]["first_date"] = (year, month)

                for category_name in budget_spending.categories.keys():
                    if category_name not in data_points["lifetime"]:
                        data_points["lifetime"].update({category_name: {}})

                    if category_name not in data_points[year]:
                        data_points[year].update({category_name: {}})

                    for subcategory_name, value in budget_spending.categories[category_name].subcategories.items():
                        if subcategory_name not in data_points["lifetime"][category_name]:
                            data_points["lifetime"][category_name].update({subcategory_name: []})

                        if subcategory_name not in data_points[year][category_name]:
                            data_points[year][category_name].update({subcategory_name: []})

                        data_points["lifetime"][category_name][subcategory_name].append(Decimal(value))
                        data_points[year][category_name][subcategory_name].append(Decimal(value))

        return data_points

    def get_analysis(self):
        """
        Gets all mathematical analysis from the given data points.

        analysis = {
            "lifetime": {
                "category": {
                    "subcategory": {
                        "average": Decimal,
                        "median": Decimal,
                        "variance": Decimal,
                        "standard_deviation: Decimal,
                        "linear_regression_coefficients": (Decimal, Decimal)
                    }
                }
            },
            "year": {
                "category": {
                    "subcategory": {
                        "average": Decimal,
                        "median": Decimal,
                        "variance": Decimal,
                        "standard_deviation: Decimal,
                        "linear_regression_coefficients": (Decimal, Decimal)
                    }
                }
            }
        }

        :return: Dict containing mathematical analyses
        """

        # Initialize the dictionary
        analysis = {}

        for time_period in self._data_points.keys():
            analysis[time_period] = {}

            for category in self._data_points[time_period].keys():
                if category == "first_date":
                    continue

                analysis[time_period][category] = {}

                for subcategory in self._data_points[time_period][category].keys():
                    analysis[time_period][category][subcategory] = {}

                    # Get Averages
                    analysis[time_period][category][subcategory]["average"] = round(
                        np.mean(self._data_points[time_period][category][subcategory]), 2
                    )

                    # Get Medians
                    analysis[time_period][category][subcategory]["median"] = round(
                        np.median(self._data_points[time_period][category][subcategory]), 2
                    )

                    # Get Variances
                    analysis[time_period][category][subcategory]["variance"] = round(
                        np.var(self._data_points[time_period][category][subcategory]), 2
                    )

                    # Get Standard Deviations
                    analysis[time_period][category][subcategory]["standard_deviation"] = round(
                        np.std(self._data_points[time_period][category][subcategory]), 2
                    )

                    # Get Linear Regression Coefficients
                    analysis[time_period][category][subcategory][
                        "linear_regression_coefficients"
                    ] = calculate_regression_coefficients(self._data_points[time_period][category][subcategory])

        return analysis

    def get_x_coordinate_for_month_and_year(self, year, month, timeframe):
        """
        For the given timeframe, calculate the x_coordinate corresponding to the given month and year. The first
        data point in the timeframe corresponds to x = 0.

        If the month and year happen to occur before the first data point, we can expect the x_coordinate to be
        negative. Likewise, if the month and year occurs after the first data point, the x_coordinate should be
        positive.

        :param year: String representing the year in format "YYYY"
        :param month: String with the month name i.e., "January", "February", etc.
        :param timeframe: Timeframe of the data - "lifetime", "2021", "2022", etc. are valid values
        :return: int representing the x_coordinate
        """

        first_year, first_month = self._data_points[timeframe]["first_date"]
        start_date = datetime.strptime(f"{first_month} {first_year}", "%B %Y")
        end_date = datetime.strptime(f"{month} {year}", "%B %Y")
        x_coordinate = (end_date.year - start_date.year) * 12 + (end_date.month - start_date.month)

        return x_coordinate

    def get_expected_value(self, year, month, timeframe, category, subcategory):
        """
        Uses the linear regression coefficients to calculate the expected value at the specified month and year
        for the given timeframe.

        :param year: String representing the year in format "YYYY"
        :param month: String with the month name i.e., "January", "February", etc.
        :param timeframe: Timeframe of the data - "lifetime", "2021", "2022", etc. are valid values
        :param category: String representing the category i.e., "Needs", "Wants", etc.
        :param subcategory: String representing the subcategory i.e., "Rent", "Free Spending", etc.
        :return: Decimal representing the calculated expected value
        """

        if timeframe not in self.analysis:
            raise RuntimeError("Invalid timeframe!")

        if category not in self.analysis[timeframe]:
            raise RuntimeError("Invalid category for the timeframe!")

        if subcategory not in self.analysis[timeframe][category]:
            raise RuntimeError("Invalid subcategory for the category!")

        slope, y_intercept = self.analysis[timeframe][category][subcategory]["linear_regression_coefficients"]
        x_coordinate = self.get_x_coordinate_for_month_and_year(year, month, timeframe)

        return calculate_predicted_value(x_coordinate, slope, y_intercept)
