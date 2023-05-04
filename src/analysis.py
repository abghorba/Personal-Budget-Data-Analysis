from decimal import Decimal

import numpy as np

from src.categorize_data import MONTHS, YEARS


def calculate_regression_coefficients(data):
    """
    Calculates the slope and y-intercept of the least squares linear regression line.

    :param data: A list of Decimals
    :return: (slope, y_intercept)
    """

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
        self.months_and_years_analyzed = []
        self._data_points = self._gather_all_data_points()
        self.analysis = self.get_analysis()

    def _gather_all_data_points(self):
        """

        data_points = {
            "lifetime": {
                "category": {
                    "subcategory": List of all data points in ascending order by date
                }
            },
            "year": {
                "category": {
                    "subcategory": List of all data points in ascending order by date
                }
            }
        }

        :return:
        """

        data_points = {"lifetime": {}}

        for year in sorted(self.budget_dict, key=YEARS.index):
            data_points.update({year: {}})

            for month in sorted(self.budget_dict[year], key=MONTHS.index):
                budget_spending = self.budget_dict[year][month]

                self.months_and_years_analyzed.append((year, month))

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
