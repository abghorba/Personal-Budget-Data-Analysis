import os


def generate_datasets():
    raw_spending_tsv_file = os.getcwd() + "/data/spending.tsv"
    small_spending_tsv_file = os.getcwd() + "/data/small-spending.tsv"
    medium_spending_tsv_file = os.getcwd() + "/data/medium-spending.tsv"
    large_spending_tsv_file = os.getcwd() + "/data/large-spending.tsv"
    xlarge_spending_tsv_file = os.getcwd() + "/data/xlarge-spending.tsv"
    datasets_to_generate = [
        small_spending_tsv_file,
        medium_spending_tsv_file,
        large_spending_tsv_file,
        xlarge_spending_tsv_file,
    ]

    with open(raw_spending_tsv_file, "r") as file:
        header_line = file.readline()
        beginning_balance_line = file.readline()
        tsv_file = file.readlines()
        last_line = tsv_file.pop()
        tsv_file_contents = "".join(tsv_file)

    for index, filepath in enumerate(datasets_to_generate):
        with open(filepath, "w") as file:
            file.write(header_line)
            file.write(beginning_balance_line)

            number_of_iterations = 5**index
            for iteration in range(number_of_iterations):
                file.write(tsv_file_contents)

            file.write(last_line)


if __name__ == "__main__":
    generate_datasets()
