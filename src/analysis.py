from decimal import Decimal


class SpendingAnalyzer:
    def __init__(self, budget_dict):
        self.budget_dict = budget_dict
        self.averages = self.get_averages()

    def get_averages(self):
        """
        Gets the lifetime and yearly averages per category and compiles into a dict.

        averages = {
            "lifetime": {
                "category": {
                    "subcategory": float
                }
            },
            "year": {
                "category": {
                    "subcategory": float
                }
            }
        }

        :return: Dict of averages
        """

        # Initialize the dictionary
        averages = {"lifetime": {}}
        lifetime_data_points = Decimal("0.00")

        for year in self.budget_dict:
            averages.update({year: {}})
            yearly_data_points = Decimal("0.00")

            for month in self.budget_dict[year]:
                lifetime_data_points += 1
                yearly_data_points += 1
                budget_spending = self.budget_dict[year][month]

                for category_name in budget_spending.categories.keys():
                    if category_name not in averages["lifetime"]:
                        averages["lifetime"].update({category_name: {}})

                    if category_name not in averages[year]:
                        averages[year].update({category_name: {}})

                    for subcategory_name, value in budget_spending.categories[category_name].subcategories.items():
                        if subcategory_name not in averages["lifetime"][category_name]:
                            averages["lifetime"][category_name].update({subcategory_name: 0})

                        if subcategory_name not in averages[year][category_name]:
                            averages[year][category_name].update({subcategory_name: 0})

                        averages["lifetime"][category_name][subcategory_name] += Decimal(value)
                        averages[year][category_name][subcategory_name] += Decimal(value)

            for category_name in averages[year].keys():
                for subcategory_name, value in averages[year][category_name].items():
                    averages[year][category_name][subcategory_name] = round(value / yearly_data_points, 2)

        for category_name in averages["lifetime"].keys():
            for subcategory_name, value in averages["lifetime"][category_name].items():
                averages["lifetime"][category_name][subcategory_name] = round(value / lifetime_data_points, 2)

        return averages
