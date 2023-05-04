from src.analysis import SpendingAnalyzer
from src.categorize_data import perform_data_compilation


def main():
    budget_dict = perform_data_compilation()

    # At this point, we can do whatever data analysis we'd like
    analyzer = SpendingAnalyzer(budget_dict)

    print(budget_dict["2023"]["April"])
    print(analyzer.averages["2021"]["needs"]["rent"])
    print(analyzer.averages["2022"]["needs"]["rent"])
    print(analyzer.averages["2023"]["needs"]["rent"])
    print(analyzer.averages["lifetime"]["needs"]["rent"])


if __name__ == "__main__":
    main()
