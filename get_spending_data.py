from src.analysis import SpendingAnalyzer
from src.categorize_data import perform_data_compilation


def main():
    budget_dict = perform_data_compilation()

    # At this point, we can do whatever data analysis we'd like
    analyzer = SpendingAnalyzer(budget_dict)

    category = "needs"
    subcategory = "gasoline"

    print(f"\nGetting data for {category.upper()} > {subcategory.upper()}")

    print("\nAverages:")
    print(analyzer.analysis["2021"][category][subcategory]["average"])
    print(analyzer.analysis["2022"][category][subcategory]["average"])
    print(analyzer.analysis["2023"][category][subcategory]["average"])
    print(analyzer.analysis["lifetime"][category][subcategory]["average"])

    print("\nMedians:")
    print(analyzer.analysis["2021"][category][subcategory]["median"])
    print(analyzer.analysis["2022"][category][subcategory]["median"])
    print(analyzer.analysis["2023"][category][subcategory]["median"])
    print(analyzer.analysis["lifetime"][category][subcategory]["median"])

    print("\nVariances:")
    print(analyzer.analysis["2021"][category][subcategory]["variance"])
    print(analyzer.analysis["2022"][category][subcategory]["variance"])
    print(analyzer.analysis["2023"][category][subcategory]["variance"])
    print(analyzer.analysis["lifetime"][category][subcategory]["variance"])

    print("\nStandard Deviations:")
    print(analyzer.analysis["2021"][category][subcategory]["standard_deviation"])
    print(analyzer.analysis["2022"][category][subcategory]["standard_deviation"])
    print(analyzer.analysis["2023"][category][subcategory]["standard_deviation"])
    print(analyzer.analysis["lifetime"][category][subcategory]["standard_deviation"])

    print("\nRegression Coefficients:")
    print(analyzer.analysis["2021"][category][subcategory]["linear_regression_coefficients"])
    print(analyzer.analysis["2022"][category][subcategory]["linear_regression_coefficients"])
    print(analyzer.analysis["2023"][category][subcategory]["linear_regression_coefficients"])
    print(analyzer.analysis["lifetime"][category][subcategory]["linear_regression_coefficients"])

    print("\nSome Expected Values:")
    print(analyzer.get_expected_value("2025", "May", "lifetime", category, subcategory))
    print(analyzer.get_expected_value("2022", "June", "lifetime", category, subcategory))


if __name__ == "__main__":
    main()
