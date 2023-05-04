from decimal import Decimal

from numpy import mean, median, std, var

from src.categorize_data import MONTHS, YEARS


class SpendingAnalyzer:
    def __init__(self, budget_dict):
        self.budget_dict = budget_dict
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
                    analysis[time_period][category][subcategory]["average"] = round(
                        mean(self._data_points[time_period][category][subcategory]), 2
                    )
                    analysis[time_period][category][subcategory]["median"] = round(
                        median(self._data_points[time_period][category][subcategory]), 2
                    )
                    analysis[time_period][category][subcategory]["variance"] = round(
                        var(self._data_points[time_period][category][subcategory]), 2
                    )
                    analysis[time_period][category][subcategory]["standard_deviation"] = round(
                        std(self._data_points[time_period][category][subcategory]), 2
                    )

        return analysis
