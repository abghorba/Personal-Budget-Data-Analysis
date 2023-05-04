import logging as log
import os
from datetime import datetime
from time import time

from numpy import average

from src.analysis import SpendingAnalyzer
from src.categorize_data import (
    compile_transactions_into_dictionary,
    load_data_to_dataframe,
    save_spending_data_as_text_file,
)
from src.clean_tsv_data import clean_tsv_file, export_cleaned_data_to_tsv


def time_clean_tsv_file(run_times_list, iteration_number=0):
    """
    Gathers and stores run time for clean_tsv_file() in run_times_list[iteration_number].

    :param run_times_list: List to hold each run time
    :param iteration_number: Index in which to store run time in run_times_list
    :return: None; information stored in run_times_list
    """

    start = time()
    clean_tsv_file()
    run_times_list[iteration_number] = time() - start


def time_export_cleaned_data_to_tsv(cleaned_tsv_lines_list, run_times_list, iteration_number=0):
    """
    Gathers and stores run time for export_cleaned_data_to_tsv() in run_times_list[iteration_number].

    :param cleaned_tsv_lines_list: List of cleaned TSV lines
    :param run_times_list: List to hold each run time
    :param iteration_number: Index in which to store run time in run_times_list
    :return: None; information stored in run_times_list
    """

    start = time()
    export_cleaned_data_to_tsv(cleaned_tsv_lines_list)
    run_times_list[iteration_number] = time() - start


def time_compile_transactions_into_dictionary_no_threading(budget_df, run_times_list, iteration_number=0):
    """
    Gathers and stores run time for compile_transactions_into_dictionary(use_threading=False)
    in run_times_list[iteration_number].

    :param budget_df: DataFrame object containing the data from cleaned_spending.tsv
    :param run_times_list: List to hold each run time
    :param iteration_number: Index in which to store run time in run_times_list
    :return: None; information stored in run_times_list
    """

    start = time()
    compile_transactions_into_dictionary(budget_df, use_threading=False)
    run_times_list[iteration_number] = time() - start


def time_compile_transactions_into_dictionary_with_multithreading(budget_df, run_times_list, iteration_number=0):
    """
    Gathers and stores run time for compile_transactions_into_dictionary(use_threading=True) in
    run_times_list[iteration_number].

    :param budget_df: DataFrame object containing the data from cleaned_spending.tsv
    :param run_times_list: List to hold each run time
    :param iteration_number: Index in which to store run time in run_times_list
    :return: None; information stored in run_times_list
    """

    start = time()
    compile_transactions_into_dictionary(budget_df, use_threading=True)
    run_times_list[iteration_number] = time() - start


def time_compile_transactions_into_dictionary_with_multiprocessing(budget_df, run_times_list, iteration_number=0):
    """
    Gathers and stores run time for compile_transactions_into_dictionary(use_threading=True) in
    run_times_list[iteration_number].

    :param budget_df: DataFrame object containing the data from cleaned_spending.tsv
    :param run_times_list: List to hold each run time
    :param iteration_number: Index in which to store run time in run_times_list
    :return: None; information stored in run_times_list
    """

    start = time()
    compile_transactions_into_dictionary(budget_df, use_multiprocessing=True)
    run_times_list[iteration_number] = time() - start


def time_save_spending_data_as_text_file(budget_dict, run_times_list, iteration_number=0):
    """
    Gathers and stores run time for save_spending_data_as_text_file() in run_times_list[iteration_number].

    :param budget_dict: Dictionary containing all budget spending
    :param run_times_list: List to hold each run time
    :param iteration_number: Index in which to store run time in run_times_list
    :return: None; information stored in run_times_list
    """

    start = time()
    save_spending_data_as_text_file(budget_dict)
    run_times_list[iteration_number] = time() - start


def time_get_averages(budget_dict, run_times_list, iteration_number=0):
    """
    Gathers and stores run time for SpendingAnalyzer.get_averages() in run_times_list[iteration_number].

    :param budget_dict: Dictionary containing all budget spending
    :param run_times_list: List to hold each run time
    :param iteration_number: Index in which to store run time in run_times_list
    :return: None; information stored in run_times_list
    """

    analyzer = SpendingAnalyzer(budget_dict)
    analyzer.averages = {}
    start = time()
    analyzer.get_averages()
    run_times_list[iteration_number] = time() - start


def main():
    # Set up logger
    log_filename = datetime.now().strftime("%Y%m%d_%H%M%S") + "-log.txt"
    log_directory = f"{os.getcwd()}/logs"
    logfile = os.path.abspath(f"{log_directory}/{log_filename}")

    # Make the log directory if necessary
    if not os.path.exists(log_directory):
        os.mkdir(log_directory)

    log_format = "%(asctime)s\t%(module)20s:%(lineno)4d\t: %(message)s"
    log.basicConfig(filename=logfile, format=log_format, level=log.INFO)
    log.getLogger().addHandler(log.StreamHandler())

    iterations = 100
    cleaned_tsv_lines_list = clean_tsv_file()
    budget_df = load_data_to_dataframe()
    budget_dict = compile_transactions_into_dictionary(budget_df)

    start_time = time()

    for target in [
        time_clean_tsv_file,
        time_export_cleaned_data_to_tsv,
        time_compile_transactions_into_dictionary_no_threading,
        time_compile_transactions_into_dictionary_with_multithreading,
        time_compile_transactions_into_dictionary_with_multiprocessing,
        time_save_spending_data_as_text_file,
        time_get_averages,
    ]:
        run_times_list = [0 for _ in range(iterations)]

        for iteration in range(iterations):
            if target == time_export_cleaned_data_to_tsv:
                args = (cleaned_tsv_lines_list, run_times_list, iteration)

            elif target in [
                time_compile_transactions_into_dictionary_no_threading,
                time_compile_transactions_into_dictionary_with_multithreading,
                time_compile_transactions_into_dictionary_with_multiprocessing,
            ]:
                args = (budget_df, run_times_list, iteration)

            elif target in [time_save_spending_data_as_text_file, time_get_averages]:
                args = (budget_dict, run_times_list, iteration)

            else:
                args = (run_times_list, iteration)

            target(*args)

        # log.info(f"{target.__name__}(): {run_times_list}")
        log.info(f"{target.__name__}() took an average time of {average(run_times_list):.10f}s")

    log.info(f"Performance tests took a total of {time() - start_time:.10f}s")


if __name__ == "__main__":
    main()
