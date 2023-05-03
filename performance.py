import logging as log
import os
from datetime import datetime
from time import time

from src.analysis import SpendingAnalyzer
from src.categorize_data import compile_all_spending, save_spending_data_as_text_file
from src.clean_tsv_data import clean_tsv_file, export_cleaned_data_to_tsv

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

# Start timing
start = time()
cleaned_tsv_lines_list = clean_tsv_file()
log.info(f"clean_tsv_file() took {time() - start:.10f}s")

iterations = 10
average_time = 0

for iteration in range(iterations):
    start = time()
    export_cleaned_data_to_tsv(cleaned_tsv_lines_list)
    average_time += time() - start - 3  # Subtract 3 to account for time.sleep(3)

log.info(f"export_cleaned_data_to_tsv() took an average time of {average_time/iterations:.10f}s")

average_time = 0
budget_dict = {}

for iteration in range(iterations):
    start = time()
    budget_dict = compile_all_spending()
    average_time += time() - start

log.info(f"compile_all_spending() took an average time of {average_time/iterations:.10f}s")

average_time = 0

for iteration in range(iterations):
    start = time()
    save_spending_data_as_text_file(budget_dict)
    average_time += time() - start

log.info(f"save_spending_data_as_text_file() took took an average time of {average_time/iterations:.10f}s")

average_time = 0
analyzer = SpendingAnalyzer(budget_dict)

for iteration in range(iterations):
    analyzer.averages = {}
    start = time()
    analyzer.get_averages()
    average_time += time() - start

log.info(f"SpendingAnalyzer.get_averages() took an average time of {average_time/iterations:.10f}s")
