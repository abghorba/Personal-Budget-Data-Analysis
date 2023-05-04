import logging as log
import os
from datetime import datetime
from time import time

from numpy import average

from data.generate_datasets import generate_datasets
from src.analysis import SpendingAnalyzer
from src.categorize_data import (
    compile_transactions_into_dictionary,
    load_data_to_dataframe,
    save_spending_data_as_text_file,
)
from src.clean_tsv_data import clean_tsv_file, export_cleaned_data_to_tsv

SMALL_SPENDING_TSV = os.getcwd() + "/data/small-spending.tsv"
MEDIUM_SPENDING_TSV = os.getcwd() + "/data/medium-spending.tsv"
LARGE_SPENDING_TSV = os.getcwd() + "/data/large-spending.tsv"
XLARGE_SPENDING_TSV = os.getcwd() + "/data/xlarge-spending.tsv"
ITERATIONS = 10


def time_clean_tsv_file(raw_filepath, run_times_list, iteration_number=0):
    """
    Gathers and stores run time for clean_tsv_file() in run_times_list[iteration_number].

    :param raw_filepath: Filepath to the raw spending.tsv file
    :param run_times_list: List to hold each run time
    :param iteration_number: Index in which to store run time in run_times_list
    :return: None; information stored in run_times_list
    """

    start = time()
    clean_tsv_file(raw_filepath)
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


def time_get_analysis(budget_dict, run_times_list, iteration_number=0):
    """
    Gathers and stores run time for SpendingAnalyzer.get_analysis() in run_times_list[iteration_number].

    :param budget_dict: Dictionary containing all budget spending
    :param run_times_list: List to hold each run time
    :param iteration_number: Index in which to store run time in run_times_list
    :return: None; information stored in run_times_list
    """

    analyzer = SpendingAnalyzer(budget_dict)
    analyzer.analysis = {}
    start = time()
    analyzer.get_analysis()
    run_times_list[iteration_number] = time() - start


def test_performance():
    # Generate the data sets to be tested with
    generate_datasets()

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

    raw_spending_files = [SMALL_SPENDING_TSV, MEDIUM_SPENDING_TSV, LARGE_SPENDING_TSV, XLARGE_SPENDING_TSV]
    total_start_time = time()

    for raw_spending_file in raw_spending_files:
        log.info(f"Testing with: {raw_spending_file}")
        cleaned_tsv_lines_list = clean_tsv_file(raw_spending_file)
        budget_df = load_data_to_dataframe(raw_spending_file)
        budget_dict = compile_transactions_into_dictionary(budget_df)

        start_time_per_file = time()

        for target in [
            time_clean_tsv_file,
            time_export_cleaned_data_to_tsv,
            time_compile_transactions_into_dictionary_no_threading,
            time_compile_transactions_into_dictionary_with_multithreading,
            time_compile_transactions_into_dictionary_with_multiprocessing,
            time_save_spending_data_as_text_file,
            time_get_analysis,
        ]:
            run_times_list = [0 for _ in range(ITERATIONS)]

            for iteration in range(ITERATIONS):
                if target == time_clean_tsv_file:
                    args = (raw_spending_file, run_times_list, iteration)

                elif target == time_export_cleaned_data_to_tsv:
                    args = (cleaned_tsv_lines_list, run_times_list, iteration)

                elif target in [
                    time_compile_transactions_into_dictionary_no_threading,
                    time_compile_transactions_into_dictionary_with_multithreading,
                    time_compile_transactions_into_dictionary_with_multiprocessing,
                ]:
                    args = (budget_df, run_times_list, iteration)

                elif target in [time_save_spending_data_as_text_file, time_get_analysis]:
                    args = (budget_dict, run_times_list, iteration)

                else:
                    args = (run_times_list, iteration)

                target(*args)

            # log.info(f"{target.__name__}(): {run_times_list}")
            log.info(f"{target.__name__}() took an average time of {average(run_times_list):.10f}s")

        log.info(f"Performance tests for {raw_spending_file} took a total of {time() - start_time_per_file:.10f}s")

    log.info(f"All performance tests took a total of {time() - total_start_time:.10f}s")


if __name__ == "__main__":
    test_performance()
