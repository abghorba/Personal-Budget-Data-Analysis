from src.analysis import SpendingAnalyzer
from src.categorize_data import perform_data_compilation


def main():
    budget_dict = perform_data_compilation()

    # At this point, we can do whatever data analysis we'd like
    analyzer = SpendingAnalyzer(budget_dict)

    print("\nAverages:")
    print(analyzer.analysis["2021"]["needs"]["rent"]["average"])
    print(analyzer.analysis["2022"]["needs"]["rent"]["average"])
    print(analyzer.analysis["2023"]["needs"]["rent"]["average"])
    print(analyzer.analysis["lifetime"]["needs"]["rent"]["average"])

    print("\nMedians:")
    print(analyzer.analysis["2021"]["needs"]["rent"]["median"])
    print(analyzer.analysis["2022"]["needs"]["rent"]["median"])
    print(analyzer.analysis["2023"]["needs"]["rent"]["median"])
    print(analyzer.analysis["lifetime"]["needs"]["rent"]["median"])

    print("\nVariances:")
    print(analyzer.analysis["2021"]["needs"]["rent"]["variance"])
    print(analyzer.analysis["2022"]["needs"]["rent"]["variance"])
    print(analyzer.analysis["2023"]["needs"]["rent"]["variance"])
    print(analyzer.analysis["lifetime"]["needs"]["rent"]["variance"])

    print("\nStandard Deviations:")
    print(analyzer.analysis["2021"]["needs"]["rent"]["standard_deviation"])
    print(analyzer.analysis["2022"]["needs"]["rent"]["standard_deviation"])
    print(analyzer.analysis["2023"]["needs"]["rent"]["standard_deviation"])
    print(analyzer.analysis["lifetime"]["needs"]["rent"]["standard_deviation"])

    print("\nRegression Coefficients:")
    print(analyzer.analysis["2021"]["needs"]["rent"]["linear_regression_coefficients"])
    print(analyzer.analysis["2022"]["needs"]["rent"]["linear_regression_coefficients"])
    print(analyzer.analysis["2023"]["needs"]["rent"]["linear_regression_coefficients"])
    print(analyzer.analysis["lifetime"]["needs"]["rent"]["linear_regression_coefficients"])

    print("\nSome Expected Values:")
    print(analyzer.get_expected_value("2025", "May", "lifetime", "needs", "rent"))
    print(analyzer.get_expected_value("2022", "June", "lifetime", "needs", "rent"))


if __name__ == "__main__":
    main()
