from src.categorize_data import compile_all_spending, save_spending_data_as_text_file


def main():
    budget_dict = compile_all_spending()
    save_spending_data_as_text_file(budget_dict)

    # At this point, we can do whatever data analysis we'd like
    for year in budget_dict:
        for month in budget_dict[year]:
            pass


if __name__ == "__main__":
    main()
