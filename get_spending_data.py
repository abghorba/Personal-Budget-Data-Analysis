from src.analysis import SpendingAnalyzer
from src.categorize_data import compile_all_spending, save_spending_data_as_text_file


def main():
    budget_dict = compile_all_spending()
    save_spending_data_as_text_file(budget_dict)

    # At this point, we can do whatever data analysis we'd like
    analyzer = SpendingAnalyzer(budget_dict)

    print(analyzer.averages["2021"]["needs"]["rent"])
    print(analyzer.averages["2022"]["needs"]["rent"])
    print(analyzer.averages["2023"]["needs"]["rent"])
    print(analyzer.averages["lifetime"]["needs"]["rent"])


if __name__ == "__main__":
    main()
