import os
from decimal import Decimal

from src.budget_items import BudgetSpending

cwd = os.getcwd()
TEST_TSV_FILE1 = cwd + "/tests/files/spending1.tsv"
TEST_TSV_FILE2 = cwd + "/tests/files/spending2.tsv"
TEST_TSV_FILE3 = cwd + "/tests/files/spending3.tsv"
EXPECTED_TEST_SPENDING_FILE1 = cwd + "/tests/files/spending1.txt"
EXPECTED_TEST_SPENDING_FILE2 = cwd + "/tests/files/spending2.txt"
EXPECTED_TEST_SPENDING_FILE3 = cwd + "/tests/files/spending3.txt"
EXPECTED_CLEANED_TSV_FILE1 = cwd + "/tests/files/cleaned_spending1.tsv"
EXPECTED_CLEANED_TSV_FILE2 = cwd + "/tests/files/cleaned_spending2.tsv"
EXPECTED_CLEANED_TSV_FILE3 = cwd + "/tests/files/cleaned_spending3.tsv"
INVALID_PATH = cwd + "/tests/files/invalid.tsv"
TEST_CLEAN_TSV_FILE = cwd + "/tests/files/cleaned_spending.tsv"
TEST_SPENDING_FILE = cwd + "/tests/files/spending.txt"
DATE_RANGE_DICT_SPENDING1 = {"April 2023": ("04/01/2023", "05/01/2023")}
DATE_RANGE_DICT_SPENDING2 = {
    "January 2022": ("01/01/2022", "02/01/2022"),
    "February 2022": ("02/01/2022", "03/01/2022"),
    "March 2022": ("03/01/2022", "04/01/2022"),
    "April 2022": ("04/01/2022", "05/01/2022"),
    "May 2022": ("05/01/2022", "06/01/2022"),
    "June 2022": ("06/01/2022", "07/01/2022"),
    "July 2022": ("07/01/2022", "08/01/2022"),
    "August 2022": ("08/01/2022", "09/01/2022"),
    "September 2022": ("09/01/2022", "10/01/2022"),
    "October 2022": ("10/01/2022", "11/01/2022"),
    "November 2022": ("11/01/2022", "12/01/2022"),
    "December 2022": ("12/01/2022", "01/01/2023"),
}
DATE_RANGE_DICT_SPENDING3 = {
    "January 2021": ("01/01/2021", "02/01/2021"),
    "February 2021": ("02/01/2021", "03/01/2021"),
    "March 2021": ("03/01/2021", "04/01/2021"),
    "April 2021": ("04/01/2021", "05/01/2021"),
    "May 2021": ("05/01/2021", "06/01/2021"),
    "June 2021": ("06/01/2021", "07/01/2021"),
    "July 2021": ("07/01/2021", "08/01/2021"),
    "August 2021": ("08/01/2021", "09/01/2021"),
    "September 2021": ("09/01/2021", "10/01/2021"),
    "October 2021": ("10/01/2021", "11/01/2021"),
    "November 2021": ("11/01/2021", "12/01/2021"),
    "December 2021": ("12/01/2021", "01/01/2022"),
    "January 2022": ("01/01/2022", "02/01/2022"),
    "February 2022": ("02/01/2022", "03/01/2022"),
    "March 2022": ("03/01/2022", "04/01/2022"),
    "April 2022": ("04/01/2022", "05/01/2022"),
    "May 2022": ("05/01/2022", "06/01/2022"),
    "June 2022": ("06/01/2022", "07/01/2022"),
    "July 2022": ("07/01/2022", "08/01/2022"),
    "August 2022": ("08/01/2022", "09/01/2022"),
    "September 2022": ("09/01/2022", "10/01/2022"),
    "October 2022": ("10/01/2022", "11/01/2022"),
    "November 2022": ("11/01/2022", "12/01/2022"),
    "December 2022": ("12/01/2022", "01/01/2023"),
    "January 2023": ("01/01/2023", "02/01/2023"),
    "February 2023": ("02/01/2023", "03/01/2023"),
    "March 2023": ("03/01/2023", "04/01/2023"),
    "April 2023": ("04/01/2023", "05/01/2023"),
}


def get_expected_budget_spending1():
    """Returns the expected BudgetSpending instance pertaining to April 2023 data from /tests/files/spending1.tsv"""

    expected_budget_spending = BudgetSpending("April 2023")
    expected_budget_spending.needs.car_insurance = Decimal("145.60")
    expected_budget_spending.needs.dental_insurance = Decimal("0.00")
    expected_budget_spending.needs.electric_bill = Decimal("16.35")
    expected_budget_spending.needs.emergencies = Decimal("125.99")
    expected_budget_spending.needs.gasoline = Decimal("68.32")
    expected_budget_spending.needs.groceries = Decimal("389.44")
    expected_budget_spending.needs.health_insurance = Decimal("0.00")
    expected_budget_spending.needs.internet_bill = Decimal("69.99")
    expected_budget_spending.needs.laundry = Decimal("0.00")
    expected_budget_spending.needs.misc = Decimal("251.98")
    expected_budget_spending.needs.mortgage = Decimal("0.00")
    expected_budget_spending.needs.other_insurance = Decimal("0.00")
    expected_budget_spending.needs.rent = Decimal("2000.00")
    expected_budget_spending.needs.renters_insurance = Decimal("68.32")
    expected_budget_spending.needs.student_loans = Decimal("145.60")
    expected_budget_spending.needs.taxes = Decimal("400.00")
    expected_budget_spending.needs.vision_insurance = Decimal("0.00")
    expected_budget_spending.wants.free_spending = Decimal("235.93")
    expected_budget_spending.wants.misc = Decimal("44.44")
    expected_budget_spending.wants.subscriptions = Decimal("28.98")
    expected_budget_spending.wants.vacation_spending = Decimal("444.44")
    expected_budget_spending.savings.crypto = Decimal("110.00")
    expected_budget_spending.savings.emergency_fund = Decimal("200.00")
    expected_budget_spending.savings.investing = Decimal("100.00")
    expected_budget_spending.savings.misc = Decimal("55.55")
    expected_budget_spending.savings.retirement = Decimal("700.00")
    expected_budget_spending.income.earnings = Decimal("6000.00")
    expected_budget_spending.income.tax_returns = Decimal("500.00")
    expected_budget_spending.reimbursements.bills = Decimal("40.00")
    expected_budget_spending.reimbursements.credit_card_rewards = Decimal("13.99")
    expected_budget_spending.reimbursements.free_spending = Decimal("45.60")
    expected_budget_spending.reimbursements.rent = Decimal("1000.00")

    return expected_budget_spending


def get_expected_budget_spending2():
    """Returns the expected BudgetSpending instance pertaining to November 2022 data from /tests/files/spending2.tsv"""

    expected_budget_spending = BudgetSpending("November 2022")
    expected_budget_spending.needs.car_insurance = Decimal("145.60")
    expected_budget_spending.needs.dental_insurance = Decimal("0.00")
    expected_budget_spending.needs.electric_bill = Decimal("19.95")
    expected_budget_spending.needs.emergencies = Decimal("400.00")
    expected_budget_spending.needs.gasoline = Decimal("240.64")
    expected_budget_spending.needs.groceries = Decimal("420.69")
    expected_budget_spending.needs.health_insurance = Decimal("0.00")
    expected_budget_spending.needs.internet_bill = Decimal("83.99")
    expected_budget_spending.needs.laundry = Decimal("25.00")
    expected_budget_spending.needs.misc = Decimal("229.00")
    expected_budget_spending.needs.mortgage = Decimal("0.00")
    expected_budget_spending.needs.other_insurance = Decimal("0.00")
    expected_budget_spending.needs.rent = Decimal("2252.00")
    expected_budget_spending.needs.renters_insurance = Decimal("59.50")
    expected_budget_spending.needs.student_loans = Decimal("0.00")
    expected_budget_spending.needs.taxes = Decimal("0.00")
    expected_budget_spending.needs.vision_insurance = Decimal("0.00")
    expected_budget_spending.wants.free_spending = Decimal("1022.15")
    expected_budget_spending.wants.misc = Decimal("0.00")
    expected_budget_spending.wants.subscriptions = Decimal("341.65")
    expected_budget_spending.wants.vacation_spending = Decimal("0.00")
    expected_budget_spending.savings.crypto = Decimal("0.00")
    expected_budget_spending.savings.emergency_fund = Decimal("0.00")
    expected_budget_spending.savings.investing = Decimal("0.00")
    expected_budget_spending.savings.misc = Decimal("0.00")
    expected_budget_spending.savings.retirement = Decimal("0.00")
    expected_budget_spending.income.earnings = Decimal("4183.77")
    expected_budget_spending.income.tax_returns = Decimal("0.00")
    expected_budget_spending.reimbursements.bills = Decimal("51.97")
    expected_budget_spending.reimbursements.credit_card_rewards = Decimal("0.00")
    expected_budget_spending.reimbursements.free_spending = Decimal("236.00")
    expected_budget_spending.reimbursements.rent = Decimal("645.00")

    return expected_budget_spending


def get_expected_budget_spending3():
    """Returns the expected BudgetSpending instance pertaining to June 2021 data from /tests/files/spending3.tsv"""

    expected_budget_spending = BudgetSpending("June 2021")
    expected_budget_spending.needs.car_insurance = Decimal("139.00")
    expected_budget_spending.needs.dental_insurance = Decimal("0.00")
    expected_budget_spending.needs.electric_bill = Decimal("51.86")
    expected_budget_spending.needs.emergencies = Decimal("0.00")
    expected_budget_spending.needs.gasoline = Decimal("134.75")
    expected_budget_spending.needs.groceries = Decimal("377.20")
    expected_budget_spending.needs.health_insurance = Decimal("0.00")
    expected_budget_spending.needs.internet_bill = Decimal("73.99")
    expected_budget_spending.needs.laundry = Decimal("40.00")
    expected_budget_spending.needs.misc = Decimal("0.00")
    expected_budget_spending.needs.mortgage = Decimal("0.00")
    expected_budget_spending.needs.other_insurance = Decimal("0.00")
    expected_budget_spending.needs.rent = Decimal("1035.50")
    expected_budget_spending.needs.renters_insurance = Decimal("0.00")
    expected_budget_spending.needs.student_loans = Decimal("108.05")
    expected_budget_spending.needs.taxes = Decimal("0.00")
    expected_budget_spending.needs.vision_insurance = Decimal("0.00")
    expected_budget_spending.wants.free_spending = Decimal("916.56")
    expected_budget_spending.wants.misc = Decimal("0.00")
    expected_budget_spending.wants.subscriptions = Decimal("143.97")
    expected_budget_spending.wants.vacation_spending = Decimal("0.00")
    expected_budget_spending.savings.crypto = Decimal("247.27")
    expected_budget_spending.savings.emergency_fund = Decimal("400.00")
    expected_budget_spending.savings.investing = Decimal("500.00")
    expected_budget_spending.savings.misc = Decimal("0.00")
    expected_budget_spending.savings.retirement = Decimal("0.00")
    expected_budget_spending.income.earnings = Decimal("3705.83")
    expected_budget_spending.income.tax_returns = Decimal("0.00")
    expected_budget_spending.reimbursements.bills = Decimal("62.93")
    expected_budget_spending.reimbursements.credit_card_rewards = Decimal("0.00")
    expected_budget_spending.reimbursements.free_spending = Decimal("68.27")
    expected_budget_spending.reimbursements.rent = Decimal("0.00")

    return expected_budget_spending


def get_expected_budget_dict1():
    """Returns the expected budget dictionary pertaining to data from /tests/files/spending1.tsv"""

    budget_spending = get_expected_budget_spending1()
    budget_dict = {"2023": {"April": budget_spending}}
    return budget_dict


def get_expected_budget_dict2():
    """Returns the expected budget dictionary pertaining to data from /tests/files/spending2.tsv"""

    budget_dict = {"2022": {}}

    budget_spending = BudgetSpending("January 2022")
    budget_spending.needs.car_insurance = Decimal("142.80")
    budget_spending.needs.dental_insurance = Decimal("0.00")
    budget_spending.needs.electric_bill = Decimal("66.39")
    budget_spending.needs.emergencies = Decimal("0.00")
    budget_spending.needs.gasoline = Decimal("77.22")
    budget_spending.needs.groceries = Decimal("102.35")
    budget_spending.needs.health_insurance = Decimal("0.00")
    budget_spending.needs.internet_bill = Decimal("83.99")
    budget_spending.needs.laundry = Decimal("15.00")
    budget_spending.needs.misc = Decimal("0.00")
    budget_spending.needs.mortgage = Decimal("0.00")
    budget_spending.needs.other_insurance = Decimal("0.00")
    budget_spending.needs.rent = Decimal("1121.51")
    budget_spending.needs.renters_insurance = Decimal("0.00")
    budget_spending.needs.student_loans = Decimal("308.05")
    budget_spending.needs.taxes = Decimal("0.00")
    budget_spending.needs.vision_insurance = Decimal("0.00")
    budget_spending.wants.free_spending = Decimal("807.58")
    budget_spending.wants.misc = Decimal("0.00")
    budget_spending.wants.subscriptions = Decimal("174.47")
    budget_spending.wants.vacation_spending = Decimal("0.00")
    budget_spending.savings.crypto = Decimal("0.00")
    budget_spending.savings.emergency_fund = Decimal("0.00")
    budget_spending.savings.investing = Decimal("0.00")
    budget_spending.savings.misc = Decimal("0.00")
    budget_spending.savings.retirement = Decimal("600.00")
    budget_spending.income.earnings = Decimal("3268.62")
    budget_spending.income.tax_returns = Decimal("0.00")
    budget_spending.reimbursements.bills = Decimal("75.19")
    budget_spending.reimbursements.credit_card_rewards = Decimal("0.00")
    budget_spending.reimbursements.free_spending = Decimal("0.00")
    budget_spending.reimbursements.rent = Decimal("0.00")
    budget_dict["2022"]["January"] = budget_spending

    budget_spending = BudgetSpending("February 2022")
    budget_spending.needs.car_insurance = Decimal("143.88")
    budget_spending.needs.dental_insurance = Decimal("0.00")
    budget_spending.needs.electric_bill = Decimal("86.68")
    budget_spending.needs.emergencies = Decimal("0.00")
    budget_spending.needs.gasoline = Decimal("203.01")
    budget_spending.needs.groceries = Decimal("378.03")
    budget_spending.needs.health_insurance = Decimal("0.00")
    budget_spending.needs.internet_bill = Decimal("83.99")
    budget_spending.needs.laundry = Decimal("0.00")
    budget_spending.needs.misc = Decimal("0.00")
    budget_spending.needs.mortgage = Decimal("0.00")
    budget_spending.needs.other_insurance = Decimal("0.00")
    budget_spending.needs.rent = Decimal("1120.61")
    budget_spending.needs.renters_insurance = Decimal("59.50")
    budget_spending.needs.student_loans = Decimal("308.05")
    budget_spending.needs.taxes = Decimal("0.00")
    budget_spending.needs.vision_insurance = Decimal("0.00")
    budget_spending.wants.free_spending = Decimal("1159.57")
    budget_spending.wants.misc = Decimal("0.00")
    budget_spending.wants.subscriptions = Decimal("223.47")
    budget_spending.wants.vacation_spending = Decimal("0.00")
    budget_spending.savings.crypto = Decimal("0.00")
    budget_spending.savings.emergency_fund = Decimal("435.02")
    budget_spending.savings.investing = Decimal("400.00")
    budget_spending.savings.misc = Decimal("0.00")
    budget_spending.savings.retirement = Decimal("0.00")
    budget_spending.income.earnings = Decimal("6688.96")
    budget_spending.income.tax_returns = Decimal("0.00")
    budget_spending.reimbursements.bills = Decimal("112.80")
    budget_spending.reimbursements.credit_card_rewards = Decimal("0.00")
    budget_spending.reimbursements.free_spending = Decimal("0.00")
    budget_spending.reimbursements.rent = Decimal("0.00")
    budget_dict["2022"]["February"] = budget_spending

    budget_spending = BudgetSpending("March 2022")
    budget_spending.needs.car_insurance = Decimal("142.80")
    budget_spending.needs.dental_insurance = Decimal("0.00")
    budget_spending.needs.electric_bill = Decimal("86.80")
    budget_spending.needs.emergencies = Decimal("0.00")
    budget_spending.needs.gasoline = Decimal("177.51")
    budget_spending.needs.groceries = Decimal("127.99")
    budget_spending.needs.health_insurance = Decimal("0.00")
    budget_spending.needs.internet_bill = Decimal("83.99")
    budget_spending.needs.laundry = Decimal("0.00")
    budget_spending.needs.misc = Decimal("0.00")
    budget_spending.needs.mortgage = Decimal("0.00")
    budget_spending.needs.other_insurance = Decimal("0.00")
    budget_spending.needs.rent = Decimal("1121.21")
    budget_spending.needs.renters_insurance = Decimal("0.00")
    budget_spending.needs.student_loans = Decimal("308.05")
    budget_spending.needs.taxes = Decimal("0.00")
    budget_spending.needs.vision_insurance = Decimal("0.00")
    budget_spending.wants.free_spending = Decimal("655.37")
    budget_spending.wants.misc = Decimal("0.00")
    budget_spending.wants.subscriptions = Decimal("174.47")
    budget_spending.wants.vacation_spending = Decimal("2918.93")
    budget_spending.savings.crypto = Decimal("0.00")
    budget_spending.savings.emergency_fund = Decimal("0.00")
    budget_spending.savings.investing = Decimal("0.00")
    budget_spending.savings.misc = Decimal("0.00")
    budget_spending.savings.retirement = Decimal("0.00")
    budget_spending.income.earnings = Decimal("1466.58")
    budget_spending.income.tax_returns = Decimal("0.00")
    budget_spending.reimbursements.bills = Decimal("85.39")
    budget_spending.reimbursements.credit_card_rewards = Decimal("116.74")
    budget_spending.reimbursements.free_spending = Decimal("0.00")
    budget_spending.reimbursements.rent = Decimal("0.00")
    budget_dict["2022"]["March"] = budget_spending

    budget_spending = BudgetSpending("April 2022")
    budget_spending.needs.car_insurance = Decimal("142.80")
    budget_spending.needs.dental_insurance = Decimal("0.00")
    budget_spending.needs.electric_bill = Decimal("57.64")
    budget_spending.needs.emergencies = Decimal("0.00")
    budget_spending.needs.gasoline = Decimal("213.25")
    budget_spending.needs.groceries = Decimal("318.11")
    budget_spending.needs.health_insurance = Decimal("0.00")
    budget_spending.needs.internet_bill = Decimal("83.99")
    budget_spending.needs.laundry = Decimal("0.00")
    budget_spending.needs.misc = Decimal("0.00")
    budget_spending.needs.mortgage = Decimal("0.00")
    budget_spending.needs.other_insurance = Decimal("0.00")
    budget_spending.needs.rent = Decimal("1120.78")
    budget_spending.needs.renters_insurance = Decimal("0.00")
    budget_spending.needs.student_loans = Decimal("308.05")
    budget_spending.needs.taxes = Decimal("418.00")
    budget_spending.needs.vision_insurance = Decimal("0.00")
    budget_spending.wants.free_spending = Decimal("1033.44")
    budget_spending.wants.misc = Decimal("0.00")
    budget_spending.wants.subscriptions = Decimal("238.97")
    budget_spending.wants.vacation_spending = Decimal("0.00")
    budget_spending.savings.crypto = Decimal("0.00")
    budget_spending.savings.emergency_fund = Decimal("1636.87")
    budget_spending.savings.investing = Decimal("1471.81")
    budget_spending.savings.misc = Decimal("0.00")
    budget_spending.savings.retirement = Decimal("0.00")
    budget_spending.income.earnings = Decimal("9319.97")
    budget_spending.income.tax_returns = Decimal("0.00")
    budget_spending.reimbursements.bills = Decimal("70.81")
    budget_spending.reimbursements.credit_card_rewards = Decimal("0.00")
    budget_spending.reimbursements.free_spending = Decimal("0.00")
    budget_spending.reimbursements.rent = Decimal("0.00")
    budget_dict["2022"]["April"] = budget_spending

    budget_spending = BudgetSpending("May 2022")
    budget_spending.needs.car_insurance = Decimal("142.80")
    budget_spending.needs.dental_insurance = Decimal("0.00")
    budget_spending.needs.electric_bill = Decimal("6.66")
    budget_spending.needs.emergencies = Decimal("0.00")
    budget_spending.needs.gasoline = Decimal("227.30")
    budget_spending.needs.groceries = Decimal("405.57")
    budget_spending.needs.health_insurance = Decimal("0.00")
    budget_spending.needs.internet_bill = Decimal("83.99")
    budget_spending.needs.laundry = Decimal("10.00")
    budget_spending.needs.misc = Decimal("0.00")
    budget_spending.needs.mortgage = Decimal("0.00")
    budget_spending.needs.other_insurance = Decimal("0.00")
    budget_spending.needs.rent = Decimal("1121.70")
    budget_spending.needs.renters_insurance = Decimal("59.50")
    budget_spending.needs.student_loans = Decimal("308.05")
    budget_spending.needs.taxes = Decimal("0.00")
    budget_spending.needs.vision_insurance = Decimal("0.00")
    budget_spending.wants.free_spending = Decimal("1080.12")
    budget_spending.wants.misc = Decimal("0.00")
    budget_spending.wants.subscriptions = Decimal("313.16")
    budget_spending.wants.vacation_spending = Decimal("0.00")
    budget_spending.savings.crypto = Decimal("0.00")
    budget_spending.savings.emergency_fund = Decimal("600.00")
    budget_spending.savings.investing = Decimal("500.00")
    budget_spending.savings.misc = Decimal("0.00")
    budget_spending.savings.retirement = Decimal("0.00")
    budget_spending.income.earnings = Decimal("4065.55")
    budget_spending.income.tax_returns = Decimal("0.00")
    budget_spending.reimbursements.bills = Decimal("75.07")
    budget_spending.reimbursements.credit_card_rewards = Decimal("0.00")
    budget_spending.reimbursements.free_spending = Decimal("0.00")
    budget_spending.reimbursements.rent = Decimal("0.00")
    budget_dict["2022"]["May"] = budget_spending

    budget_spending = BudgetSpending("June 2022")
    budget_spending.needs.car_insurance = Decimal("142.80")
    budget_spending.needs.dental_insurance = Decimal("0.00")
    budget_spending.needs.electric_bill = Decimal("65.26")
    budget_spending.needs.emergencies = Decimal("1006.15")
    budget_spending.needs.gasoline = Decimal("278.63")
    budget_spending.needs.groceries = Decimal("576.01")
    budget_spending.needs.health_insurance = Decimal("0.00")
    budget_spending.needs.internet_bill = Decimal("83.99")
    budget_spending.needs.laundry = Decimal("0.00")
    budget_spending.needs.misc = Decimal("0.00")
    budget_spending.needs.mortgage = Decimal("0.00")
    budget_spending.needs.other_insurance = Decimal("0.00")
    budget_spending.needs.rent = Decimal("1114.01")
    budget_spending.needs.renters_insurance = Decimal("0.00")
    budget_spending.needs.student_loans = Decimal("308.05")
    budget_spending.needs.taxes = Decimal("0.00")
    budget_spending.needs.vision_insurance = Decimal("0.00")
    budget_spending.wants.free_spending = Decimal("661.48")
    budget_spending.wants.misc = Decimal("0.00")
    budget_spending.wants.subscriptions = Decimal("325.15")
    budget_spending.wants.vacation_spending = Decimal("0.00")
    budget_spending.savings.crypto = Decimal("0.00")
    budget_spending.savings.emergency_fund = Decimal("550.00")
    budget_spending.savings.investing = Decimal("450.00")
    budget_spending.savings.misc = Decimal("0.00")
    budget_spending.savings.retirement = Decimal("0.00")
    budget_spending.income.earnings = Decimal("4093.67")
    budget_spending.income.tax_returns = Decimal("0.00")
    budget_spending.reimbursements.bills = Decimal("74.62")
    budget_spending.reimbursements.credit_card_rewards = Decimal("92.05")
    budget_spending.reimbursements.free_spending = Decimal("0.00")
    budget_spending.reimbursements.rent = Decimal("0.00")
    budget_dict["2022"]["June"] = budget_spending

    budget_spending = BudgetSpending("July 2022")
    budget_spending.needs.car_insurance = Decimal("142.80")
    budget_spending.needs.dental_insurance = Decimal("0.00")
    budget_spending.needs.electric_bill = Decimal("114.37")
    budget_spending.needs.emergencies = Decimal("0.00")
    budget_spending.needs.gasoline = Decimal("417.16")
    budget_spending.needs.groceries = Decimal("394.67")
    budget_spending.needs.health_insurance = Decimal("0.00")
    budget_spending.needs.internet_bill = Decimal("83.99")
    budget_spending.needs.laundry = Decimal("0.00")
    budget_spending.needs.misc = Decimal("0.00")
    budget_spending.needs.mortgage = Decimal("0.00")
    budget_spending.needs.other_insurance = Decimal("0.00")
    budget_spending.needs.rent = Decimal("1123.02")
    budget_spending.needs.renters_insurance = Decimal("0.00")
    budget_spending.needs.student_loans = Decimal("308.05")
    budget_spending.needs.taxes = Decimal("0.00")
    budget_spending.needs.vision_insurance = Decimal("0.00")
    budget_spending.wants.free_spending = Decimal("832.97")
    budget_spending.wants.misc = Decimal("0.00")
    budget_spending.wants.subscriptions = Decimal("325.15")
    budget_spending.wants.vacation_spending = Decimal("266.00")
    budget_spending.savings.crypto = Decimal("0.00")
    budget_spending.savings.emergency_fund = Decimal("500.00")
    budget_spending.savings.investing = Decimal("200.00")
    budget_spending.savings.misc = Decimal("0.00")
    budget_spending.savings.retirement = Decimal("0.00")
    budget_spending.income.earnings = Decimal("4022.03")
    budget_spending.income.tax_returns = Decimal("0.00")
    budget_spending.reimbursements.bills = Decimal("99.18")
    budget_spending.reimbursements.credit_card_rewards = Decimal("0.00")
    budget_spending.reimbursements.free_spending = Decimal("12.00")
    budget_spending.reimbursements.rent = Decimal("0.00")
    budget_dict["2022"]["July"] = budget_spending

    budget_spending = BudgetSpending("August 2022")
    budget_spending.needs.car_insurance = Decimal("146.88")
    budget_spending.needs.dental_insurance = Decimal("0.00")
    budget_spending.needs.electric_bill = Decimal("118.86")
    budget_spending.needs.emergencies = Decimal("0.00")
    budget_spending.needs.gasoline = Decimal("196.85")
    budget_spending.needs.groceries = Decimal("417.54")
    budget_spending.needs.health_insurance = Decimal("0.00")
    budget_spending.needs.internet_bill = Decimal("83.99")
    budget_spending.needs.laundry = Decimal("20.00")
    budget_spending.needs.misc = Decimal("542.00")
    budget_spending.needs.mortgage = Decimal("0.00")
    budget_spending.needs.other_insurance = Decimal("0.00")
    budget_spending.needs.rent = Decimal("1667.05")
    budget_spending.needs.renters_insurance = Decimal("59.50")
    budget_spending.needs.student_loans = Decimal("300.00")
    budget_spending.needs.taxes = Decimal("0.00")
    budget_spending.needs.vision_insurance = Decimal("0.00")
    budget_spending.wants.free_spending = Decimal("1069.49")
    budget_spending.wants.misc = Decimal("0.00")
    budget_spending.wants.subscriptions = Decimal("328.15")
    budget_spending.wants.vacation_spending = Decimal("0.00")
    budget_spending.savings.crypto = Decimal("0.00")
    budget_spending.savings.emergency_fund = Decimal("500.00")
    budget_spending.savings.investing = Decimal("0.00")
    budget_spending.savings.misc = Decimal("0.00")
    budget_spending.savings.retirement = Decimal("0.00")
    budget_spending.income.earnings = Decimal("4287.17")
    budget_spending.income.tax_returns = Decimal("0.00")
    budget_spending.reimbursements.bills = Decimal("0.00")
    budget_spending.reimbursements.credit_card_rewards = Decimal("0.00")
    budget_spending.reimbursements.free_spending = Decimal("550.00")
    budget_spending.reimbursements.rent = Decimal("0.00")
    budget_dict["2022"]["August"] = budget_spending

    budget_spending = BudgetSpending("September 2022")
    budget_spending.needs.car_insurance = Decimal("145.60")
    budget_spending.needs.dental_insurance = Decimal("0.00")
    budget_spending.needs.electric_bill = Decimal("110.56")
    budget_spending.needs.emergencies = Decimal("0.00")
    budget_spending.needs.gasoline = Decimal("249.06")
    budget_spending.needs.groceries = Decimal("414.80")
    budget_spending.needs.health_insurance = Decimal("0.00")
    budget_spending.needs.internet_bill = Decimal("83.99")
    budget_spending.needs.laundry = Decimal("25.00")
    budget_spending.needs.misc = Decimal("0.00")
    budget_spending.needs.mortgage = Decimal("0.00")
    budget_spending.needs.other_insurance = Decimal("0.00")
    budget_spending.needs.rent = Decimal("2252.12")
    budget_spending.needs.renters_insurance = Decimal("0.00")
    budget_spending.needs.student_loans = Decimal("0.00")
    budget_spending.needs.taxes = Decimal("0.00")
    budget_spending.needs.vision_insurance = Decimal("0.00")
    budget_spending.wants.free_spending = Decimal("1437.87")
    budget_spending.wants.misc = Decimal("0.00")
    budget_spending.wants.subscriptions = Decimal("343.23")
    budget_spending.wants.vacation_spending = Decimal("388.55")
    budget_spending.savings.crypto = Decimal("0.00")
    budget_spending.savings.emergency_fund = Decimal("1400.00")
    budget_spending.savings.investing = Decimal("0.00")
    budget_spending.savings.misc = Decimal("0.00")
    budget_spending.savings.retirement = Decimal("0.00")
    budget_spending.income.earnings = Decimal("7852.29")
    budget_spending.income.tax_returns = Decimal("0.00")
    budget_spending.reimbursements.bills = Decimal("0.00")
    budget_spending.reimbursements.credit_card_rewards = Decimal("0.00")
    budget_spending.reimbursements.free_spending = Decimal("235.75")
    budget_spending.reimbursements.rent = Decimal("300.00")
    budget_dict["2022"]["September"] = budget_spending

    budget_spending = BudgetSpending("October 2022")
    budget_spending.needs.car_insurance = Decimal("145.60")
    budget_spending.needs.dental_insurance = Decimal("0.00")
    budget_spending.needs.electric_bill = Decimal("103.78")
    budget_spending.needs.emergencies = Decimal("0.00")
    budget_spending.needs.gasoline = Decimal("146.84")
    budget_spending.needs.groceries = Decimal("516.67")
    budget_spending.needs.health_insurance = Decimal("0.00")
    budget_spending.needs.internet_bill = Decimal("83.99")
    budget_spending.needs.laundry = Decimal("60.00")
    budget_spending.needs.misc = Decimal("0.00")
    budget_spending.needs.mortgage = Decimal("0.00")
    budget_spending.needs.other_insurance = Decimal("0.00")
    budget_spending.needs.rent = Decimal("2271.49")
    budget_spending.needs.renters_insurance = Decimal("0.00")
    budget_spending.needs.student_loans = Decimal("0.00")
    budget_spending.needs.taxes = Decimal("0.00")
    budget_spending.needs.vision_insurance = Decimal("0.00")
    budget_spending.wants.free_spending = Decimal("1623.82")
    budget_spending.wants.misc = Decimal("0.00")
    budget_spending.wants.subscriptions = Decimal("341.65")
    budget_spending.wants.vacation_spending = Decimal("812.20")
    budget_spending.savings.crypto = Decimal("0.00")
    budget_spending.savings.emergency_fund = Decimal("300.00")
    budget_spending.savings.investing = Decimal("0.00")
    budget_spending.savings.misc = Decimal("0.00")
    budget_spending.savings.retirement = Decimal("0.00")
    budget_spending.income.earnings = Decimal("4197.21")
    budget_spending.income.tax_returns = Decimal("0.00")
    budget_spending.reimbursements.bills = Decimal("93.88")
    budget_spending.reimbursements.credit_card_rewards = Decimal("217.55")
    budget_spending.reimbursements.free_spending = Decimal("86.00")
    budget_spending.reimbursements.rent = Decimal("600.00")
    budget_dict["2022"]["October"] = budget_spending

    budget_spending = BudgetSpending("November 2022")
    budget_spending.needs.car_insurance = Decimal("145.60")
    budget_spending.needs.dental_insurance = Decimal("0.00")
    budget_spending.needs.electric_bill = Decimal("19.95")
    budget_spending.needs.emergencies = Decimal("400.00")
    budget_spending.needs.gasoline = Decimal("240.64")
    budget_spending.needs.groceries = Decimal("420.69")
    budget_spending.needs.health_insurance = Decimal("0.00")
    budget_spending.needs.internet_bill = Decimal("83.99")
    budget_spending.needs.laundry = Decimal("25.00")
    budget_spending.needs.misc = Decimal("229.00")
    budget_spending.needs.mortgage = Decimal("0.00")
    budget_spending.needs.other_insurance = Decimal("0.00")
    budget_spending.needs.rent = Decimal("2252.00")
    budget_spending.needs.renters_insurance = Decimal("59.50")
    budget_spending.needs.student_loans = Decimal("0.00")
    budget_spending.needs.taxes = Decimal("0.00")
    budget_spending.needs.vision_insurance = Decimal("0.00")
    budget_spending.wants.free_spending = Decimal("1022.15")
    budget_spending.wants.misc = Decimal("0.00")
    budget_spending.wants.subscriptions = Decimal("341.65")
    budget_spending.wants.vacation_spending = Decimal("0.00")
    budget_spending.savings.crypto = Decimal("0.00")
    budget_spending.savings.emergency_fund = Decimal("0.00")
    budget_spending.savings.investing = Decimal("0.00")
    budget_spending.savings.misc = Decimal("0.00")
    budget_spending.savings.retirement = Decimal("0.00")
    budget_spending.income.earnings = Decimal("4183.77")
    budget_spending.income.tax_returns = Decimal("0.00")
    budget_spending.reimbursements.bills = Decimal("51.97")
    budget_spending.reimbursements.credit_card_rewards = Decimal("0.00")
    budget_spending.reimbursements.free_spending = Decimal("236.00")
    budget_spending.reimbursements.rent = Decimal("645.00")
    budget_dict["2022"]["November"] = budget_spending

    budget_spending = BudgetSpending("December 2022")
    budget_spending.needs.car_insurance = Decimal("145.60")
    budget_spending.needs.dental_insurance = Decimal("0.00")
    budget_spending.needs.electric_bill = Decimal("117.35")
    budget_spending.needs.emergencies = Decimal("0.00")
    budget_spending.needs.gasoline = Decimal("67.84")
    budget_spending.needs.groceries = Decimal("578.81")
    budget_spending.needs.health_insurance = Decimal("0.00")
    budget_spending.needs.internet_bill = Decimal("83.99")
    budget_spending.needs.laundry = Decimal("50.00")
    budget_spending.needs.misc = Decimal("0.00")
    budget_spending.needs.mortgage = Decimal("0.00")
    budget_spending.needs.other_insurance = Decimal("0.00")
    budget_spending.needs.rent = Decimal("2248.86")
    budget_spending.needs.renters_insurance = Decimal("0.00")
    budget_spending.needs.student_loans = Decimal("0.00")
    budget_spending.needs.taxes = Decimal("0.00")
    budget_spending.needs.vision_insurance = Decimal("0.00")
    budget_spending.wants.free_spending = Decimal("864.07")
    budget_spending.wants.misc = Decimal("0.00")
    budget_spending.wants.subscriptions = Decimal("347.62")
    budget_spending.wants.vacation_spending = Decimal("1699.82")
    budget_spending.savings.crypto = Decimal("0.00")
    budget_spending.savings.emergency_fund = Decimal("0.00")
    budget_spending.savings.investing = Decimal("0.00")
    budget_spending.savings.misc = Decimal("0.00")
    budget_spending.savings.retirement = Decimal("0.00")
    budget_spending.income.earnings = Decimal("4180.64")
    budget_spending.income.tax_returns = Decimal("250.00")
    budget_spending.reimbursements.bills = Decimal("100.67")
    budget_spending.reimbursements.credit_card_rewards = Decimal("215.10")
    budget_spending.reimbursements.free_spending = Decimal("100.00")
    budget_spending.reimbursements.rent = Decimal("645.00")
    budget_dict["2022"]["December"] = budget_spending

    return budget_dict


def get_expected_budget_dict3():
    """Returns the expected budget dictionary pertaining to data from /tests/files/spending3.tsv"""

    budget_dict = {"2021": {}, "2022": {}, "2023": {}}

    budget_spending = BudgetSpending("March 2021")
    budget_spending.needs.car_insurance = Decimal("139.00")
    budget_spending.needs.dental_insurance = Decimal("0.00")
    budget_spending.needs.electric_bill = Decimal("98.14")
    budget_spending.needs.emergencies = Decimal("0.00")
    budget_spending.needs.gasoline = Decimal("158.70")
    budget_spending.needs.groceries = Decimal("316.74")
    budget_spending.needs.health_insurance = Decimal("0.00")
    budget_spending.needs.internet_bill = Decimal("73.99")
    budget_spending.needs.laundry = Decimal("10.00")
    budget_spending.needs.misc = Decimal("0.00")
    budget_spending.needs.mortgage = Decimal("0.00")
    budget_spending.needs.other_insurance = Decimal("0.00")
    budget_spending.needs.rent = Decimal("1033.43")
    budget_spending.needs.renters_insurance = Decimal("0.00")
    budget_spending.needs.student_loans = Decimal("608.05")
    budget_spending.needs.taxes = Decimal("0.00")
    budget_spending.needs.vision_insurance = Decimal("0.00")
    budget_spending.wants.free_spending = Decimal("1220.00")
    budget_spending.wants.misc = Decimal("0.00")
    budget_spending.wants.subscriptions = Decimal("194.69")
    budget_spending.wants.vacation_spending = Decimal("0.00")
    budget_spending.savings.crypto = Decimal("180.00")
    budget_spending.savings.emergency_fund = Decimal("700.00")
    budget_spending.savings.investing = Decimal("200.00")
    budget_spending.savings.misc = Decimal("0.00")
    budget_spending.savings.retirement = Decimal("800.00")
    budget_spending.income.earnings = Decimal("4495.86")
    budget_spending.income.tax_returns = Decimal("0.00")
    budget_spending.reimbursements.bills = Decimal("86.07")
    budget_spending.reimbursements.credit_card_rewards = Decimal("0.00")
    budget_spending.reimbursements.free_spending = Decimal("0.00")
    budget_spending.reimbursements.rent = Decimal("0.00")
    budget_dict["2021"]["March"] = budget_spending

    budget_spending = BudgetSpending("April 2021")
    budget_spending.needs.car_insurance = Decimal("139.00")
    budget_spending.needs.dental_insurance = Decimal("0.00")
    budget_spending.needs.electric_bill = Decimal("49.60")
    budget_spending.needs.emergencies = Decimal("0.00")
    budget_spending.needs.gasoline = Decimal("126.05")
    budget_spending.needs.groceries = Decimal("126.91")
    budget_spending.needs.health_insurance = Decimal("0.00")
    budget_spending.needs.internet_bill = Decimal("73.99")
    budget_spending.needs.laundry = Decimal("0.00")
    budget_spending.needs.misc = Decimal("0.00")
    budget_spending.needs.mortgage = Decimal("0.00")
    budget_spending.needs.other_insurance = Decimal("0.00")
    budget_spending.needs.rent = Decimal("1034.39")
    budget_spending.needs.renters_insurance = Decimal("0.00")
    budget_spending.needs.student_loans = Decimal("368.05")
    budget_spending.needs.taxes = Decimal("0.00")
    budget_spending.needs.vision_insurance = Decimal("0.00")
    budget_spending.wants.free_spending = Decimal("620.53")
    budget_spending.wants.misc = Decimal("0.00")
    budget_spending.wants.subscriptions = Decimal("143.97")
    budget_spending.wants.vacation_spending = Decimal("0.00")
    budget_spending.savings.crypto = Decimal("250.00")
    budget_spending.savings.emergency_fund = Decimal("100.00")
    budget_spending.savings.investing = Decimal("472.00")
    budget_spending.savings.misc = Decimal("0.00")
    budget_spending.savings.retirement = Decimal("400.00")
    budget_spending.income.earnings = Decimal("5226.63")
    budget_spending.income.tax_returns = Decimal("0.00")
    budget_spending.reimbursements.bills = Decimal("61.79")
    budget_spending.reimbursements.credit_card_rewards = Decimal("0.00")
    budget_spending.reimbursements.free_spending = Decimal("0.00")
    budget_spending.reimbursements.rent = Decimal("0.00")
    budget_dict["2021"]["April"] = budget_spending

    budget_spending = BudgetSpending("May 2021")
    budget_spending.needs.car_insurance = Decimal("139.00")
    budget_spending.needs.dental_insurance = Decimal("0.00")
    budget_spending.needs.electric_bill = Decimal("29.95")
    budget_spending.needs.emergencies = Decimal("288.61")
    budget_spending.needs.gasoline = Decimal("247.11")
    budget_spending.needs.groceries = Decimal("543.56")
    budget_spending.needs.health_insurance = Decimal("0.00")
    budget_spending.needs.internet_bill = Decimal("73.99")
    budget_spending.needs.laundry = Decimal("0.00")
    budget_spending.needs.misc = Decimal("0.00")
    budget_spending.needs.mortgage = Decimal("0.00")
    budget_spending.needs.other_insurance = Decimal("0.00")
    budget_spending.needs.rent = Decimal("1035.39")
    budget_spending.needs.renters_insurance = Decimal("59.50")
    budget_spending.needs.student_loans = Decimal("108.05")
    budget_spending.needs.taxes = Decimal("345.00")
    budget_spending.needs.vision_insurance = Decimal("0.00")
    budget_spending.wants.free_spending = Decimal("1009.09")
    budget_spending.wants.misc = Decimal("0.00")
    budget_spending.wants.subscriptions = Decimal("63.96")
    budget_spending.wants.vacation_spending = Decimal("0.00")
    budget_spending.savings.crypto = Decimal("210.00")
    budget_spending.savings.emergency_fund = Decimal("400.00")
    budget_spending.savings.investing = Decimal("480.00")
    budget_spending.savings.misc = Decimal("0.00")
    budget_spending.savings.retirement = Decimal("0.00")
    budget_spending.income.earnings = Decimal("3940.99")
    budget_spending.income.tax_returns = Decimal("319.00")
    budget_spending.reimbursements.bills = Decimal("81.72")
    budget_spending.reimbursements.credit_card_rewards = Decimal("71.33")
    budget_spending.reimbursements.free_spending = Decimal("106.00")
    budget_spending.reimbursements.rent = Decimal("0.00")
    budget_dict["2021"]["May"] = budget_spending

    budget_spending = BudgetSpending("June 2021")
    budget_spending.needs.car_insurance = Decimal("139.00")
    budget_spending.needs.dental_insurance = Decimal("0.00")
    budget_spending.needs.electric_bill = Decimal("51.86")
    budget_spending.needs.emergencies = Decimal("0.00")
    budget_spending.needs.gasoline = Decimal("134.75")
    budget_spending.needs.groceries = Decimal("377.20")
    budget_spending.needs.health_insurance = Decimal("0.00")
    budget_spending.needs.internet_bill = Decimal("73.99")
    budget_spending.needs.laundry = Decimal("40.00")
    budget_spending.needs.misc = Decimal("0.00")
    budget_spending.needs.mortgage = Decimal("0.00")
    budget_spending.needs.other_insurance = Decimal("0.00")
    budget_spending.needs.rent = Decimal("1035.50")
    budget_spending.needs.renters_insurance = Decimal("0.00")
    budget_spending.needs.student_loans = Decimal("108.05")
    budget_spending.needs.taxes = Decimal("0.00")
    budget_spending.needs.vision_insurance = Decimal("0.00")
    budget_spending.wants.free_spending = Decimal("916.56")
    budget_spending.wants.misc = Decimal("0.00")
    budget_spending.wants.subscriptions = Decimal("143.97")
    budget_spending.wants.vacation_spending = Decimal("0.00")
    budget_spending.savings.crypto = Decimal("247.27")
    budget_spending.savings.emergency_fund = Decimal("400.00")
    budget_spending.savings.investing = Decimal("500.00")
    budget_spending.savings.misc = Decimal("0.00")
    budget_spending.savings.retirement = Decimal("0.00")
    budget_spending.income.earnings = Decimal("3705.83")
    budget_spending.income.tax_returns = Decimal("0.00")
    budget_spending.reimbursements.bills = Decimal("62.93")
    budget_spending.reimbursements.credit_card_rewards = Decimal("0.00")
    budget_spending.reimbursements.free_spending = Decimal("68.27")
    budget_spending.reimbursements.rent = Decimal("0.00")
    budget_dict["2021"]["June"] = budget_spending

    budget_spending = BudgetSpending("July 2021")
    budget_spending.needs.car_insurance = Decimal("139.00")
    budget_spending.needs.dental_insurance = Decimal("0.00")
    budget_spending.needs.electric_bill = Decimal("74.42")
    budget_spending.needs.emergencies = Decimal("0.00")
    budget_spending.needs.gasoline = Decimal("172.36")
    budget_spending.needs.groceries = Decimal("276.06")
    budget_spending.needs.health_insurance = Decimal("0.00")
    budget_spending.needs.internet_bill = Decimal("73.99")
    budget_spending.needs.laundry = Decimal("0.00")
    budget_spending.needs.misc = Decimal("30.69")
    budget_spending.needs.mortgage = Decimal("0.00")
    budget_spending.needs.other_insurance = Decimal("0.00")
    budget_spending.needs.rent = Decimal("1035.19")
    budget_spending.needs.renters_insurance = Decimal("0.00")
    budget_spending.needs.student_loans = Decimal("368.05")
    budget_spending.needs.taxes = Decimal("0.00")
    budget_spending.needs.vision_insurance = Decimal("0.00")
    budget_spending.wants.free_spending = Decimal("868.59")
    budget_spending.wants.misc = Decimal("0.00")
    budget_spending.wants.subscriptions = Decimal("248.98")
    budget_spending.wants.vacation_spending = Decimal("0.00")
    budget_spending.savings.crypto = Decimal("250.00")
    budget_spending.savings.emergency_fund = Decimal("400.00")
    budget_spending.savings.investing = Decimal("480.00")
    budget_spending.savings.misc = Decimal("0.00")
    budget_spending.savings.retirement = Decimal("0.00")
    budget_spending.income.earnings = Decimal("3284.40")
    budget_spending.income.tax_returns = Decimal("0.00")
    budget_spending.reimbursements.bills = Decimal("74.20")
    budget_spending.reimbursements.credit_card_rewards = Decimal("0.00")
    budget_spending.reimbursements.free_spending = Decimal("0.00")
    budget_spending.reimbursements.rent = Decimal("0.00")
    budget_dict["2021"]["July"] = budget_spending

    budget_spending = BudgetSpending("August 2021")
    budget_spending.needs.car_insurance = Decimal("143.95")
    budget_spending.needs.dental_insurance = Decimal("0.00")
    budget_spending.needs.electric_bill = Decimal("106.06")
    budget_spending.needs.emergencies = Decimal("0.00")
    budget_spending.needs.gasoline = Decimal("301.22")
    budget_spending.needs.groceries = Decimal("60.97")
    budget_spending.needs.health_insurance = Decimal("0.00")
    budget_spending.needs.internet_bill = Decimal("83.99")
    budget_spending.needs.laundry = Decimal("10.00")
    budget_spending.needs.misc = Decimal("42.99")
    budget_spending.needs.mortgage = Decimal("0.00")
    budget_spending.needs.other_insurance = Decimal("0.00")
    budget_spending.needs.rent = Decimal("1033.92")
    budget_spending.needs.renters_insurance = Decimal("59.50")
    budget_spending.needs.student_loans = Decimal("108.05")
    budget_spending.needs.taxes = Decimal("0.00")
    budget_spending.needs.vision_insurance = Decimal("0.00")
    budget_spending.wants.free_spending = Decimal("2625.63")
    budget_spending.wants.misc = Decimal("0.00")
    budget_spending.wants.subscriptions = Decimal("148.98")
    budget_spending.wants.vacation_spending = Decimal("0.00")
    budget_spending.savings.crypto = Decimal("200.00")
    budget_spending.savings.emergency_fund = Decimal("400.00")
    budget_spending.savings.investing = Decimal("0.00")
    budget_spending.savings.misc = Decimal("0.00")
    budget_spending.savings.retirement = Decimal("0.00")
    budget_spending.income.earnings = Decimal("4601.99")
    budget_spending.income.tax_returns = Decimal("0.00")
    budget_spending.reimbursements.bills = Decimal("124.78")
    budget_spending.reimbursements.credit_card_rewards = Decimal("425.00")
    budget_spending.reimbursements.free_spending = Decimal("64.00")
    budget_spending.reimbursements.rent = Decimal("0.00")
    budget_dict["2021"]["August"] = budget_spending

    budget_spending = BudgetSpending("September 2021")
    budget_spending.needs.car_insurance = Decimal("142.80")
    budget_spending.needs.dental_insurance = Decimal("0.00")
    budget_spending.needs.electric_bill = Decimal("83.82")
    budget_spending.needs.emergencies = Decimal("0.00")
    budget_spending.needs.gasoline = Decimal("145.18")
    budget_spending.needs.groceries = Decimal("191.00")
    budget_spending.needs.health_insurance = Decimal("0.00")
    budget_spending.needs.internet_bill = Decimal("83.99")
    budget_spending.needs.laundry = Decimal("0.00")
    budget_spending.needs.misc = Decimal("0.00")
    budget_spending.needs.mortgage = Decimal("0.00")
    budget_spending.needs.other_insurance = Decimal("0.00")
    budget_spending.needs.rent = Decimal("1101.11")
    budget_spending.needs.renters_insurance = Decimal("0.00")
    budget_spending.needs.student_loans = Decimal("1655.03")
    budget_spending.needs.taxes = Decimal("0.00")
    budget_spending.needs.vision_insurance = Decimal("0.00")
    budget_spending.wants.free_spending = Decimal("1862.81")
    budget_spending.wants.misc = Decimal("0.00")
    budget_spending.wants.subscriptions = Decimal("49.47")
    budget_spending.wants.vacation_spending = Decimal("0.00")
    budget_spending.savings.crypto = Decimal("200.00")
    budget_spending.savings.emergency_fund = Decimal("200.00")
    budget_spending.savings.investing = Decimal("0.00")
    budget_spending.savings.misc = Decimal("0.00")
    budget_spending.savings.retirement = Decimal("0.00")
    budget_spending.income.earnings = Decimal("4094.29")
    budget_spending.income.tax_returns = Decimal("0.00")
    budget_spending.reimbursements.bills = Decimal("83.91")
    budget_spending.reimbursements.credit_card_rewards = Decimal("0.00")
    budget_spending.reimbursements.free_spending = Decimal("0.00")
    budget_spending.reimbursements.rent = Decimal("0.00")
    budget_dict["2021"]["September"] = budget_spending

    budget_spending = BudgetSpending("October 2021")
    budget_spending.needs.car_insurance = Decimal("142.80")
    budget_spending.needs.dental_insurance = Decimal("0.00")
    budget_spending.needs.electric_bill = Decimal("68.52")
    budget_spending.needs.emergencies = Decimal("0.00")
    budget_spending.needs.gasoline = Decimal("142.02")
    budget_spending.needs.groceries = Decimal("65.98")
    budget_spending.needs.health_insurance = Decimal("0.00")
    budget_spending.needs.internet_bill = Decimal("83.99")
    budget_spending.needs.laundry = Decimal("0.00")
    budget_spending.needs.misc = Decimal("0.00")
    budget_spending.needs.mortgage = Decimal("0.00")
    budget_spending.needs.other_insurance = Decimal("0.00")
    budget_spending.needs.rent = Decimal("1116.95")
    budget_spending.needs.renters_insurance = Decimal("0.00")
    budget_spending.needs.student_loans = Decimal("308.05")
    budget_spending.needs.taxes = Decimal("0.00")
    budget_spending.needs.vision_insurance = Decimal("0.00")
    budget_spending.wants.free_spending = Decimal("1539.19")
    budget_spending.wants.misc = Decimal("0.00")
    budget_spending.wants.subscriptions = Decimal("174.47")
    budget_spending.wants.vacation_spending = Decimal("0.00")
    budget_spending.savings.crypto = Decimal("260.00")
    budget_spending.savings.emergency_fund = Decimal("0.00")
    budget_spending.savings.investing = Decimal("600.00")
    budget_spending.savings.misc = Decimal("0.00")
    budget_spending.savings.retirement = Decimal("0.00")
    budget_spending.income.earnings = Decimal("4926.58")
    budget_spending.income.tax_returns = Decimal("0.00")
    budget_spending.reimbursements.bills = Decimal("76.26")
    budget_spending.reimbursements.credit_card_rewards = Decimal("0.00")
    budget_spending.reimbursements.free_spending = Decimal("0.00")
    budget_spending.reimbursements.rent = Decimal("0.00")
    budget_dict["2021"]["October"] = budget_spending

    budget_spending = BudgetSpending("November 2021")
    budget_spending.needs.car_insurance = Decimal("142.80")
    budget_spending.needs.dental_insurance = Decimal("0.00")
    budget_spending.needs.electric_bill = Decimal("32.24")
    budget_spending.needs.emergencies = Decimal("0.00")
    budget_spending.needs.gasoline = Decimal("140.55")
    budget_spending.needs.groceries = Decimal("46.74")
    budget_spending.needs.health_insurance = Decimal("0.00")
    budget_spending.needs.internet_bill = Decimal("83.99")
    budget_spending.needs.laundry = Decimal("0.00")
    budget_spending.needs.misc = Decimal("239.00")
    budget_spending.needs.mortgage = Decimal("0.00")
    budget_spending.needs.other_insurance = Decimal("0.00")
    budget_spending.needs.rent = Decimal("1117.60")
    budget_spending.needs.renters_insurance = Decimal("59.50")
    budget_spending.needs.student_loans = Decimal("308.05")
    budget_spending.needs.taxes = Decimal("0.00")
    budget_spending.needs.vision_insurance = Decimal("0.00")
    budget_spending.wants.free_spending = Decimal("1086.27")
    budget_spending.wants.misc = Decimal("0.00")
    budget_spending.wants.subscriptions = Decimal("174.47")
    budget_spending.wants.vacation_spending = Decimal("395.08")
    budget_spending.savings.crypto = Decimal("200.00")
    budget_spending.savings.emergency_fund = Decimal("0.00")
    budget_spending.savings.investing = Decimal("400.00")
    budget_spending.savings.misc = Decimal("0.00")
    budget_spending.savings.retirement = Decimal("0.00")
    budget_spending.income.earnings = Decimal("5403.12")
    budget_spending.income.tax_returns = Decimal("0.00")
    budget_spending.reimbursements.bills = Decimal("85.37")
    budget_spending.reimbursements.credit_card_rewards = Decimal("0.00")
    budget_spending.reimbursements.free_spending = Decimal("0.00")
    budget_spending.reimbursements.rent = Decimal("0.00")
    budget_dict["2021"]["November"] = budget_spending

    budget_spending = BudgetSpending("December 2021")
    budget_spending.needs.car_insurance = Decimal("142.80")
    budget_spending.needs.dental_insurance = Decimal("0.00")
    budget_spending.needs.electric_bill = Decimal("63.49")
    budget_spending.needs.emergencies = Decimal("0.00")
    budget_spending.needs.gasoline = Decimal("182.21")
    budget_spending.needs.groceries = Decimal("199.64")
    budget_spending.needs.health_insurance = Decimal("0.00")
    budget_spending.needs.internet_bill = Decimal("83.99")
    budget_spending.needs.laundry = Decimal("0.00")
    budget_spending.needs.misc = Decimal("0.00")
    budget_spending.needs.mortgage = Decimal("0.00")
    budget_spending.needs.other_insurance = Decimal("0.00")
    budget_spending.needs.rent = Decimal("1119.20")
    budget_spending.needs.renters_insurance = Decimal("0.00")
    budget_spending.needs.student_loans = Decimal("308.05")
    budget_spending.needs.taxes = Decimal("0.00")
    budget_spending.needs.vision_insurance = Decimal("0.00")
    budget_spending.wants.free_spending = Decimal("1144.55")
    budget_spending.wants.misc = Decimal("0.00")
    budget_spending.wants.subscriptions = Decimal("174.47")
    budget_spending.wants.vacation_spending = Decimal("387.01")
    budget_spending.savings.crypto = Decimal("250.00")
    budget_spending.savings.emergency_fund = Decimal("0.00")
    budget_spending.savings.investing = Decimal("400.00")
    budget_spending.savings.misc = Decimal("0.00")
    budget_spending.savings.retirement = Decimal("0.00")
    budget_spending.income.earnings = Decimal("3284.39")
    budget_spending.income.tax_returns = Decimal("0.00")
    budget_spending.reimbursements.bills = Decimal("143.73")
    budget_spending.reimbursements.credit_card_rewards = Decimal("0.00")
    budget_spending.reimbursements.free_spending = Decimal("0.00")
    budget_spending.reimbursements.rent = Decimal("0.00")
    budget_dict["2021"]["December"] = budget_spending

    budget_spending = BudgetSpending("January 2022")
    budget_spending.needs.car_insurance = Decimal("142.80")
    budget_spending.needs.dental_insurance = Decimal("0.00")
    budget_spending.needs.electric_bill = Decimal("66.39")
    budget_spending.needs.emergencies = Decimal("0.00")
    budget_spending.needs.gasoline = Decimal("77.22")
    budget_spending.needs.groceries = Decimal("102.35")
    budget_spending.needs.health_insurance = Decimal("0.00")
    budget_spending.needs.internet_bill = Decimal("83.99")
    budget_spending.needs.laundry = Decimal("15.00")
    budget_spending.needs.misc = Decimal("0.00")
    budget_spending.needs.mortgage = Decimal("0.00")
    budget_spending.needs.other_insurance = Decimal("0.00")
    budget_spending.needs.rent = Decimal("1121.51")
    budget_spending.needs.renters_insurance = Decimal("0.00")
    budget_spending.needs.student_loans = Decimal("308.05")
    budget_spending.needs.taxes = Decimal("0.00")
    budget_spending.needs.vision_insurance = Decimal("0.00")
    budget_spending.wants.free_spending = Decimal("807.58")
    budget_spending.wants.misc = Decimal("0.00")
    budget_spending.wants.subscriptions = Decimal("174.47")
    budget_spending.wants.vacation_spending = Decimal("0.00")
    budget_spending.savings.crypto = Decimal("0.00")
    budget_spending.savings.emergency_fund = Decimal("0.00")
    budget_spending.savings.investing = Decimal("0.00")
    budget_spending.savings.misc = Decimal("0.00")
    budget_spending.savings.retirement = Decimal("600.00")
    budget_spending.income.earnings = Decimal("3268.62")
    budget_spending.income.tax_returns = Decimal("0.00")
    budget_spending.reimbursements.bills = Decimal("75.19")
    budget_spending.reimbursements.credit_card_rewards = Decimal("0.00")
    budget_spending.reimbursements.free_spending = Decimal("0.00")
    budget_spending.reimbursements.rent = Decimal("0.00")
    budget_dict["2022"]["January"] = budget_spending

    budget_spending = BudgetSpending("February 2022")
    budget_spending.needs.car_insurance = Decimal("143.88")
    budget_spending.needs.dental_insurance = Decimal("0.00")
    budget_spending.needs.electric_bill = Decimal("86.68")
    budget_spending.needs.emergencies = Decimal("0.00")
    budget_spending.needs.gasoline = Decimal("203.01")
    budget_spending.needs.groceries = Decimal("378.03")
    budget_spending.needs.health_insurance = Decimal("0.00")
    budget_spending.needs.internet_bill = Decimal("83.99")
    budget_spending.needs.laundry = Decimal("0.00")
    budget_spending.needs.misc = Decimal("0.00")
    budget_spending.needs.mortgage = Decimal("0.00")
    budget_spending.needs.other_insurance = Decimal("0.00")
    budget_spending.needs.rent = Decimal("1120.61")
    budget_spending.needs.renters_insurance = Decimal("59.50")
    budget_spending.needs.student_loans = Decimal("308.05")
    budget_spending.needs.taxes = Decimal("0.00")
    budget_spending.needs.vision_insurance = Decimal("0.00")
    budget_spending.wants.free_spending = Decimal("1159.57")
    budget_spending.wants.misc = Decimal("0.00")
    budget_spending.wants.subscriptions = Decimal("223.47")
    budget_spending.wants.vacation_spending = Decimal("0.00")
    budget_spending.savings.crypto = Decimal("0.00")
    budget_spending.savings.emergency_fund = Decimal("435.02")
    budget_spending.savings.investing = Decimal("400.00")
    budget_spending.savings.misc = Decimal("0.00")
    budget_spending.savings.retirement = Decimal("0.00")
    budget_spending.income.earnings = Decimal("6688.96")
    budget_spending.income.tax_returns = Decimal("0.00")
    budget_spending.reimbursements.bills = Decimal("112.80")
    budget_spending.reimbursements.credit_card_rewards = Decimal("0.00")
    budget_spending.reimbursements.free_spending = Decimal("0.00")
    budget_spending.reimbursements.rent = Decimal("0.00")
    budget_dict["2022"]["February"] = budget_spending

    budget_spending = BudgetSpending("March 2022")
    budget_spending.needs.car_insurance = Decimal("142.80")
    budget_spending.needs.dental_insurance = Decimal("0.00")
    budget_spending.needs.electric_bill = Decimal("86.80")
    budget_spending.needs.emergencies = Decimal("0.00")
    budget_spending.needs.gasoline = Decimal("177.51")
    budget_spending.needs.groceries = Decimal("127.99")
    budget_spending.needs.health_insurance = Decimal("0.00")
    budget_spending.needs.internet_bill = Decimal("83.99")
    budget_spending.needs.laundry = Decimal("0.00")
    budget_spending.needs.misc = Decimal("0.00")
    budget_spending.needs.mortgage = Decimal("0.00")
    budget_spending.needs.other_insurance = Decimal("0.00")
    budget_spending.needs.rent = Decimal("1121.21")
    budget_spending.needs.renters_insurance = Decimal("0.00")
    budget_spending.needs.student_loans = Decimal("308.05")
    budget_spending.needs.taxes = Decimal("0.00")
    budget_spending.needs.vision_insurance = Decimal("0.00")
    budget_spending.wants.free_spending = Decimal("655.37")
    budget_spending.wants.misc = Decimal("0.00")
    budget_spending.wants.subscriptions = Decimal("174.47")
    budget_spending.wants.vacation_spending = Decimal("2918.93")
    budget_spending.savings.crypto = Decimal("0.00")
    budget_spending.savings.emergency_fund = Decimal("0.00")
    budget_spending.savings.investing = Decimal("0.00")
    budget_spending.savings.misc = Decimal("0.00")
    budget_spending.savings.retirement = Decimal("0.00")
    budget_spending.income.earnings = Decimal("1466.58")
    budget_spending.income.tax_returns = Decimal("0.00")
    budget_spending.reimbursements.bills = Decimal("85.39")
    budget_spending.reimbursements.credit_card_rewards = Decimal("116.74")
    budget_spending.reimbursements.free_spending = Decimal("0.00")
    budget_spending.reimbursements.rent = Decimal("0.00")
    budget_dict["2022"]["March"] = budget_spending

    budget_spending = BudgetSpending("April 2022")
    budget_spending.needs.car_insurance = Decimal("142.80")
    budget_spending.needs.dental_insurance = Decimal("0.00")
    budget_spending.needs.electric_bill = Decimal("57.64")
    budget_spending.needs.emergencies = Decimal("0.00")
    budget_spending.needs.gasoline = Decimal("213.25")
    budget_spending.needs.groceries = Decimal("318.11")
    budget_spending.needs.health_insurance = Decimal("0.00")
    budget_spending.needs.internet_bill = Decimal("83.99")
    budget_spending.needs.laundry = Decimal("0.00")
    budget_spending.needs.misc = Decimal("0.00")
    budget_spending.needs.mortgage = Decimal("0.00")
    budget_spending.needs.other_insurance = Decimal("0.00")
    budget_spending.needs.rent = Decimal("1120.78")
    budget_spending.needs.renters_insurance = Decimal("0.00")
    budget_spending.needs.student_loans = Decimal("308.05")
    budget_spending.needs.taxes = Decimal("418.00")
    budget_spending.needs.vision_insurance = Decimal("0.00")
    budget_spending.wants.free_spending = Decimal("1033.44")
    budget_spending.wants.misc = Decimal("0.00")
    budget_spending.wants.subscriptions = Decimal("238.97")
    budget_spending.wants.vacation_spending = Decimal("0.00")
    budget_spending.savings.crypto = Decimal("0.00")
    budget_spending.savings.emergency_fund = Decimal("1636.87")
    budget_spending.savings.investing = Decimal("1471.81")
    budget_spending.savings.misc = Decimal("0.00")
    budget_spending.savings.retirement = Decimal("0.00")
    budget_spending.income.earnings = Decimal("9319.97")
    budget_spending.income.tax_returns = Decimal("0.00")
    budget_spending.reimbursements.bills = Decimal("70.81")
    budget_spending.reimbursements.credit_card_rewards = Decimal("0.00")
    budget_spending.reimbursements.free_spending = Decimal("0.00")
    budget_spending.reimbursements.rent = Decimal("0.00")
    budget_dict["2022"]["April"] = budget_spending

    budget_spending = BudgetSpending("May 2022")
    budget_spending.needs.car_insurance = Decimal("142.80")
    budget_spending.needs.dental_insurance = Decimal("0.00")
    budget_spending.needs.electric_bill = Decimal("6.66")
    budget_spending.needs.emergencies = Decimal("0.00")
    budget_spending.needs.gasoline = Decimal("227.30")
    budget_spending.needs.groceries = Decimal("405.57")
    budget_spending.needs.health_insurance = Decimal("0.00")
    budget_spending.needs.internet_bill = Decimal("83.99")
    budget_spending.needs.laundry = Decimal("10.00")
    budget_spending.needs.misc = Decimal("0.00")
    budget_spending.needs.mortgage = Decimal("0.00")
    budget_spending.needs.other_insurance = Decimal("0.00")
    budget_spending.needs.rent = Decimal("1121.70")
    budget_spending.needs.renters_insurance = Decimal("59.50")
    budget_spending.needs.student_loans = Decimal("308.05")
    budget_spending.needs.taxes = Decimal("0.00")
    budget_spending.needs.vision_insurance = Decimal("0.00")
    budget_spending.wants.free_spending = Decimal("1080.12")
    budget_spending.wants.misc = Decimal("0.00")
    budget_spending.wants.subscriptions = Decimal("313.16")
    budget_spending.wants.vacation_spending = Decimal("0.00")
    budget_spending.savings.crypto = Decimal("0.00")
    budget_spending.savings.emergency_fund = Decimal("600.00")
    budget_spending.savings.investing = Decimal("500.00")
    budget_spending.savings.misc = Decimal("0.00")
    budget_spending.savings.retirement = Decimal("0.00")
    budget_spending.income.earnings = Decimal("4065.55")
    budget_spending.income.tax_returns = Decimal("0.00")
    budget_spending.reimbursements.bills = Decimal("75.07")
    budget_spending.reimbursements.credit_card_rewards = Decimal("0.00")
    budget_spending.reimbursements.free_spending = Decimal("0.00")
    budget_spending.reimbursements.rent = Decimal("0.00")
    budget_dict["2022"]["May"] = budget_spending

    budget_spending = BudgetSpending("June 2022")
    budget_spending.needs.car_insurance = Decimal("142.80")
    budget_spending.needs.dental_insurance = Decimal("0.00")
    budget_spending.needs.electric_bill = Decimal("65.26")
    budget_spending.needs.emergencies = Decimal("1006.15")
    budget_spending.needs.gasoline = Decimal("278.63")
    budget_spending.needs.groceries = Decimal("576.01")
    budget_spending.needs.health_insurance = Decimal("0.00")
    budget_spending.needs.internet_bill = Decimal("83.99")
    budget_spending.needs.laundry = Decimal("0.00")
    budget_spending.needs.misc = Decimal("0.00")
    budget_spending.needs.mortgage = Decimal("0.00")
    budget_spending.needs.other_insurance = Decimal("0.00")
    budget_spending.needs.rent = Decimal("1114.01")
    budget_spending.needs.renters_insurance = Decimal("0.00")
    budget_spending.needs.student_loans = Decimal("308.05")
    budget_spending.needs.taxes = Decimal("0.00")
    budget_spending.needs.vision_insurance = Decimal("0.00")
    budget_spending.wants.free_spending = Decimal("661.48")
    budget_spending.wants.misc = Decimal("0.00")
    budget_spending.wants.subscriptions = Decimal("325.15")
    budget_spending.wants.vacation_spending = Decimal("0.00")
    budget_spending.savings.crypto = Decimal("0.00")
    budget_spending.savings.emergency_fund = Decimal("550.00")
    budget_spending.savings.investing = Decimal("450.00")
    budget_spending.savings.misc = Decimal("0.00")
    budget_spending.savings.retirement = Decimal("0.00")
    budget_spending.income.earnings = Decimal("4093.67")
    budget_spending.income.tax_returns = Decimal("0.00")
    budget_spending.reimbursements.bills = Decimal("74.62")
    budget_spending.reimbursements.credit_card_rewards = Decimal("92.05")
    budget_spending.reimbursements.free_spending = Decimal("0.00")
    budget_spending.reimbursements.rent = Decimal("0.00")
    budget_dict["2022"]["June"] = budget_spending

    budget_spending = BudgetSpending("July 2022")
    budget_spending.needs.car_insurance = Decimal("142.80")
    budget_spending.needs.dental_insurance = Decimal("0.00")
    budget_spending.needs.electric_bill = Decimal("114.37")
    budget_spending.needs.emergencies = Decimal("0.00")
    budget_spending.needs.gasoline = Decimal("417.16")
    budget_spending.needs.groceries = Decimal("394.67")
    budget_spending.needs.health_insurance = Decimal("0.00")
    budget_spending.needs.internet_bill = Decimal("83.99")
    budget_spending.needs.laundry = Decimal("0.00")
    budget_spending.needs.misc = Decimal("0.00")
    budget_spending.needs.mortgage = Decimal("0.00")
    budget_spending.needs.other_insurance = Decimal("0.00")
    budget_spending.needs.rent = Decimal("1123.02")
    budget_spending.needs.renters_insurance = Decimal("0.00")
    budget_spending.needs.student_loans = Decimal("308.05")
    budget_spending.needs.taxes = Decimal("0.00")
    budget_spending.needs.vision_insurance = Decimal("0.00")
    budget_spending.wants.free_spending = Decimal("832.97")
    budget_spending.wants.misc = Decimal("0.00")
    budget_spending.wants.subscriptions = Decimal("325.15")
    budget_spending.wants.vacation_spending = Decimal("266.00")
    budget_spending.savings.crypto = Decimal("0.00")
    budget_spending.savings.emergency_fund = Decimal("500.00")
    budget_spending.savings.investing = Decimal("200.00")
    budget_spending.savings.misc = Decimal("0.00")
    budget_spending.savings.retirement = Decimal("0.00")
    budget_spending.income.earnings = Decimal("4022.03")
    budget_spending.income.tax_returns = Decimal("0.00")
    budget_spending.reimbursements.bills = Decimal("99.18")
    budget_spending.reimbursements.credit_card_rewards = Decimal("0.00")
    budget_spending.reimbursements.free_spending = Decimal("12.00")
    budget_spending.reimbursements.rent = Decimal("0.00")
    budget_dict["2022"]["July"] = budget_spending

    budget_spending = BudgetSpending("August 2022")
    budget_spending.needs.car_insurance = Decimal("146.88")
    budget_spending.needs.dental_insurance = Decimal("0.00")
    budget_spending.needs.electric_bill = Decimal("118.86")
    budget_spending.needs.emergencies = Decimal("0.00")
    budget_spending.needs.gasoline = Decimal("196.85")
    budget_spending.needs.groceries = Decimal("417.54")
    budget_spending.needs.health_insurance = Decimal("0.00")
    budget_spending.needs.internet_bill = Decimal("83.99")
    budget_spending.needs.laundry = Decimal("20.00")
    budget_spending.needs.misc = Decimal("542.00")
    budget_spending.needs.mortgage = Decimal("0.00")
    budget_spending.needs.other_insurance = Decimal("0.00")
    budget_spending.needs.rent = Decimal("1667.05")
    budget_spending.needs.renters_insurance = Decimal("59.50")
    budget_spending.needs.student_loans = Decimal("300.00")
    budget_spending.needs.taxes = Decimal("0.00")
    budget_spending.needs.vision_insurance = Decimal("0.00")
    budget_spending.wants.free_spending = Decimal("1069.49")
    budget_spending.wants.misc = Decimal("0.00")
    budget_spending.wants.subscriptions = Decimal("328.15")
    budget_spending.wants.vacation_spending = Decimal("0.00")
    budget_spending.savings.crypto = Decimal("0.00")
    budget_spending.savings.emergency_fund = Decimal("500.00")
    budget_spending.savings.investing = Decimal("0.00")
    budget_spending.savings.misc = Decimal("0.00")
    budget_spending.savings.retirement = Decimal("0.00")
    budget_spending.income.earnings = Decimal("4287.17")
    budget_spending.income.tax_returns = Decimal("0.00")
    budget_spending.reimbursements.bills = Decimal("0.00")
    budget_spending.reimbursements.credit_card_rewards = Decimal("0.00")
    budget_spending.reimbursements.free_spending = Decimal("550.00")
    budget_spending.reimbursements.rent = Decimal("0.00")
    budget_dict["2022"]["August"] = budget_spending

    budget_spending = BudgetSpending("September 2022")
    budget_spending.needs.car_insurance = Decimal("145.60")
    budget_spending.needs.dental_insurance = Decimal("0.00")
    budget_spending.needs.electric_bill = Decimal("110.56")
    budget_spending.needs.emergencies = Decimal("0.00")
    budget_spending.needs.gasoline = Decimal("249.06")
    budget_spending.needs.groceries = Decimal("414.80")
    budget_spending.needs.health_insurance = Decimal("0.00")
    budget_spending.needs.internet_bill = Decimal("83.99")
    budget_spending.needs.laundry = Decimal("25.00")
    budget_spending.needs.misc = Decimal("0.00")
    budget_spending.needs.mortgage = Decimal("0.00")
    budget_spending.needs.other_insurance = Decimal("0.00")
    budget_spending.needs.rent = Decimal("2252.12")
    budget_spending.needs.renters_insurance = Decimal("0.00")
    budget_spending.needs.student_loans = Decimal("0.00")
    budget_spending.needs.taxes = Decimal("0.00")
    budget_spending.needs.vision_insurance = Decimal("0.00")
    budget_spending.wants.free_spending = Decimal("1437.87")
    budget_spending.wants.misc = Decimal("0.00")
    budget_spending.wants.subscriptions = Decimal("343.23")
    budget_spending.wants.vacation_spending = Decimal("388.55")
    budget_spending.savings.crypto = Decimal("0.00")
    budget_spending.savings.emergency_fund = Decimal("1400.00")
    budget_spending.savings.investing = Decimal("0.00")
    budget_spending.savings.misc = Decimal("0.00")
    budget_spending.savings.retirement = Decimal("0.00")
    budget_spending.income.earnings = Decimal("7852.29")
    budget_spending.income.tax_returns = Decimal("0.00")
    budget_spending.reimbursements.bills = Decimal("0.00")
    budget_spending.reimbursements.credit_card_rewards = Decimal("0.00")
    budget_spending.reimbursements.free_spending = Decimal("235.75")
    budget_spending.reimbursements.rent = Decimal("300.00")
    budget_dict["2022"]["September"] = budget_spending

    budget_spending = BudgetSpending("October 2022")
    budget_spending.needs.car_insurance = Decimal("145.60")
    budget_spending.needs.dental_insurance = Decimal("0.00")
    budget_spending.needs.electric_bill = Decimal("103.78")
    budget_spending.needs.emergencies = Decimal("0.00")
    budget_spending.needs.gasoline = Decimal("146.84")
    budget_spending.needs.groceries = Decimal("516.67")
    budget_spending.needs.health_insurance = Decimal("0.00")
    budget_spending.needs.internet_bill = Decimal("83.99")
    budget_spending.needs.laundry = Decimal("60.00")
    budget_spending.needs.misc = Decimal("0.00")
    budget_spending.needs.mortgage = Decimal("0.00")
    budget_spending.needs.other_insurance = Decimal("0.00")
    budget_spending.needs.rent = Decimal("2271.49")
    budget_spending.needs.renters_insurance = Decimal("0.00")
    budget_spending.needs.student_loans = Decimal("0.00")
    budget_spending.needs.taxes = Decimal("0.00")
    budget_spending.needs.vision_insurance = Decimal("0.00")
    budget_spending.wants.free_spending = Decimal("1623.82")
    budget_spending.wants.misc = Decimal("0.00")
    budget_spending.wants.subscriptions = Decimal("341.65")
    budget_spending.wants.vacation_spending = Decimal("812.20")
    budget_spending.savings.crypto = Decimal("0.00")
    budget_spending.savings.emergency_fund = Decimal("300.00")
    budget_spending.savings.investing = Decimal("0.00")
    budget_spending.savings.misc = Decimal("0.00")
    budget_spending.savings.retirement = Decimal("0.00")
    budget_spending.income.earnings = Decimal("4197.21")
    budget_spending.income.tax_returns = Decimal("0.00")
    budget_spending.reimbursements.bills = Decimal("93.88")
    budget_spending.reimbursements.credit_card_rewards = Decimal("217.55")
    budget_spending.reimbursements.free_spending = Decimal("86.00")
    budget_spending.reimbursements.rent = Decimal("600.00")
    budget_dict["2022"]["October"] = budget_spending

    budget_spending = BudgetSpending("November 2022")
    budget_spending.needs.car_insurance = Decimal("145.60")
    budget_spending.needs.dental_insurance = Decimal("0.00")
    budget_spending.needs.electric_bill = Decimal("19.95")
    budget_spending.needs.emergencies = Decimal("400.00")
    budget_spending.needs.gasoline = Decimal("240.64")
    budget_spending.needs.groceries = Decimal("420.69")
    budget_spending.needs.health_insurance = Decimal("0.00")
    budget_spending.needs.internet_bill = Decimal("83.99")
    budget_spending.needs.laundry = Decimal("25.00")
    budget_spending.needs.misc = Decimal("229.00")
    budget_spending.needs.mortgage = Decimal("0.00")
    budget_spending.needs.other_insurance = Decimal("0.00")
    budget_spending.needs.rent = Decimal("2252.00")
    budget_spending.needs.renters_insurance = Decimal("59.50")
    budget_spending.needs.student_loans = Decimal("0.00")
    budget_spending.needs.taxes = Decimal("0.00")
    budget_spending.needs.vision_insurance = Decimal("0.00")
    budget_spending.wants.free_spending = Decimal("1022.15")
    budget_spending.wants.misc = Decimal("0.00")
    budget_spending.wants.subscriptions = Decimal("341.65")
    budget_spending.wants.vacation_spending = Decimal("0.00")
    budget_spending.savings.crypto = Decimal("0.00")
    budget_spending.savings.emergency_fund = Decimal("0.00")
    budget_spending.savings.investing = Decimal("0.00")
    budget_spending.savings.misc = Decimal("0.00")
    budget_spending.savings.retirement = Decimal("0.00")
    budget_spending.income.earnings = Decimal("4183.77")
    budget_spending.income.tax_returns = Decimal("0.00")
    budget_spending.reimbursements.bills = Decimal("51.97")
    budget_spending.reimbursements.credit_card_rewards = Decimal("0.00")
    budget_spending.reimbursements.free_spending = Decimal("236.00")
    budget_spending.reimbursements.rent = Decimal("645.00")
    budget_dict["2022"]["November"] = budget_spending

    budget_spending = BudgetSpending("December 2022")
    budget_spending.needs.car_insurance = Decimal("145.60")
    budget_spending.needs.dental_insurance = Decimal("0.00")
    budget_spending.needs.electric_bill = Decimal("117.35")
    budget_spending.needs.emergencies = Decimal("0.00")
    budget_spending.needs.gasoline = Decimal("67.84")
    budget_spending.needs.groceries = Decimal("578.81")
    budget_spending.needs.health_insurance = Decimal("0.00")
    budget_spending.needs.internet_bill = Decimal("83.99")
    budget_spending.needs.laundry = Decimal("50.00")
    budget_spending.needs.misc = Decimal("0.00")
    budget_spending.needs.mortgage = Decimal("0.00")
    budget_spending.needs.other_insurance = Decimal("0.00")
    budget_spending.needs.rent = Decimal("2248.86")
    budget_spending.needs.renters_insurance = Decimal("0.00")
    budget_spending.needs.student_loans = Decimal("0.00")
    budget_spending.needs.taxes = Decimal("0.00")
    budget_spending.needs.vision_insurance = Decimal("0.00")
    budget_spending.wants.free_spending = Decimal("864.07")
    budget_spending.wants.misc = Decimal("0.00")
    budget_spending.wants.subscriptions = Decimal("347.62")
    budget_spending.wants.vacation_spending = Decimal("1699.82")
    budget_spending.savings.crypto = Decimal("0.00")
    budget_spending.savings.emergency_fund = Decimal("0.00")
    budget_spending.savings.investing = Decimal("0.00")
    budget_spending.savings.misc = Decimal("0.00")
    budget_spending.savings.retirement = Decimal("0.00")
    budget_spending.income.earnings = Decimal("4180.64")
    budget_spending.income.tax_returns = Decimal("250.00")
    budget_spending.reimbursements.bills = Decimal("100.67")
    budget_spending.reimbursements.credit_card_rewards = Decimal("215.10")
    budget_spending.reimbursements.free_spending = Decimal("100.00")
    budget_spending.reimbursements.rent = Decimal("645.00")
    budget_dict["2022"]["December"] = budget_spending

    budget_spending = BudgetSpending("January 2023")
    budget_spending.needs.car_insurance = Decimal("145.60")
    budget_spending.needs.dental_insurance = Decimal("0.00")
    budget_spending.needs.electric_bill = Decimal("152.69")
    budget_spending.needs.emergencies = Decimal("0.00")
    budget_spending.needs.gasoline = Decimal("56.11")
    budget_spending.needs.groceries = Decimal("320.00")
    budget_spending.needs.health_insurance = Decimal("0.00")
    budget_spending.needs.internet_bill = Decimal("89.99")
    budget_spending.needs.laundry = Decimal("50.00")
    budget_spending.needs.misc = Decimal("0.00")
    budget_spending.needs.mortgage = Decimal("0.00")
    budget_spending.needs.other_insurance = Decimal("0.00")
    budget_spending.needs.rent = Decimal("2379.21")
    budget_spending.needs.renters_insurance = Decimal("0.00")
    budget_spending.needs.student_loans = Decimal("0.00")
    budget_spending.needs.taxes = Decimal("0.00")
    budget_spending.needs.vision_insurance = Decimal("0.00")
    budget_spending.wants.free_spending = Decimal("1305.19")
    budget_spending.wants.misc = Decimal("0.00")
    budget_spending.wants.subscriptions = Decimal("347.62")
    budget_spending.wants.vacation_spending = Decimal("0.00")
    budget_spending.savings.crypto = Decimal("0.00")
    budget_spending.savings.emergency_fund = Decimal("0.00")
    budget_spending.savings.investing = Decimal("100.00")
    budget_spending.savings.misc = Decimal("0.00")
    budget_spending.savings.retirement = Decimal("700.00")
    budget_spending.income.earnings = Decimal("4416.51")
    budget_spending.income.tax_returns = Decimal("0.00")
    budget_spending.reimbursements.bills = Decimal("118.34")
    budget_spending.reimbursements.credit_card_rewards = Decimal("0.00")
    budget_spending.reimbursements.free_spending = Decimal("20.00")
    budget_spending.reimbursements.rent = Decimal("645.00")
    budget_dict["2023"]["January"] = budget_spending

    budget_spending = BudgetSpending("February 2023")
    budget_spending.needs.car_insurance = Decimal("146.88")
    budget_spending.needs.dental_insurance = Decimal("0.00")
    budget_spending.needs.electric_bill = Decimal("159.28")
    budget_spending.needs.emergencies = Decimal("208.18")
    budget_spending.needs.gasoline = Decimal("244.93")
    budget_spending.needs.groceries = Decimal("506.95")
    budget_spending.needs.health_insurance = Decimal("0.00")
    budget_spending.needs.internet_bill = Decimal("67.99")
    budget_spending.needs.laundry = Decimal("60.00")
    budget_spending.needs.misc = Decimal("0.00")
    budget_spending.needs.mortgage = Decimal("0.00")
    budget_spending.needs.other_insurance = Decimal("0.00")
    budget_spending.needs.rent = Decimal("2380.08")
    budget_spending.needs.renters_insurance = Decimal("59.50")
    budget_spending.needs.student_loans = Decimal("0.00")
    budget_spending.needs.taxes = Decimal("0.00")
    budget_spending.needs.vision_insurance = Decimal("0.00")
    budget_spending.wants.free_spending = Decimal("551.71")
    budget_spending.wants.misc = Decimal("0.00")
    budget_spending.wants.subscriptions = Decimal("348.62")
    budget_spending.wants.vacation_spending = Decimal("459.49")
    budget_spending.savings.crypto = Decimal("0.00")
    budget_spending.savings.emergency_fund = Decimal("0.00")
    budget_spending.savings.investing = Decimal("50.00")
    budget_spending.savings.misc = Decimal("0.00")
    budget_spending.savings.retirement = Decimal("699.62")
    budget_spending.income.earnings = Decimal("4621.67")
    budget_spending.income.tax_returns = Decimal("0.00")
    budget_spending.reimbursements.bills = Decimal("114.63")
    budget_spending.reimbursements.credit_card_rewards = Decimal("0.00")
    budget_spending.reimbursements.free_spending = Decimal("180.65")
    budget_spending.reimbursements.rent = Decimal("645.00")
    budget_dict["2023"]["February"] = budget_spending

    budget_spending = BudgetSpending("March 2023")
    budget_spending.needs.car_insurance = Decimal("145.60")
    budget_spending.needs.dental_insurance = Decimal("0.00")
    budget_spending.needs.electric_bill = Decimal("207.71")
    budget_spending.needs.emergencies = Decimal("0.00")
    budget_spending.needs.gasoline = Decimal("168.53")
    budget_spending.needs.groceries = Decimal("319.93")
    budget_spending.needs.health_insurance = Decimal("0.00")
    budget_spending.needs.internet_bill = Decimal("69.99")
    budget_spending.needs.laundry = Decimal("50.00")
    budget_spending.needs.misc = Decimal("0.00")
    budget_spending.needs.mortgage = Decimal("0.00")
    budget_spending.needs.other_insurance = Decimal("0.00")
    budget_spending.needs.rent = Decimal("2384.22")
    budget_spending.needs.renters_insurance = Decimal("0.00")
    budget_spending.needs.student_loans = Decimal("0.00")
    budget_spending.needs.taxes = Decimal("450.00")
    budget_spending.needs.vision_insurance = Decimal("0.00")
    budget_spending.wants.free_spending = Decimal("1456.69")
    budget_spending.wants.misc = Decimal("0.00")
    budget_spending.wants.subscriptions = Decimal("348.62")
    budget_spending.wants.vacation_spending = Decimal("1046.16")
    budget_spending.savings.crypto = Decimal("0.00")
    budget_spending.savings.emergency_fund = Decimal("0.00")
    budget_spending.savings.investing = Decimal("0.00")
    budget_spending.savings.misc = Decimal("0.00")
    budget_spending.savings.retirement = Decimal("700.00")
    budget_spending.income.earnings = Decimal("6066.15")
    budget_spending.income.tax_returns = Decimal("0.00")
    budget_spending.reimbursements.bills = Decimal("0.00")
    budget_spending.reimbursements.credit_card_rewards = Decimal("133.41")
    budget_spending.reimbursements.free_spending = Decimal("42.00")
    budget_spending.reimbursements.rent = Decimal("645.00")
    budget_dict["2023"]["March"] = budget_spending

    budget_spending = BudgetSpending("April 2023")
    budget_spending.needs.car_insurance = Decimal("145.60")
    budget_spending.needs.dental_insurance = Decimal("0.00")
    budget_spending.needs.electric_bill = Decimal("16.35")
    budget_spending.needs.emergencies = Decimal("286.77")
    budget_spending.needs.gasoline = Decimal("68.32")
    budget_spending.needs.groceries = Decimal("537.51")
    budget_spending.needs.health_insurance = Decimal("0.00")
    budget_spending.needs.internet_bill = Decimal("69.99")
    budget_spending.needs.laundry = Decimal("60.00")
    budget_spending.needs.misc = Decimal("0.00")
    budget_spending.needs.mortgage = Decimal("0.00")
    budget_spending.needs.other_insurance = Decimal("0.00")
    budget_spending.needs.rent = Decimal("2380.70")
    budget_spending.needs.renters_insurance = Decimal("0.00")
    budget_spending.needs.student_loans = Decimal("0.00")
    budget_spending.needs.taxes = Decimal("1103.00")
    budget_spending.needs.vision_insurance = Decimal("0.00")
    budget_spending.wants.free_spending = Decimal("1072.70")
    budget_spending.wants.misc = Decimal("0.00")
    budget_spending.wants.subscriptions = Decimal("348.62")
    budget_spending.wants.vacation_spending = Decimal("274.00")
    budget_spending.savings.crypto = Decimal("0.00")
    budget_spending.savings.emergency_fund = Decimal("0.00")
    budget_spending.savings.investing = Decimal("0.00")
    budget_spending.savings.misc = Decimal("0.00")
    budget_spending.savings.retirement = Decimal("700.00")
    budget_spending.income.earnings = Decimal("4767.83")
    budget_spending.income.tax_returns = Decimal("385.00")
    budget_spending.reimbursements.bills = Decimal("40.17")
    budget_spending.reimbursements.credit_card_rewards = Decimal("0.00")
    budget_spending.reimbursements.free_spending = Decimal("0.00")
    budget_spending.reimbursements.rent = Decimal("645.00")
    budget_dict["2023"]["April"] = budget_spending

    return budget_dict


def get_expected_data_points1():
    """Returns the expected data points dictionary pertaining to data from /tests/files/spending1.tsv"""

    expected_data_points_dict = {
        "lifetime": {
            "first_date": ("2023", "April"),
            "needs": {
                "car_insurance": [Decimal("145.60")],
                "dental_insurance": [Decimal("0.00")],
                "electric_bill": [Decimal("16.35")],
                "emergencies": [Decimal("125.99")],
                "gasoline": [Decimal("68.32")],
                "groceries": [Decimal("389.44")],
                "health_insurance": [Decimal("0.00")],
                "internet_bill": [Decimal("69.99")],
                "laundry": [Decimal("0.00")],
                "misc": [Decimal("251.98")],
                "mortgage": [Decimal("0.00")],
                "other_insurance": [Decimal("0.00")],
                "rent": [Decimal("2000.00")],
                "renters_insurance": [Decimal("68.32")],
                "student_loans": [Decimal("145.60")],
                "taxes": [Decimal("400.00")],
                "vision_insurance": [Decimal("0.00")],
            },
            "wants": {
                "free_spending": [Decimal("235.93")],
                "misc": [Decimal("44.44")],
                "subscriptions": [Decimal("28.98")],
                "vacation_spending": [Decimal("444.44")],
            },
            "savings": {
                "crypto": [Decimal("110.00")],
                "emergency_fund": [Decimal("200.00")],
                "investing": [Decimal("100.00")],
                "misc": [Decimal("55.55")],
                "retirement": [Decimal("700.00")],
            },
            "income": {"earnings": [Decimal("6000.00")], "tax_returns": [Decimal("500.00")]},
            "reimbursements": {
                "bills": [Decimal("40.00")],
                "credit_card_rewards": [Decimal("13.99")],
                "free_spending": [Decimal("45.60")],
                "rent": [Decimal("1000.00")],
            },
        },
        "2021": {},
        "2022": {},
        "2023": {
            "first_date": ("2023", "April"),
            "needs": {
                "car_insurance": [Decimal("145.60")],
                "dental_insurance": [Decimal("0.00")],
                "electric_bill": [Decimal("16.35")],
                "emergencies": [Decimal("125.99")],
                "gasoline": [Decimal("68.32")],
                "groceries": [Decimal("389.44")],
                "health_insurance": [Decimal("0.00")],
                "internet_bill": [Decimal("69.99")],
                "laundry": [Decimal("0.00")],
                "misc": [Decimal("251.98")],
                "mortgage": [Decimal("0.00")],
                "other_insurance": [Decimal("0.00")],
                "rent": [Decimal("2000.00")],
                "renters_insurance": [Decimal("68.32")],
                "student_loans": [Decimal("145.60")],
                "taxes": [Decimal("400.00")],
                "vision_insurance": [Decimal("0.00")],
            },
            "wants": {
                "free_spending": [Decimal("235.93")],
                "misc": [Decimal("44.44")],
                "subscriptions": [Decimal("28.98")],
                "vacation_spending": [Decimal("444.44")],
            },
            "savings": {
                "crypto": [Decimal("110.00")],
                "emergency_fund": [Decimal("200.00")],
                "investing": [Decimal("100.00")],
                "misc": [Decimal("55.55")],
                "retirement": [Decimal("700.00")],
            },
            "income": {"earnings": [Decimal("6000.00")], "tax_returns": [Decimal("500.00")]},
            "reimbursements": {
                "bills": [Decimal("40.00")],
                "credit_card_rewards": [Decimal("13.99")],
                "free_spending": [Decimal("45.60")],
                "rent": [Decimal("1000.00")],
            },
        },
    }

    return expected_data_points_dict


def get_expected_data_points2():
    """Returns the expected data points dictionary pertaining to data from /tests/files/spending2.tsv"""

    expected_data_points_dict = {
        "lifetime": {
            "first_date": ("2022", "January"),
            "needs": {
                "car_insurance": [
                    Decimal("142.80"),
                    Decimal("143.88"),
                    Decimal("142.80"),
                    Decimal("142.80"),
                    Decimal("142.80"),
                    Decimal("142.80"),
                    Decimal("142.80"),
                    Decimal("146.88"),
                    Decimal("145.60"),
                    Decimal("145.60"),
                    Decimal("145.60"),
                    Decimal("145.60"),
                ],
                "dental_insurance": [
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                ],
                "electric_bill": [
                    Decimal("66.39"),
                    Decimal("86.68"),
                    Decimal("86.80"),
                    Decimal("57.64"),
                    Decimal("6.66"),
                    Decimal("65.26"),
                    Decimal("114.37"),
                    Decimal("118.86"),
                    Decimal("110.56"),
                    Decimal("103.78"),
                    Decimal("19.95"),
                    Decimal("117.35"),
                ],
                "emergencies": [
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("1006.15"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("400.00"),
                    Decimal("0.00"),
                ],
                "gasoline": [
                    Decimal("77.22"),
                    Decimal("203.01"),
                    Decimal("177.51"),
                    Decimal("213.25"),
                    Decimal("227.30"),
                    Decimal("278.63"),
                    Decimal("417.16"),
                    Decimal("196.85"),
                    Decimal("249.06"),
                    Decimal("146.84"),
                    Decimal("240.64"),
                    Decimal("67.84"),
                ],
                "groceries": [
                    Decimal("102.35"),
                    Decimal("378.03"),
                    Decimal("127.99"),
                    Decimal("318.11"),
                    Decimal("405.57"),
                    Decimal("576.01"),
                    Decimal("394.67"),
                    Decimal("417.54"),
                    Decimal("414.80"),
                    Decimal("516.67"),
                    Decimal("420.69"),
                    Decimal("578.81"),
                ],
                "health_insurance": [
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                ],
                "internet_bill": [
                    Decimal("83.99"),
                    Decimal("83.99"),
                    Decimal("83.99"),
                    Decimal("83.99"),
                    Decimal("83.99"),
                    Decimal("83.99"),
                    Decimal("83.99"),
                    Decimal("83.99"),
                    Decimal("83.99"),
                    Decimal("83.99"),
                    Decimal("83.99"),
                    Decimal("83.99"),
                ],
                "laundry": [
                    Decimal("15.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("10.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("20.00"),
                    Decimal("25.00"),
                    Decimal("60.00"),
                    Decimal("25.00"),
                    Decimal("50.00"),
                ],
                "misc": [
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("542.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("229.00"),
                    Decimal("0.00"),
                ],
                "mortgage": [
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                ],
                "other_insurance": [
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                ],
                "rent": [
                    Decimal("1121.51"),
                    Decimal("1120.61"),
                    Decimal("1121.21"),
                    Decimal("1120.78"),
                    Decimal("1121.70"),
                    Decimal("1114.01"),
                    Decimal("1123.02"),
                    Decimal("1667.05"),
                    Decimal("2252.12"),
                    Decimal("2271.49"),
                    Decimal("2252.00"),
                    Decimal("2248.86"),
                ],
                "renters_insurance": [
                    Decimal("0.00"),
                    Decimal("59.50"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("59.50"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("59.50"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("59.50"),
                    Decimal("0.00"),
                ],
                "student_loans": [
                    Decimal("308.05"),
                    Decimal("308.05"),
                    Decimal("308.05"),
                    Decimal("308.05"),
                    Decimal("308.05"),
                    Decimal("308.05"),
                    Decimal("308.05"),
                    Decimal("300.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                ],
                "taxes": [
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("418.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                ],
                "vision_insurance": [
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                ],
            },
            "wants": {
                "free_spending": [
                    Decimal("807.58"),
                    Decimal("1159.57"),
                    Decimal("655.37"),
                    Decimal("1033.44"),
                    Decimal("1080.12"),
                    Decimal("661.48"),
                    Decimal("832.97"),
                    Decimal("1069.49"),
                    Decimal("1437.87"),
                    Decimal("1623.82"),
                    Decimal("1022.15"),
                    Decimal("864.07"),
                ],
                "misc": [
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                ],
                "subscriptions": [
                    Decimal("174.47"),
                    Decimal("223.47"),
                    Decimal("174.47"),
                    Decimal("238.97"),
                    Decimal("313.16"),
                    Decimal("325.15"),
                    Decimal("325.15"),
                    Decimal("328.15"),
                    Decimal("343.23"),
                    Decimal("341.65"),
                    Decimal("341.65"),
                    Decimal("347.62"),
                ],
                "vacation_spending": [
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("2918.93"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("266.00"),
                    Decimal("0.00"),
                    Decimal("388.55"),
                    Decimal("812.20"),
                    Decimal("0.00"),
                    Decimal("1699.82"),
                ],
            },
            "savings": {
                "crypto": [
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                ],
                "emergency_fund": [
                    Decimal("0.00"),
                    Decimal("435.02"),
                    Decimal("0.00"),
                    Decimal("1636.87"),
                    Decimal("600.00"),
                    Decimal("550.00"),
                    Decimal("500.00"),
                    Decimal("500.00"),
                    Decimal("1400.00"),
                    Decimal("300.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                ],
                "investing": [
                    Decimal("0.00"),
                    Decimal("400.00"),
                    Decimal("0.00"),
                    Decimal("1471.81"),
                    Decimal("500.00"),
                    Decimal("450.00"),
                    Decimal("200.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                ],
                "misc": [
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                ],
                "retirement": [
                    Decimal("600.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                ],
            },
            "income": {
                "earnings": [
                    Decimal("3268.62"),
                    Decimal("6688.96"),
                    Decimal("1466.58"),
                    Decimal("9319.97"),
                    Decimal("4065.55"),
                    Decimal("4093.67"),
                    Decimal("4022.03"),
                    Decimal("4287.17"),
                    Decimal("7852.29"),
                    Decimal("4197.21"),
                    Decimal("4183.77"),
                    Decimal("4180.64"),
                ],
                "tax_returns": [
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("250.00"),
                ],
            },
            "reimbursements": {
                "bills": [
                    Decimal("75.19"),
                    Decimal("112.80"),
                    Decimal("85.39"),
                    Decimal("70.81"),
                    Decimal("75.07"),
                    Decimal("74.62"),
                    Decimal("99.18"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("93.88"),
                    Decimal("51.97"),
                    Decimal("100.67"),
                ],
                "credit_card_rewards": [
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("116.74"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("92.05"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("217.55"),
                    Decimal("0.00"),
                    Decimal("215.10"),
                ],
                "free_spending": [
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("12.00"),
                    Decimal("550.00"),
                    Decimal("235.75"),
                    Decimal("86.00"),
                    Decimal("236.00"),
                    Decimal("100.00"),
                ],
                "rent": [
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("300.00"),
                    Decimal("600.00"),
                    Decimal("645.00"),
                    Decimal("645.00"),
                ],
            },
        },
        "2021": {},
        "2022": {
            "first_date": ("2022", "January"),
            "needs": {
                "car_insurance": [
                    Decimal("142.80"),
                    Decimal("143.88"),
                    Decimal("142.80"),
                    Decimal("142.80"),
                    Decimal("142.80"),
                    Decimal("142.80"),
                    Decimal("142.80"),
                    Decimal("146.88"),
                    Decimal("145.60"),
                    Decimal("145.60"),
                    Decimal("145.60"),
                    Decimal("145.60"),
                ],
                "dental_insurance": [
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                ],
                "electric_bill": [
                    Decimal("66.39"),
                    Decimal("86.68"),
                    Decimal("86.80"),
                    Decimal("57.64"),
                    Decimal("6.66"),
                    Decimal("65.26"),
                    Decimal("114.37"),
                    Decimal("118.86"),
                    Decimal("110.56"),
                    Decimal("103.78"),
                    Decimal("19.95"),
                    Decimal("117.35"),
                ],
                "emergencies": [
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("1006.15"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("400.00"),
                    Decimal("0.00"),
                ],
                "gasoline": [
                    Decimal("77.22"),
                    Decimal("203.01"),
                    Decimal("177.51"),
                    Decimal("213.25"),
                    Decimal("227.30"),
                    Decimal("278.63"),
                    Decimal("417.16"),
                    Decimal("196.85"),
                    Decimal("249.06"),
                    Decimal("146.84"),
                    Decimal("240.64"),
                    Decimal("67.84"),
                ],
                "groceries": [
                    Decimal("102.35"),
                    Decimal("378.03"),
                    Decimal("127.99"),
                    Decimal("318.11"),
                    Decimal("405.57"),
                    Decimal("576.01"),
                    Decimal("394.67"),
                    Decimal("417.54"),
                    Decimal("414.80"),
                    Decimal("516.67"),
                    Decimal("420.69"),
                    Decimal("578.81"),
                ],
                "health_insurance": [
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                ],
                "internet_bill": [
                    Decimal("83.99"),
                    Decimal("83.99"),
                    Decimal("83.99"),
                    Decimal("83.99"),
                    Decimal("83.99"),
                    Decimal("83.99"),
                    Decimal("83.99"),
                    Decimal("83.99"),
                    Decimal("83.99"),
                    Decimal("83.99"),
                    Decimal("83.99"),
                    Decimal("83.99"),
                ],
                "laundry": [
                    Decimal("15.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("10.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("20.00"),
                    Decimal("25.00"),
                    Decimal("60.00"),
                    Decimal("25.00"),
                    Decimal("50.00"),
                ],
                "misc": [
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("542.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("229.00"),
                    Decimal("0.00"),
                ],
                "mortgage": [
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                ],
                "other_insurance": [
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                ],
                "rent": [
                    Decimal("1121.51"),
                    Decimal("1120.61"),
                    Decimal("1121.21"),
                    Decimal("1120.78"),
                    Decimal("1121.70"),
                    Decimal("1114.01"),
                    Decimal("1123.02"),
                    Decimal("1667.05"),
                    Decimal("2252.12"),
                    Decimal("2271.49"),
                    Decimal("2252.00"),
                    Decimal("2248.86"),
                ],
                "renters_insurance": [
                    Decimal("0.00"),
                    Decimal("59.50"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("59.50"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("59.50"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("59.50"),
                    Decimal("0.00"),
                ],
                "student_loans": [
                    Decimal("308.05"),
                    Decimal("308.05"),
                    Decimal("308.05"),
                    Decimal("308.05"),
                    Decimal("308.05"),
                    Decimal("308.05"),
                    Decimal("308.05"),
                    Decimal("300.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                ],
                "taxes": [
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("418.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                ],
                "vision_insurance": [
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                ],
            },
            "wants": {
                "free_spending": [
                    Decimal("807.58"),
                    Decimal("1159.57"),
                    Decimal("655.37"),
                    Decimal("1033.44"),
                    Decimal("1080.12"),
                    Decimal("661.48"),
                    Decimal("832.97"),
                    Decimal("1069.49"),
                    Decimal("1437.87"),
                    Decimal("1623.82"),
                    Decimal("1022.15"),
                    Decimal("864.07"),
                ],
                "misc": [
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                ],
                "subscriptions": [
                    Decimal("174.47"),
                    Decimal("223.47"),
                    Decimal("174.47"),
                    Decimal("238.97"),
                    Decimal("313.16"),
                    Decimal("325.15"),
                    Decimal("325.15"),
                    Decimal("328.15"),
                    Decimal("343.23"),
                    Decimal("341.65"),
                    Decimal("341.65"),
                    Decimal("347.62"),
                ],
                "vacation_spending": [
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("2918.93"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("266.00"),
                    Decimal("0.00"),
                    Decimal("388.55"),
                    Decimal("812.20"),
                    Decimal("0.00"),
                    Decimal("1699.82"),
                ],
            },
            "savings": {
                "crypto": [
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                ],
                "emergency_fund": [
                    Decimal("0.00"),
                    Decimal("435.02"),
                    Decimal("0.00"),
                    Decimal("1636.87"),
                    Decimal("600.00"),
                    Decimal("550.00"),
                    Decimal("500.00"),
                    Decimal("500.00"),
                    Decimal("1400.00"),
                    Decimal("300.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                ],
                "investing": [
                    Decimal("0.00"),
                    Decimal("400.00"),
                    Decimal("0.00"),
                    Decimal("1471.81"),
                    Decimal("500.00"),
                    Decimal("450.00"),
                    Decimal("200.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                ],
                "misc": [
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                ],
                "retirement": [
                    Decimal("600.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                ],
            },
            "income": {
                "earnings": [
                    Decimal("3268.62"),
                    Decimal("6688.96"),
                    Decimal("1466.58"),
                    Decimal("9319.97"),
                    Decimal("4065.55"),
                    Decimal("4093.67"),
                    Decimal("4022.03"),
                    Decimal("4287.17"),
                    Decimal("7852.29"),
                    Decimal("4197.21"),
                    Decimal("4183.77"),
                    Decimal("4180.64"),
                ],
                "tax_returns": [
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("250.00"),
                ],
            },
            "reimbursements": {
                "bills": [
                    Decimal("75.19"),
                    Decimal("112.80"),
                    Decimal("85.39"),
                    Decimal("70.81"),
                    Decimal("75.07"),
                    Decimal("74.62"),
                    Decimal("99.18"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("93.88"),
                    Decimal("51.97"),
                    Decimal("100.67"),
                ],
                "credit_card_rewards": [
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("116.74"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("92.05"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("217.55"),
                    Decimal("0.00"),
                    Decimal("215.10"),
                ],
                "free_spending": [
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("12.00"),
                    Decimal("550.00"),
                    Decimal("235.75"),
                    Decimal("86.00"),
                    Decimal("236.00"),
                    Decimal("100.00"),
                ],
                "rent": [
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("300.00"),
                    Decimal("600.00"),
                    Decimal("645.00"),
                    Decimal("645.00"),
                ],
            },
        },
        "2023": {},
    }

    return expected_data_points_dict


def get_expected_data_points3():
    """Returns the expected data points dictionary pertaining to data from /tests/files/spending3.tsv"""

    expected_data_points_dict = {
        "lifetime": {
            "first_date": ("2021", "March"),
            "needs": {
                "car_insurance": [
                    Decimal("139.00"),
                    Decimal("139.00"),
                    Decimal("139.00"),
                    Decimal("139.00"),
                    Decimal("139.00"),
                    Decimal("143.95"),
                    Decimal("142.80"),
                    Decimal("142.80"),
                    Decimal("142.80"),
                    Decimal("142.80"),
                    Decimal("142.80"),
                    Decimal("143.88"),
                    Decimal("142.80"),
                    Decimal("142.80"),
                    Decimal("142.80"),
                    Decimal("142.80"),
                    Decimal("142.80"),
                    Decimal("146.88"),
                    Decimal("145.60"),
                    Decimal("145.60"),
                    Decimal("145.60"),
                    Decimal("145.60"),
                    Decimal("145.60"),
                    Decimal("146.88"),
                    Decimal("145.60"),
                    Decimal("145.60"),
                ],
                "dental_insurance": [
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                ],
                "electric_bill": [
                    Decimal("98.14"),
                    Decimal("49.60"),
                    Decimal("29.95"),
                    Decimal("51.86"),
                    Decimal("74.42"),
                    Decimal("106.06"),
                    Decimal("83.82"),
                    Decimal("68.52"),
                    Decimal("32.24"),
                    Decimal("63.49"),
                    Decimal("66.39"),
                    Decimal("86.68"),
                    Decimal("86.80"),
                    Decimal("57.64"),
                    Decimal("6.66"),
                    Decimal("65.26"),
                    Decimal("114.37"),
                    Decimal("118.86"),
                    Decimal("110.56"),
                    Decimal("103.78"),
                    Decimal("19.95"),
                    Decimal("117.35"),
                    Decimal("152.69"),
                    Decimal("159.28"),
                    Decimal("207.71"),
                    Decimal("16.35"),
                ],
                "emergencies": [
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("288.61"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("1006.15"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("400.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("208.18"),
                    Decimal("0.00"),
                    Decimal("286.77"),
                ],
                "gasoline": [
                    Decimal("158.70"),
                    Decimal("126.05"),
                    Decimal("247.11"),
                    Decimal("134.75"),
                    Decimal("172.36"),
                    Decimal("301.22"),
                    Decimal("145.18"),
                    Decimal("142.02"),
                    Decimal("140.55"),
                    Decimal("182.21"),
                    Decimal("77.22"),
                    Decimal("203.01"),
                    Decimal("177.51"),
                    Decimal("213.25"),
                    Decimal("227.30"),
                    Decimal("278.63"),
                    Decimal("417.16"),
                    Decimal("196.85"),
                    Decimal("249.06"),
                    Decimal("146.84"),
                    Decimal("240.64"),
                    Decimal("67.84"),
                    Decimal("56.11"),
                    Decimal("244.93"),
                    Decimal("168.53"),
                    Decimal("68.32"),
                ],
                "groceries": [
                    Decimal("316.74"),
                    Decimal("126.91"),
                    Decimal("543.56"),
                    Decimal("377.20"),
                    Decimal("276.06"),
                    Decimal("60.97"),
                    Decimal("191.00"),
                    Decimal("65.98"),
                    Decimal("46.74"),
                    Decimal("199.64"),
                    Decimal("102.35"),
                    Decimal("378.03"),
                    Decimal("127.99"),
                    Decimal("318.11"),
                    Decimal("405.57"),
                    Decimal("576.01"),
                    Decimal("394.67"),
                    Decimal("417.54"),
                    Decimal("414.80"),
                    Decimal("516.67"),
                    Decimal("420.69"),
                    Decimal("578.81"),
                    Decimal("320.00"),
                    Decimal("506.95"),
                    Decimal("319.93"),
                    Decimal("537.51"),
                ],
                "health_insurance": [
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                ],
                "internet_bill": [
                    Decimal("73.99"),
                    Decimal("73.99"),
                    Decimal("73.99"),
                    Decimal("73.99"),
                    Decimal("73.99"),
                    Decimal("83.99"),
                    Decimal("83.99"),
                    Decimal("83.99"),
                    Decimal("83.99"),
                    Decimal("83.99"),
                    Decimal("83.99"),
                    Decimal("83.99"),
                    Decimal("83.99"),
                    Decimal("83.99"),
                    Decimal("83.99"),
                    Decimal("83.99"),
                    Decimal("83.99"),
                    Decimal("83.99"),
                    Decimal("83.99"),
                    Decimal("83.99"),
                    Decimal("83.99"),
                    Decimal("83.99"),
                    Decimal("89.99"),
                    Decimal("67.99"),
                    Decimal("69.99"),
                    Decimal("69.99"),
                ],
                "laundry": [
                    Decimal("10.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("40.00"),
                    Decimal("0.00"),
                    Decimal("10.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("15.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("10.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("20.00"),
                    Decimal("25.00"),
                    Decimal("60.00"),
                    Decimal("25.00"),
                    Decimal("50.00"),
                    Decimal("50.00"),
                    Decimal("60.00"),
                    Decimal("50.00"),
                    Decimal("60.00"),
                ],
                "misc": [
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("30.69"),
                    Decimal("42.99"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("239.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("542.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("229.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                ],
                "mortgage": [
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                ],
                "other_insurance": [
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                ],
                "rent": [
                    Decimal("1033.43"),
                    Decimal("1034.39"),
                    Decimal("1035.39"),
                    Decimal("1035.50"),
                    Decimal("1035.19"),
                    Decimal("1033.92"),
                    Decimal("1101.11"),
                    Decimal("1116.95"),
                    Decimal("1117.60"),
                    Decimal("1119.20"),
                    Decimal("1121.51"),
                    Decimal("1120.61"),
                    Decimal("1121.21"),
                    Decimal("1120.78"),
                    Decimal("1121.70"),
                    Decimal("1114.01"),
                    Decimal("1123.02"),
                    Decimal("1667.05"),
                    Decimal("2252.12"),
                    Decimal("2271.49"),
                    Decimal("2252.00"),
                    Decimal("2248.86"),
                    Decimal("2379.21"),
                    Decimal("2380.08"),
                    Decimal("2384.22"),
                    Decimal("2380.70"),
                ],
                "renters_insurance": [
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("59.50"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("59.50"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("59.50"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("59.50"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("59.50"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("59.50"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("59.50"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("59.50"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                ],
                "student_loans": [
                    Decimal("608.05"),
                    Decimal("368.05"),
                    Decimal("108.05"),
                    Decimal("108.05"),
                    Decimal("368.05"),
                    Decimal("108.05"),
                    Decimal("1655.03"),
                    Decimal("308.05"),
                    Decimal("308.05"),
                    Decimal("308.05"),
                    Decimal("308.05"),
                    Decimal("308.05"),
                    Decimal("308.05"),
                    Decimal("308.05"),
                    Decimal("308.05"),
                    Decimal("308.05"),
                    Decimal("308.05"),
                    Decimal("300.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                ],
                "taxes": [
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("345.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("418.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("450.00"),
                    Decimal("1103.00"),
                ],
                "vision_insurance": [
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                ],
            },
            "wants": {
                "free_spending": [
                    Decimal("1220.00"),
                    Decimal("620.53"),
                    Decimal("1009.09"),
                    Decimal("916.56"),
                    Decimal("868.59"),
                    Decimal("2625.63"),
                    Decimal("1862.81"),
                    Decimal("1539.19"),
                    Decimal("1086.27"),
                    Decimal("1144.55"),
                    Decimal("807.58"),
                    Decimal("1159.57"),
                    Decimal("655.37"),
                    Decimal("1033.44"),
                    Decimal("1080.12"),
                    Decimal("661.48"),
                    Decimal("832.97"),
                    Decimal("1069.49"),
                    Decimal("1437.87"),
                    Decimal("1623.82"),
                    Decimal("1022.15"),
                    Decimal("864.07"),
                    Decimal("1305.19"),
                    Decimal("551.71"),
                    Decimal("1456.69"),
                    Decimal("1072.70"),
                ],
                "misc": [
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                ],
                "subscriptions": [
                    Decimal("194.69"),
                    Decimal("143.97"),
                    Decimal("63.96"),
                    Decimal("143.97"),
                    Decimal("248.98"),
                    Decimal("148.98"),
                    Decimal("49.47"),
                    Decimal("174.47"),
                    Decimal("174.47"),
                    Decimal("174.47"),
                    Decimal("174.47"),
                    Decimal("223.47"),
                    Decimal("174.47"),
                    Decimal("238.97"),
                    Decimal("313.16"),
                    Decimal("325.15"),
                    Decimal("325.15"),
                    Decimal("328.15"),
                    Decimal("343.23"),
                    Decimal("341.65"),
                    Decimal("341.65"),
                    Decimal("347.62"),
                    Decimal("347.62"),
                    Decimal("348.62"),
                    Decimal("348.62"),
                    Decimal("348.62"),
                ],
                "vacation_spending": [
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("395.08"),
                    Decimal("387.01"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("2918.93"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("266.00"),
                    Decimal("0.00"),
                    Decimal("388.55"),
                    Decimal("812.20"),
                    Decimal("0.00"),
                    Decimal("1699.82"),
                    Decimal("0.00"),
                    Decimal("459.49"),
                    Decimal("1046.16"),
                    Decimal("274.00"),
                ],
            },
            "savings": {
                "crypto": [
                    Decimal("180.00"),
                    Decimal("250.00"),
                    Decimal("210.00"),
                    Decimal("247.27"),
                    Decimal("250.00"),
                    Decimal("200.00"),
                    Decimal("200.00"),
                    Decimal("260.00"),
                    Decimal("200.00"),
                    Decimal("250.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                ],
                "emergency_fund": [
                    Decimal("700.00"),
                    Decimal("100.00"),
                    Decimal("400.00"),
                    Decimal("400.00"),
                    Decimal("400.00"),
                    Decimal("400.00"),
                    Decimal("200.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("435.02"),
                    Decimal("0.00"),
                    Decimal("1636.87"),
                    Decimal("600.00"),
                    Decimal("550.00"),
                    Decimal("500.00"),
                    Decimal("500.00"),
                    Decimal("1400.00"),
                    Decimal("300.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                ],
                "investing": [
                    Decimal("200.00"),
                    Decimal("472.00"),
                    Decimal("480.00"),
                    Decimal("500.00"),
                    Decimal("480.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("600.00"),
                    Decimal("400.00"),
                    Decimal("400.00"),
                    Decimal("0.00"),
                    Decimal("400.00"),
                    Decimal("0.00"),
                    Decimal("1471.81"),
                    Decimal("500.00"),
                    Decimal("450.00"),
                    Decimal("200.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("100.00"),
                    Decimal("50.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                ],
                "misc": [
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                ],
                "retirement": [
                    Decimal("800.00"),
                    Decimal("400.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("600.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("700.00"),
                    Decimal("699.62"),
                    Decimal("700.00"),
                    Decimal("700.00"),
                ],
            },
            "income": {
                "earnings": [
                    Decimal("4495.86"),
                    Decimal("5226.63"),
                    Decimal("3940.99"),
                    Decimal("3705.83"),
                    Decimal("3284.40"),
                    Decimal("4601.99"),
                    Decimal("4094.29"),
                    Decimal("4926.58"),
                    Decimal("5403.12"),
                    Decimal("3284.39"),
                    Decimal("3268.62"),
                    Decimal("6688.96"),
                    Decimal("1466.58"),
                    Decimal("9319.97"),
                    Decimal("4065.55"),
                    Decimal("4093.67"),
                    Decimal("4022.03"),
                    Decimal("4287.17"),
                    Decimal("7852.29"),
                    Decimal("4197.21"),
                    Decimal("4183.77"),
                    Decimal("4180.64"),
                    Decimal("4416.51"),
                    Decimal("4621.67"),
                    Decimal("6066.15"),
                    Decimal("4767.83"),
                ],
                "tax_returns": [
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("319.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("250.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("385.00"),
                ],
            },
            "reimbursements": {
                "bills": [
                    Decimal("86.07"),
                    Decimal("61.79"),
                    Decimal("81.72"),
                    Decimal("62.93"),
                    Decimal("74.20"),
                    Decimal("124.78"),
                    Decimal("83.91"),
                    Decimal("76.26"),
                    Decimal("85.37"),
                    Decimal("143.73"),
                    Decimal("75.19"),
                    Decimal("112.80"),
                    Decimal("85.39"),
                    Decimal("70.81"),
                    Decimal("75.07"),
                    Decimal("74.62"),
                    Decimal("99.18"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("93.88"),
                    Decimal("51.97"),
                    Decimal("100.67"),
                    Decimal("118.34"),
                    Decimal("114.63"),
                    Decimal("0.00"),
                    Decimal("40.17"),
                ],
                "credit_card_rewards": [
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("71.33"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("425.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("116.74"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("92.05"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("217.55"),
                    Decimal("0.00"),
                    Decimal("215.10"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("133.41"),
                    Decimal("0.00"),
                ],
                "free_spending": [
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("106.00"),
                    Decimal("68.27"),
                    Decimal("0.00"),
                    Decimal("64.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("12.00"),
                    Decimal("550.00"),
                    Decimal("235.75"),
                    Decimal("86.00"),
                    Decimal("236.00"),
                    Decimal("100.00"),
                    Decimal("20.00"),
                    Decimal("180.65"),
                    Decimal("42.00"),
                    Decimal("0.00"),
                ],
                "rent": [
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("300.00"),
                    Decimal("600.00"),
                    Decimal("645.00"),
                    Decimal("645.00"),
                    Decimal("645.00"),
                    Decimal("645.00"),
                    Decimal("645.00"),
                    Decimal("645.00"),
                ],
            },
        },
        "2021": {
            "first_date": ("2021", "March"),
            "needs": {
                "car_insurance": [
                    Decimal("139.00"),
                    Decimal("139.00"),
                    Decimal("139.00"),
                    Decimal("139.00"),
                    Decimal("139.00"),
                    Decimal("143.95"),
                    Decimal("142.80"),
                    Decimal("142.80"),
                    Decimal("142.80"),
                    Decimal("142.80"),
                ],
                "dental_insurance": [
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                ],
                "electric_bill": [
                    Decimal("98.14"),
                    Decimal("49.60"),
                    Decimal("29.95"),
                    Decimal("51.86"),
                    Decimal("74.42"),
                    Decimal("106.06"),
                    Decimal("83.82"),
                    Decimal("68.52"),
                    Decimal("32.24"),
                    Decimal("63.49"),
                ],
                "emergencies": [
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("288.61"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                ],
                "gasoline": [
                    Decimal("158.70"),
                    Decimal("126.05"),
                    Decimal("247.11"),
                    Decimal("134.75"),
                    Decimal("172.36"),
                    Decimal("301.22"),
                    Decimal("145.18"),
                    Decimal("142.02"),
                    Decimal("140.55"),
                    Decimal("182.21"),
                ],
                "groceries": [
                    Decimal("316.74"),
                    Decimal("126.91"),
                    Decimal("543.56"),
                    Decimal("377.20"),
                    Decimal("276.06"),
                    Decimal("60.97"),
                    Decimal("191.00"),
                    Decimal("65.98"),
                    Decimal("46.74"),
                    Decimal("199.64"),
                ],
                "health_insurance": [
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                ],
                "internet_bill": [
                    Decimal("73.99"),
                    Decimal("73.99"),
                    Decimal("73.99"),
                    Decimal("73.99"),
                    Decimal("73.99"),
                    Decimal("83.99"),
                    Decimal("83.99"),
                    Decimal("83.99"),
                    Decimal("83.99"),
                    Decimal("83.99"),
                ],
                "laundry": [
                    Decimal("10.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("40.00"),
                    Decimal("0.00"),
                    Decimal("10.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                ],
                "misc": [
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("30.69"),
                    Decimal("42.99"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("239.00"),
                    Decimal("0.00"),
                ],
                "mortgage": [
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                ],
                "other_insurance": [
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                ],
                "rent": [
                    Decimal("1033.43"),
                    Decimal("1034.39"),
                    Decimal("1035.39"),
                    Decimal("1035.50"),
                    Decimal("1035.19"),
                    Decimal("1033.92"),
                    Decimal("1101.11"),
                    Decimal("1116.95"),
                    Decimal("1117.60"),
                    Decimal("1119.20"),
                ],
                "renters_insurance": [
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("59.50"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("59.50"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("59.50"),
                    Decimal("0.00"),
                ],
                "student_loans": [
                    Decimal("608.05"),
                    Decimal("368.05"),
                    Decimal("108.05"),
                    Decimal("108.05"),
                    Decimal("368.05"),
                    Decimal("108.05"),
                    Decimal("1655.03"),
                    Decimal("308.05"),
                    Decimal("308.05"),
                    Decimal("308.05"),
                ],
                "taxes": [
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("345.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                ],
                "vision_insurance": [
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                ],
            },
            "wants": {
                "free_spending": [
                    Decimal("1220.00"),
                    Decimal("620.53"),
                    Decimal("1009.09"),
                    Decimal("916.56"),
                    Decimal("868.59"),
                    Decimal("2625.63"),
                    Decimal("1862.81"),
                    Decimal("1539.19"),
                    Decimal("1086.27"),
                    Decimal("1144.55"),
                ],
                "misc": [
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                ],
                "subscriptions": [
                    Decimal("194.69"),
                    Decimal("143.97"),
                    Decimal("63.96"),
                    Decimal("143.97"),
                    Decimal("248.98"),
                    Decimal("148.98"),
                    Decimal("49.47"),
                    Decimal("174.47"),
                    Decimal("174.47"),
                    Decimal("174.47"),
                ],
                "vacation_spending": [
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("395.08"),
                    Decimal("387.01"),
                ],
            },
            "savings": {
                "crypto": [
                    Decimal("180.00"),
                    Decimal("250.00"),
                    Decimal("210.00"),
                    Decimal("247.27"),
                    Decimal("250.00"),
                    Decimal("200.00"),
                    Decimal("200.00"),
                    Decimal("260.00"),
                    Decimal("200.00"),
                    Decimal("250.00"),
                ],
                "emergency_fund": [
                    Decimal("700.00"),
                    Decimal("100.00"),
                    Decimal("400.00"),
                    Decimal("400.00"),
                    Decimal("400.00"),
                    Decimal("400.00"),
                    Decimal("200.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                ],
                "investing": [
                    Decimal("200.00"),
                    Decimal("472.00"),
                    Decimal("480.00"),
                    Decimal("500.00"),
                    Decimal("480.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("600.00"),
                    Decimal("400.00"),
                    Decimal("400.00"),
                ],
                "misc": [
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                ],
                "retirement": [
                    Decimal("800.00"),
                    Decimal("400.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                ],
            },
            "income": {
                "earnings": [
                    Decimal("4495.86"),
                    Decimal("5226.63"),
                    Decimal("3940.99"),
                    Decimal("3705.83"),
                    Decimal("3284.40"),
                    Decimal("4601.99"),
                    Decimal("4094.29"),
                    Decimal("4926.58"),
                    Decimal("5403.12"),
                    Decimal("3284.39"),
                ],
                "tax_returns": [
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("319.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                ],
            },
            "reimbursements": {
                "bills": [
                    Decimal("86.07"),
                    Decimal("61.79"),
                    Decimal("81.72"),
                    Decimal("62.93"),
                    Decimal("74.20"),
                    Decimal("124.78"),
                    Decimal("83.91"),
                    Decimal("76.26"),
                    Decimal("85.37"),
                    Decimal("143.73"),
                ],
                "credit_card_rewards": [
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("71.33"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("425.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                ],
                "free_spending": [
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("106.00"),
                    Decimal("68.27"),
                    Decimal("0.00"),
                    Decimal("64.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                ],
                "rent": [
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                ],
            },
        },
        "2022": {
            "first_date": ("2022", "January"),
            "needs": {
                "car_insurance": [
                    Decimal("142.80"),
                    Decimal("143.88"),
                    Decimal("142.80"),
                    Decimal("142.80"),
                    Decimal("142.80"),
                    Decimal("142.80"),
                    Decimal("142.80"),
                    Decimal("146.88"),
                    Decimal("145.60"),
                    Decimal("145.60"),
                    Decimal("145.60"),
                    Decimal("145.60"),
                ],
                "dental_insurance": [
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                ],
                "electric_bill": [
                    Decimal("66.39"),
                    Decimal("86.68"),
                    Decimal("86.80"),
                    Decimal("57.64"),
                    Decimal("6.66"),
                    Decimal("65.26"),
                    Decimal("114.37"),
                    Decimal("118.86"),
                    Decimal("110.56"),
                    Decimal("103.78"),
                    Decimal("19.95"),
                    Decimal("117.35"),
                ],
                "emergencies": [
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("1006.15"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("400.00"),
                    Decimal("0.00"),
                ],
                "gasoline": [
                    Decimal("77.22"),
                    Decimal("203.01"),
                    Decimal("177.51"),
                    Decimal("213.25"),
                    Decimal("227.30"),
                    Decimal("278.63"),
                    Decimal("417.16"),
                    Decimal("196.85"),
                    Decimal("249.06"),
                    Decimal("146.84"),
                    Decimal("240.64"),
                    Decimal("67.84"),
                ],
                "groceries": [
                    Decimal("102.35"),
                    Decimal("378.03"),
                    Decimal("127.99"),
                    Decimal("318.11"),
                    Decimal("405.57"),
                    Decimal("576.01"),
                    Decimal("394.67"),
                    Decimal("417.54"),
                    Decimal("414.80"),
                    Decimal("516.67"),
                    Decimal("420.69"),
                    Decimal("578.81"),
                ],
                "health_insurance": [
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                ],
                "internet_bill": [
                    Decimal("83.99"),
                    Decimal("83.99"),
                    Decimal("83.99"),
                    Decimal("83.99"),
                    Decimal("83.99"),
                    Decimal("83.99"),
                    Decimal("83.99"),
                    Decimal("83.99"),
                    Decimal("83.99"),
                    Decimal("83.99"),
                    Decimal("83.99"),
                    Decimal("83.99"),
                ],
                "laundry": [
                    Decimal("15.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("10.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("20.00"),
                    Decimal("25.00"),
                    Decimal("60.00"),
                    Decimal("25.00"),
                    Decimal("50.00"),
                ],
                "misc": [
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("542.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("229.00"),
                    Decimal("0.00"),
                ],
                "mortgage": [
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                ],
                "other_insurance": [
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                ],
                "rent": [
                    Decimal("1121.51"),
                    Decimal("1120.61"),
                    Decimal("1121.21"),
                    Decimal("1120.78"),
                    Decimal("1121.70"),
                    Decimal("1114.01"),
                    Decimal("1123.02"),
                    Decimal("1667.05"),
                    Decimal("2252.12"),
                    Decimal("2271.49"),
                    Decimal("2252.00"),
                    Decimal("2248.86"),
                ],
                "renters_insurance": [
                    Decimal("0.00"),
                    Decimal("59.50"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("59.50"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("59.50"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("59.50"),
                    Decimal("0.00"),
                ],
                "student_loans": [
                    Decimal("308.05"),
                    Decimal("308.05"),
                    Decimal("308.05"),
                    Decimal("308.05"),
                    Decimal("308.05"),
                    Decimal("308.05"),
                    Decimal("308.05"),
                    Decimal("300.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                ],
                "taxes": [
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("418.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                ],
                "vision_insurance": [
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                ],
            },
            "wants": {
                "free_spending": [
                    Decimal("807.58"),
                    Decimal("1159.57"),
                    Decimal("655.37"),
                    Decimal("1033.44"),
                    Decimal("1080.12"),
                    Decimal("661.48"),
                    Decimal("832.97"),
                    Decimal("1069.49"),
                    Decimal("1437.87"),
                    Decimal("1623.82"),
                    Decimal("1022.15"),
                    Decimal("864.07"),
                ],
                "misc": [
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                ],
                "subscriptions": [
                    Decimal("174.47"),
                    Decimal("223.47"),
                    Decimal("174.47"),
                    Decimal("238.97"),
                    Decimal("313.16"),
                    Decimal("325.15"),
                    Decimal("325.15"),
                    Decimal("328.15"),
                    Decimal("343.23"),
                    Decimal("341.65"),
                    Decimal("341.65"),
                    Decimal("347.62"),
                ],
                "vacation_spending": [
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("2918.93"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("266.00"),
                    Decimal("0.00"),
                    Decimal("388.55"),
                    Decimal("812.20"),
                    Decimal("0.00"),
                    Decimal("1699.82"),
                ],
            },
            "savings": {
                "crypto": [
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                ],
                "emergency_fund": [
                    Decimal("0.00"),
                    Decimal("435.02"),
                    Decimal("0.00"),
                    Decimal("1636.87"),
                    Decimal("600.00"),
                    Decimal("550.00"),
                    Decimal("500.00"),
                    Decimal("500.00"),
                    Decimal("1400.00"),
                    Decimal("300.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                ],
                "investing": [
                    Decimal("0.00"),
                    Decimal("400.00"),
                    Decimal("0.00"),
                    Decimal("1471.81"),
                    Decimal("500.00"),
                    Decimal("450.00"),
                    Decimal("200.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                ],
                "misc": [
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                ],
                "retirement": [
                    Decimal("600.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                ],
            },
            "income": {
                "earnings": [
                    Decimal("3268.62"),
                    Decimal("6688.96"),
                    Decimal("1466.58"),
                    Decimal("9319.97"),
                    Decimal("4065.55"),
                    Decimal("4093.67"),
                    Decimal("4022.03"),
                    Decimal("4287.17"),
                    Decimal("7852.29"),
                    Decimal("4197.21"),
                    Decimal("4183.77"),
                    Decimal("4180.64"),
                ],
                "tax_returns": [
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("250.00"),
                ],
            },
            "reimbursements": {
                "bills": [
                    Decimal("75.19"),
                    Decimal("112.80"),
                    Decimal("85.39"),
                    Decimal("70.81"),
                    Decimal("75.07"),
                    Decimal("74.62"),
                    Decimal("99.18"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("93.88"),
                    Decimal("51.97"),
                    Decimal("100.67"),
                ],
                "credit_card_rewards": [
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("116.74"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("92.05"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("217.55"),
                    Decimal("0.00"),
                    Decimal("215.10"),
                ],
                "free_spending": [
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("12.00"),
                    Decimal("550.00"),
                    Decimal("235.75"),
                    Decimal("86.00"),
                    Decimal("236.00"),
                    Decimal("100.00"),
                ],
                "rent": [
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("0.00"),
                    Decimal("300.00"),
                    Decimal("600.00"),
                    Decimal("645.00"),
                    Decimal("645.00"),
                ],
            },
        },
        "2023": {
            "first_date": ("2023", "January"),
            "needs": {
                "car_insurance": [Decimal("145.60"), Decimal("146.88"), Decimal("145.60"), Decimal("145.60")],
                "dental_insurance": [Decimal("0.00"), Decimal("0.00"), Decimal("0.00"), Decimal("0.00")],
                "electric_bill": [Decimal("152.69"), Decimal("159.28"), Decimal("207.71"), Decimal("16.35")],
                "emergencies": [Decimal("0.00"), Decimal("208.18"), Decimal("0.00"), Decimal("286.77")],
                "gasoline": [Decimal("56.11"), Decimal("244.93"), Decimal("168.53"), Decimal("68.32")],
                "groceries": [Decimal("320.00"), Decimal("506.95"), Decimal("319.93"), Decimal("537.51")],
                "health_insurance": [Decimal("0.00"), Decimal("0.00"), Decimal("0.00"), Decimal("0.00")],
                "internet_bill": [Decimal("89.99"), Decimal("67.99"), Decimal("69.99"), Decimal("69.99")],
                "laundry": [Decimal("50.00"), Decimal("60.00"), Decimal("50.00"), Decimal("60.00")],
                "misc": [Decimal("0.00"), Decimal("0.00"), Decimal("0.00"), Decimal("0.00")],
                "mortgage": [Decimal("0.00"), Decimal("0.00"), Decimal("0.00"), Decimal("0.00")],
                "other_insurance": [Decimal("0.00"), Decimal("0.00"), Decimal("0.00"), Decimal("0.00")],
                "rent": [Decimal("2379.21"), Decimal("2380.08"), Decimal("2384.22"), Decimal("2380.70")],
                "renters_insurance": [Decimal("0.00"), Decimal("59.50"), Decimal("0.00"), Decimal("0.00")],
                "student_loans": [Decimal("0.00"), Decimal("0.00"), Decimal("0.00"), Decimal("0.00")],
                "taxes": [Decimal("0.00"), Decimal("0.00"), Decimal("450.00"), Decimal("1103.00")],
                "vision_insurance": [Decimal("0.00"), Decimal("0.00"), Decimal("0.00"), Decimal("0.00")],
            },
            "wants": {
                "free_spending": [Decimal("1305.19"), Decimal("551.71"), Decimal("1456.69"), Decimal("1072.70")],
                "misc": [Decimal("0.00"), Decimal("0.00"), Decimal("0.00"), Decimal("0.00")],
                "subscriptions": [Decimal("347.62"), Decimal("348.62"), Decimal("348.62"), Decimal("348.62")],
                "vacation_spending": [Decimal("0.00"), Decimal("459.49"), Decimal("1046.16"), Decimal("274.00")],
            },
            "savings": {
                "crypto": [Decimal("0.00"), Decimal("0.00"), Decimal("0.00"), Decimal("0.00")],
                "emergency_fund": [Decimal("0.00"), Decimal("0.00"), Decimal("0.00"), Decimal("0.00")],
                "investing": [Decimal("100.00"), Decimal("50.00"), Decimal("0.00"), Decimal("0.00")],
                "misc": [Decimal("0.00"), Decimal("0.00"), Decimal("0.00"), Decimal("0.00")],
                "retirement": [Decimal("700.00"), Decimal("699.62"), Decimal("700.00"), Decimal("700.00")],
            },
            "income": {
                "earnings": [Decimal("4416.51"), Decimal("4621.67"), Decimal("6066.15"), Decimal("4767.83")],
                "tax_returns": [Decimal("0.00"), Decimal("0.00"), Decimal("0.00"), Decimal("385.00")],
            },
            "reimbursements": {
                "bills": [Decimal("118.34"), Decimal("114.63"), Decimal("0.00"), Decimal("40.17")],
                "credit_card_rewards": [Decimal("0.00"), Decimal("0.00"), Decimal("133.41"), Decimal("0.00")],
                "free_spending": [Decimal("20.00"), Decimal("180.65"), Decimal("42.00"), Decimal("0.00")],
                "rent": [Decimal("645.00"), Decimal("645.00"), Decimal("645.00"), Decimal("645.00")],
            },
        },
    }

    return expected_data_points_dict


def get_expected_analysis_dict1():
    """Returns the expected analysis dictionary pertaining to data from /tests/files/spending1.tsv"""

    expected_analysis_dict = {
        "lifetime": {
            "needs": {
                "car_insurance": {
                    "average": Decimal("145.60"),
                    "median": Decimal("145.60"),
                    "variance": Decimal("0.00"),
                    "standard_deviation": Decimal("0.00"),
                    "linear_regression_coefficients": (0, 0),
                },
                "dental_insurance": {
                    "average": Decimal("0.00"),
                    "median": Decimal("0.00"),
                    "variance": Decimal("0.00"),
                    "standard_deviation": Decimal("0.00"),
                    "linear_regression_coefficients": (0, 0),
                },
                "electric_bill": {
                    "average": Decimal("16.35"),
                    "median": Decimal("16.35"),
                    "variance": Decimal("0.00"),
                    "standard_deviation": Decimal("0.00"),
                    "linear_regression_coefficients": (0, 0),
                },
                "emergencies": {
                    "average": Decimal("125.99"),
                    "median": Decimal("125.99"),
                    "variance": Decimal("0.00"),
                    "standard_deviation": Decimal("0.00"),
                    "linear_regression_coefficients": (0, 0),
                },
                "gasoline": {
                    "average": Decimal("68.32"),
                    "median": Decimal("68.32"),
                    "variance": Decimal("0.00"),
                    "standard_deviation": Decimal("0.00"),
                    "linear_regression_coefficients": (0, 0),
                },
                "groceries": {
                    "average": Decimal("389.44"),
                    "median": Decimal("389.44"),
                    "variance": Decimal("0.00"),
                    "standard_deviation": Decimal("0.00"),
                    "linear_regression_coefficients": (0, 0),
                },
                "health_insurance": {
                    "average": Decimal("0.00"),
                    "median": Decimal("0.00"),
                    "variance": Decimal("0.00"),
                    "standard_deviation": Decimal("0.00"),
                    "linear_regression_coefficients": (0, 0),
                },
                "internet_bill": {
                    "average": Decimal("69.99"),
                    "median": Decimal("69.99"),
                    "variance": Decimal("0.00"),
                    "standard_deviation": Decimal("0.00"),
                    "linear_regression_coefficients": (0, 0),
                },
                "laundry": {
                    "average": Decimal("0.00"),
                    "median": Decimal("0.00"),
                    "variance": Decimal("0.00"),
                    "standard_deviation": Decimal("0.00"),
                    "linear_regression_coefficients": (0, 0),
                },
                "misc": {
                    "average": Decimal("251.98"),
                    "median": Decimal("251.98"),
                    "variance": Decimal("0.00"),
                    "standard_deviation": Decimal("0.00"),
                    "linear_regression_coefficients": (0, 0),
                },
                "mortgage": {
                    "average": Decimal("0.00"),
                    "median": Decimal("0.00"),
                    "variance": Decimal("0.00"),
                    "standard_deviation": Decimal("0.00"),
                    "linear_regression_coefficients": (0, 0),
                },
                "other_insurance": {
                    "average": Decimal("0.00"),
                    "median": Decimal("0.00"),
                    "variance": Decimal("0.00"),
                    "standard_deviation": Decimal("0.00"),
                    "linear_regression_coefficients": (0, 0),
                },
                "rent": {
                    "average": Decimal("2000.00"),
                    "median": Decimal("2000.00"),
                    "variance": Decimal("0.00"),
                    "standard_deviation": Decimal("0.00"),
                    "linear_regression_coefficients": (0, 0),
                },
                "renters_insurance": {
                    "average": Decimal("68.32"),
                    "median": Decimal("68.32"),
                    "variance": Decimal("0.00"),
                    "standard_deviation": Decimal("0.00"),
                    "linear_regression_coefficients": (0, 0),
                },
                "student_loans": {
                    "average": Decimal("145.60"),
                    "median": Decimal("145.60"),
                    "variance": Decimal("0.00"),
                    "standard_deviation": Decimal("0.00"),
                    "linear_regression_coefficients": (0, 0),
                },
                "taxes": {
                    "average": Decimal("400.00"),
                    "median": Decimal("400.00"),
                    "variance": Decimal("0.00"),
                    "standard_deviation": Decimal("0.00"),
                    "linear_regression_coefficients": (0, 0),
                },
                "vision_insurance": {
                    "average": Decimal("0.00"),
                    "median": Decimal("0.00"),
                    "variance": Decimal("0.00"),
                    "standard_deviation": Decimal("0.00"),
                    "linear_regression_coefficients": (0, 0),
                },
            },
            "wants": {
                "free_spending": {
                    "average": Decimal("235.93"),
                    "median": Decimal("235.93"),
                    "variance": Decimal("0.00"),
                    "standard_deviation": Decimal("0.00"),
                    "linear_regression_coefficients": (0, 0),
                },
                "misc": {
                    "average": Decimal("44.44"),
                    "median": Decimal("44.44"),
                    "variance": Decimal("0.00"),
                    "standard_deviation": Decimal("0.00"),
                    "linear_regression_coefficients": (0, 0),
                },
                "subscriptions": {
                    "average": Decimal("28.98"),
                    "median": Decimal("28.98"),
                    "variance": Decimal("0.00"),
                    "standard_deviation": Decimal("0.00"),
                    "linear_regression_coefficients": (0, 0),
                },
                "vacation_spending": {
                    "average": Decimal("444.44"),
                    "median": Decimal("444.44"),
                    "variance": Decimal("0.00"),
                    "standard_deviation": Decimal("0.00"),
                    "linear_regression_coefficients": (0, 0),
                },
            },
            "savings": {
                "crypto": {
                    "average": Decimal("110.00"),
                    "median": Decimal("110.00"),
                    "variance": Decimal("0.00"),
                    "standard_deviation": Decimal("0.00"),
                    "linear_regression_coefficients": (0, 0),
                },
                "emergency_fund": {
                    "average": Decimal("200.00"),
                    "median": Decimal("200.00"),
                    "variance": Decimal("0.00"),
                    "standard_deviation": Decimal("0.00"),
                    "linear_regression_coefficients": (0, 0),
                },
                "investing": {
                    "average": Decimal("100.00"),
                    "median": Decimal("100.00"),
                    "variance": Decimal("0.00"),
                    "standard_deviation": Decimal("0.00"),
                    "linear_regression_coefficients": (0, 0),
                },
                "misc": {
                    "average": Decimal("55.55"),
                    "median": Decimal("55.55"),
                    "variance": Decimal("0.00"),
                    "standard_deviation": Decimal("0.00"),
                    "linear_regression_coefficients": (0, 0),
                },
                "retirement": {
                    "average": Decimal("700.00"),
                    "median": Decimal("700.00"),
                    "variance": Decimal("0.00"),
                    "standard_deviation": Decimal("0.00"),
                    "linear_regression_coefficients": (0, 0),
                },
            },
            "income": {
                "earnings": {
                    "average": Decimal("6000.00"),
                    "median": Decimal("6000.00"),
                    "variance": Decimal("0.00"),
                    "standard_deviation": Decimal("0.00"),
                    "linear_regression_coefficients": (0, 0),
                },
                "tax_returns": {
                    "average": Decimal("500.00"),
                    "median": Decimal("500.00"),
                    "variance": Decimal("0.00"),
                    "standard_deviation": Decimal("0.00"),
                    "linear_regression_coefficients": (0, 0),
                },
            },
            "reimbursements": {
                "bills": {
                    "average": Decimal("40.00"),
                    "median": Decimal("40.00"),
                    "variance": Decimal("0.00"),
                    "standard_deviation": Decimal("0.00"),
                    "linear_regression_coefficients": (0, 0),
                },
                "credit_card_rewards": {
                    "average": Decimal("13.99"),
                    "median": Decimal("13.99"),
                    "variance": Decimal("0.00"),
                    "standard_deviation": Decimal("0.00"),
                    "linear_regression_coefficients": (0, 0),
                },
                "free_spending": {
                    "average": Decimal("45.60"),
                    "median": Decimal("45.60"),
                    "variance": Decimal("0.00"),
                    "standard_deviation": Decimal("0.00"),
                    "linear_regression_coefficients": (0, 0),
                },
                "rent": {
                    "average": Decimal("1000.00"),
                    "median": Decimal("1000.00"),
                    "variance": Decimal("0.00"),
                    "standard_deviation": Decimal("0.00"),
                    "linear_regression_coefficients": (0, 0),
                },
            },
        },
        "2021": {},
        "2022": {},
        "2023": {
            "needs": {
                "car_insurance": {
                    "average": Decimal("145.60"),
                    "median": Decimal("145.60"),
                    "variance": Decimal("0.00"),
                    "standard_deviation": Decimal("0.00"),
                    "linear_regression_coefficients": (0, 0),
                },
                "dental_insurance": {
                    "average": Decimal("0.00"),
                    "median": Decimal("0.00"),
                    "variance": Decimal("0.00"),
                    "standard_deviation": Decimal("0.00"),
                    "linear_regression_coefficients": (0, 0),
                },
                "electric_bill": {
                    "average": Decimal("16.35"),
                    "median": Decimal("16.35"),
                    "variance": Decimal("0.00"),
                    "standard_deviation": Decimal("0.00"),
                    "linear_regression_coefficients": (0, 0),
                },
                "emergencies": {
                    "average": Decimal("125.99"),
                    "median": Decimal("125.99"),
                    "variance": Decimal("0.00"),
                    "standard_deviation": Decimal("0.00"),
                    "linear_regression_coefficients": (0, 0),
                },
                "gasoline": {
                    "average": Decimal("68.32"),
                    "median": Decimal("68.32"),
                    "variance": Decimal("0.00"),
                    "standard_deviation": Decimal("0.00"),
                    "linear_regression_coefficients": (0, 0),
                },
                "groceries": {
                    "average": Decimal("389.44"),
                    "median": Decimal("389.44"),
                    "variance": Decimal("0.00"),
                    "standard_deviation": Decimal("0.00"),
                    "linear_regression_coefficients": (0, 0),
                },
                "health_insurance": {
                    "average": Decimal("0.00"),
                    "median": Decimal("0.00"),
                    "variance": Decimal("0.00"),
                    "standard_deviation": Decimal("0.00"),
                    "linear_regression_coefficients": (0, 0),
                },
                "internet_bill": {
                    "average": Decimal("69.99"),
                    "median": Decimal("69.99"),
                    "variance": Decimal("0.00"),
                    "standard_deviation": Decimal("0.00"),
                    "linear_regression_coefficients": (0, 0),
                },
                "laundry": {
                    "average": Decimal("0.00"),
                    "median": Decimal("0.00"),
                    "variance": Decimal("0.00"),
                    "standard_deviation": Decimal("0.00"),
                    "linear_regression_coefficients": (0, 0),
                },
                "misc": {
                    "average": Decimal("251.98"),
                    "median": Decimal("251.98"),
                    "variance": Decimal("0.00"),
                    "standard_deviation": Decimal("0.00"),
                    "linear_regression_coefficients": (0, 0),
                },
                "mortgage": {
                    "average": Decimal("0.00"),
                    "median": Decimal("0.00"),
                    "variance": Decimal("0.00"),
                    "standard_deviation": Decimal("0.00"),
                    "linear_regression_coefficients": (0, 0),
                },
                "other_insurance": {
                    "average": Decimal("0.00"),
                    "median": Decimal("0.00"),
                    "variance": Decimal("0.00"),
                    "standard_deviation": Decimal("0.00"),
                    "linear_regression_coefficients": (0, 0),
                },
                "rent": {
                    "average": Decimal("2000.00"),
                    "median": Decimal("2000.00"),
                    "variance": Decimal("0.00"),
                    "standard_deviation": Decimal("0.00"),
                    "linear_regression_coefficients": (0, 0),
                },
                "renters_insurance": {
                    "average": Decimal("68.32"),
                    "median": Decimal("68.32"),
                    "variance": Decimal("0.00"),
                    "standard_deviation": Decimal("0.00"),
                    "linear_regression_coefficients": (0, 0),
                },
                "student_loans": {
                    "average": Decimal("145.60"),
                    "median": Decimal("145.60"),
                    "variance": Decimal("0.00"),
                    "standard_deviation": Decimal("0.00"),
                    "linear_regression_coefficients": (0, 0),
                },
                "taxes": {
                    "average": Decimal("400.00"),
                    "median": Decimal("400.00"),
                    "variance": Decimal("0.00"),
                    "standard_deviation": Decimal("0.00"),
                    "linear_regression_coefficients": (0, 0),
                },
                "vision_insurance": {
                    "average": Decimal("0.00"),
                    "median": Decimal("0.00"),
                    "variance": Decimal("0.00"),
                    "standard_deviation": Decimal("0.00"),
                    "linear_regression_coefficients": (0, 0),
                },
            },
            "wants": {
                "free_spending": {
                    "average": Decimal("235.93"),
                    "median": Decimal("235.93"),
                    "variance": Decimal("0.00"),
                    "standard_deviation": Decimal("0.00"),
                    "linear_regression_coefficients": (0, 0),
                },
                "misc": {
                    "average": Decimal("44.44"),
                    "median": Decimal("44.44"),
                    "variance": Decimal("0.00"),
                    "standard_deviation": Decimal("0.00"),
                    "linear_regression_coefficients": (0, 0),
                },
                "subscriptions": {
                    "average": Decimal("28.98"),
                    "median": Decimal("28.98"),
                    "variance": Decimal("0.00"),
                    "standard_deviation": Decimal("0.00"),
                    "linear_regression_coefficients": (0, 0),
                },
                "vacation_spending": {
                    "average": Decimal("444.44"),
                    "median": Decimal("444.44"),
                    "variance": Decimal("0.00"),
                    "standard_deviation": Decimal("0.00"),
                    "linear_regression_coefficients": (0, 0),
                },
            },
            "savings": {
                "crypto": {
                    "average": Decimal("110.00"),
                    "median": Decimal("110.00"),
                    "variance": Decimal("0.00"),
                    "standard_deviation": Decimal("0.00"),
                    "linear_regression_coefficients": (0, 0),
                },
                "emergency_fund": {
                    "average": Decimal("200.00"),
                    "median": Decimal("200.00"),
                    "variance": Decimal("0.00"),
                    "standard_deviation": Decimal("0.00"),
                    "linear_regression_coefficients": (0, 0),
                },
                "investing": {
                    "average": Decimal("100.00"),
                    "median": Decimal("100.00"),
                    "variance": Decimal("0.00"),
                    "standard_deviation": Decimal("0.00"),
                    "linear_regression_coefficients": (0, 0),
                },
                "misc": {
                    "average": Decimal("55.55"),
                    "median": Decimal("55.55"),
                    "variance": Decimal("0.00"),
                    "standard_deviation": Decimal("0.00"),
                    "linear_regression_coefficients": (0, 0),
                },
                "retirement": {
                    "average": Decimal("700.00"),
                    "median": Decimal("700.00"),
                    "variance": Decimal("0.00"),
                    "standard_deviation": Decimal("0.00"),
                    "linear_regression_coefficients": (0, 0),
                },
            },
            "income": {
                "earnings": {
                    "average": Decimal("6000.00"),
                    "median": Decimal("6000.00"),
                    "variance": Decimal("0.00"),
                    "standard_deviation": Decimal("0.00"),
                    "linear_regression_coefficients": (0, 0),
                },
                "tax_returns": {
                    "average": Decimal("500.00"),
                    "median": Decimal("500.00"),
                    "variance": Decimal("0.00"),
                    "standard_deviation": Decimal("0.00"),
                    "linear_regression_coefficients": (0, 0),
                },
            },
            "reimbursements": {
                "bills": {
                    "average": Decimal("40.00"),
                    "median": Decimal("40.00"),
                    "variance": Decimal("0.00"),
                    "standard_deviation": Decimal("0.00"),
                    "linear_regression_coefficients": (0, 0),
                },
                "credit_card_rewards": {
                    "average": Decimal("13.99"),
                    "median": Decimal("13.99"),
                    "variance": Decimal("0.00"),
                    "standard_deviation": Decimal("0.00"),
                    "linear_regression_coefficients": (0, 0),
                },
                "free_spending": {
                    "average": Decimal("45.60"),
                    "median": Decimal("45.60"),
                    "variance": Decimal("0.00"),
                    "standard_deviation": Decimal("0.00"),
                    "linear_regression_coefficients": (0, 0),
                },
                "rent": {
                    "average": Decimal("1000.00"),
                    "median": Decimal("1000.00"),
                    "variance": Decimal("0.00"),
                    "standard_deviation": Decimal("0.00"),
                    "linear_regression_coefficients": (0, 0),
                },
            },
        },
    }

    return expected_analysis_dict


def get_expected_analysis_dict2():
    """Returns the expected analysis dictionary dictionary pertaining to data from /tests/files/spending2.tsv"""

    expected_analysis_dict = {
        "lifetime": {
            "needs": {
                "car_insurance": {
                    "average": Decimal("144.16"),
                    "median": Decimal("143.34"),
                    "variance": Decimal("2.24"),
                    "standard_deviation": Decimal("1.50"),
                    "linear_regression_coefficients": (Decimal("0.32"), Decimal("142.40")),
                },
                "dental_insurance": {
                    "average": Decimal("0.00"),
                    "median": Decimal("0.00"),
                    "variance": Decimal("0.00"),
                    "standard_deviation": Decimal("0.00"),
                    "linear_regression_coefficients": (Decimal("0.00"), Decimal("0.00")),
                },
                "electric_bill": {
                    "average": Decimal("79.52"),
                    "median": Decimal("86.74"),
                    "variance": Decimal("1296.77"),
                    "standard_deviation": Decimal("36.01"),
                    "linear_regression_coefficients": (Decimal("2.55"), Decimal("65.50")),
                },
                "emergencies": {
                    "average": Decimal("117.18"),
                    "median": Decimal("0.00"),
                    "variance": Decimal("83963.86"),
                    "standard_deviation": Decimal("289.77"),
                    "linear_regression_coefficients": (Decimal("9.07"), Decimal("67.29")),
                },
                "gasoline": {
                    "average": Decimal("207.94"),
                    "median": Decimal("208.13"),
                    "variance": Decimal("7787.95"),
                    "standard_deviation": Decimal("88.25"),
                    "linear_regression_coefficients": (Decimal("0.86"), Decimal("203.21")),
                },
                "groceries": {
                    "average": Decimal("387.60"),
                    "median": Decimal("410.18"),
                    "variance": Decimal("20459.01"),
                    "standard_deviation": Decimal("143.03"),
                    "linear_regression_coefficients": (Decimal("30.36"), Decimal("220.62")),
                },
                "health_insurance": {
                    "average": Decimal("0.00"),
                    "median": Decimal("0.00"),
                    "variance": Decimal("0.00"),
                    "standard_deviation": Decimal("0.00"),
                    "linear_regression_coefficients": (Decimal("0.00"), Decimal("0.00")),
                },
                "internet_bill": {
                    "average": Decimal("83.99"),
                    "median": Decimal("83.99"),
                    "variance": Decimal("0.00"),
                    "standard_deviation": Decimal("0.00"),
                    "linear_regression_coefficients": (Decimal("0.00"), Decimal("83.99")),
                },
                "laundry": {
                    "average": Decimal("17.08"),
                    "median": Decimal("12.50"),
                    "variance": Decimal("381.08"),
                    "standard_deviation": Decimal("19.52"),
                    "linear_regression_coefficients": (Decimal("4.14"), Decimal("-5.69")),
                },
                "misc": {
                    "average": Decimal("64.25"),
                    "median": Decimal("0.00"),
                    "variance": Decimal("24722.35"),
                    "standard_deviation": Decimal("157.23"),
                    "linear_regression_coefficients": (Decimal("12.89"), Decimal("-6.64")),
                },
                "mortgage": {
                    "average": Decimal("0.00"),
                    "median": Decimal("0.00"),
                    "variance": Decimal("0.00"),
                    "standard_deviation": Decimal("0.00"),
                    "linear_regression_coefficients": (Decimal("0.00"), Decimal("0.00")),
                },
                "other_insurance": {
                    "average": Decimal("0.00"),
                    "median": Decimal("0.00"),
                    "variance": Decimal("0.00"),
                    "standard_deviation": Decimal("0.00"),
                    "linear_regression_coefficients": (Decimal("0.00"), Decimal("0.00")),
                },
                "rent": {
                    "average": Decimal("1544.53"),
                    "median": Decimal("1122.36"),
                    "variance": Decimal("274998.46"),
                    "standard_deviation": Decimal("524.40"),
                    "linear_regression_coefficients": (Decimal("132.65"), Decimal("814.96")),
                },
                "renters_insurance": {
                    "average": Decimal("19.83"),
                    "median": Decimal("0.00"),
                    "variance": Decimal("786.72"),
                    "standard_deviation": Decimal("28.05"),
                    "linear_regression_coefficients": (Decimal("0.00"), Decimal("19.83")),
                },
                "student_loans": {
                    "average": Decimal("204.70"),
                    "median": Decimal("308.05"),
                    "variance": Decimal("20954.92"),
                    "standard_deviation": Decimal("144.76"),
                    "linear_regression_coefficients": (Decimal("-34.55"), Decimal("394.72")),
                },
                "taxes": {
                    "average": Decimal("34.83"),
                    "median": Decimal("0.00"),
                    "variance": Decimal("13346.97"),
                    "standard_deviation": Decimal("115.53"),
                    "linear_regression_coefficients": (Decimal("-7.31"), Decimal("75.04")),
                },
                "vision_insurance": {
                    "average": Decimal("0.00"),
                    "median": Decimal("0.00"),
                    "variance": Decimal("0.00"),
                    "standard_deviation": Decimal("0.00"),
                    "linear_regression_coefficients": (Decimal("0.00"), Decimal("0.00")),
                },
            },
            "wants": {
                "free_spending": {
                    "average": Decimal("1020.66"),
                    "median": Decimal("1027.80"),
                    "variance": Decimal("77570.47"),
                    "standard_deviation": Decimal("278.51"),
                    "linear_regression_coefficients": (Decimal("29.11"), Decimal("860.56")),
                },
                "misc": {
                    "average": Decimal("0.00"),
                    "median": Decimal("0.00"),
                    "variance": Decimal("0.00"),
                    "standard_deviation": Decimal("0.00"),
                    "linear_regression_coefficients": (Decimal("0.00"), Decimal("0.00")),
                },
                "subscriptions": {
                    "average": Decimal("289.76"),
                    "median": Decimal("325.15"),
                    "variance": Decimal("4139.65"),
                    "standard_deviation": Decimal("64.34"),
                    "linear_regression_coefficients": (Decimal("16.45"), Decimal("199.29")),
                },
                "vacation_spending": {
                    "average": Decimal("507.12"),
                    "median": Decimal("0.00"),
                    "variance": Decimal("767068.93"),
                    "standard_deviation": Decimal("875.82"),
                    "linear_regression_coefficients": (Decimal("21.54"), Decimal("388.66")),
                },
            },
            "savings": {
                "crypto": {
                    "average": Decimal("0.00"),
                    "median": Decimal("0.00"),
                    "variance": Decimal("0.00"),
                    "standard_deviation": Decimal("0.00"),
                    "linear_regression_coefficients": (Decimal("0.00"), Decimal("0.00")),
                },
                "emergency_fund": {
                    "average": Decimal("493.49"),
                    "median": Decimal("467.51"),
                    "variance": Decimal("263223.95"),
                    "standard_deviation": Decimal("513.05"),
                    "linear_regression_coefficients": (Decimal("-11.71"), Decimal("557.90")),
                },
                "investing": {
                    "average": Decimal("251.82"),
                    "median": Decimal("0.00"),
                    "variance": Decimal("171481.67"),
                    "standard_deviation": Decimal("414.10"),
                    "linear_regression_coefficients": (Decimal("-44.44"), Decimal("496.24")),
                },
                "misc": {
                    "average": Decimal("0.00"),
                    "median": Decimal("0.00"),
                    "variance": Decimal("0.00"),
                    "standard_deviation": Decimal("0.00"),
                    "linear_regression_coefficients": (Decimal("0.00"), Decimal("0.00")),
                },
                "retirement": {
                    "average": Decimal("50.00"),
                    "median": Decimal("0.00"),
                    "variance": Decimal("27500.00"),
                    "standard_deviation": Decimal("165.83"),
                    "linear_regression_coefficients": (Decimal("-23.08"), Decimal("176.94")),
                },
            },
            "income": {
                "earnings": {
                    "average": Decimal("4802.20"),
                    "median": Decimal("4182.20"),
                    "variance": Decimal("4150398.42"),
                    "standard_deviation": Decimal("2037.25"),
                    "linear_regression_coefficients": (Decimal("-0.51"), Decimal("4805.01")),
                },
                "tax_returns": {
                    "average": Decimal("20.83"),
                    "median": Decimal("0.00"),
                    "variance": Decimal("4774.31"),
                    "standard_deviation": Decimal("69.10"),
                    "linear_regression_coefficients": (Decimal("9.62"), Decimal("-32.08")),
                },
            },
            "reimbursements": {
                "bills": {
                    "average": Decimal("69.96"),
                    "median": Decimal("75.13"),
                    "variance": Decimal("1219.23"),
                    "standard_deviation": Decimal("34.92"),
                    "linear_regression_coefficients": (Decimal("-2.67"), Decimal("84.65")),
                },
                "credit_card_rewards": {
                    "average": Decimal("53.45"),
                    "median": Decimal("0.00"),
                    "variance": Decimal("6784.19"),
                    "standard_deviation": Decimal("82.37"),
                    "linear_regression_coefficients": (Decimal("10.42"), Decimal("-3.86")),
                },
                "free_spending": {
                    "average": Decimal("101.65"),
                    "median": Decimal("6.00"),
                    "variance": Decimal("25610.96"),
                    "standard_deviation": Decimal("160.03"),
                    "linear_regression_coefficients": (Decimal("23.31"), Decimal("-26.56")),
                },
                "rent": {
                    "average": Decimal("182.50"),
                    "median": Decimal("0.00"),
                    "variance": Decimal("73531.25"),
                    "standard_deviation": Decimal("271.17"),
                    "linear_regression_coefficients": (Decimal("65.03"), Decimal("-175.16")),
                },
            },
        },
        "2021": {},
        "2022": {
            "needs": {
                "car_insurance": {
                    "average": Decimal("144.16"),
                    "median": Decimal("143.34"),
                    "variance": Decimal("2.24"),
                    "standard_deviation": Decimal("1.50"),
                    "linear_regression_coefficients": (Decimal("0.32"), Decimal("142.40")),
                },
                "dental_insurance": {
                    "average": Decimal("0.00"),
                    "median": Decimal("0.00"),
                    "variance": Decimal("0.00"),
                    "standard_deviation": Decimal("0.00"),
                    "linear_regression_coefficients": (Decimal("0.00"), Decimal("0.00")),
                },
                "electric_bill": {
                    "average": Decimal("79.52"),
                    "median": Decimal("86.74"),
                    "variance": Decimal("1296.77"),
                    "standard_deviation": Decimal("36.01"),
                    "linear_regression_coefficients": (Decimal("2.55"), Decimal("65.50")),
                },
                "emergencies": {
                    "average": Decimal("117.18"),
                    "median": Decimal("0.00"),
                    "variance": Decimal("83963.86"),
                    "standard_deviation": Decimal("289.77"),
                    "linear_regression_coefficients": (Decimal("9.07"), Decimal("67.29")),
                },
                "gasoline": {
                    "average": Decimal("207.94"),
                    "median": Decimal("208.13"),
                    "variance": Decimal("7787.95"),
                    "standard_deviation": Decimal("88.25"),
                    "linear_regression_coefficients": (Decimal("0.86"), Decimal("203.21")),
                },
                "groceries": {
                    "average": Decimal("387.60"),
                    "median": Decimal("410.18"),
                    "variance": Decimal("20459.01"),
                    "standard_deviation": Decimal("143.03"),
                    "linear_regression_coefficients": (Decimal("30.36"), Decimal("220.62")),
                },
                "health_insurance": {
                    "average": Decimal("0.00"),
                    "median": Decimal("0.00"),
                    "variance": Decimal("0.00"),
                    "standard_deviation": Decimal("0.00"),
                    "linear_regression_coefficients": (Decimal("0.00"), Decimal("0.00")),
                },
                "internet_bill": {
                    "average": Decimal("83.99"),
                    "median": Decimal("83.99"),
                    "variance": Decimal("0.00"),
                    "standard_deviation": Decimal("0.00"),
                    "linear_regression_coefficients": (Decimal("0.00"), Decimal("83.99")),
                },
                "laundry": {
                    "average": Decimal("17.08"),
                    "median": Decimal("12.50"),
                    "variance": Decimal("381.08"),
                    "standard_deviation": Decimal("19.52"),
                    "linear_regression_coefficients": (Decimal("4.14"), Decimal("-5.69")),
                },
                "misc": {
                    "average": Decimal("64.25"),
                    "median": Decimal("0.00"),
                    "variance": Decimal("24722.35"),
                    "standard_deviation": Decimal("157.23"),
                    "linear_regression_coefficients": (Decimal("12.89"), Decimal("-6.64")),
                },
                "mortgage": {
                    "average": Decimal("0.00"),
                    "median": Decimal("0.00"),
                    "variance": Decimal("0.00"),
                    "standard_deviation": Decimal("0.00"),
                    "linear_regression_coefficients": (Decimal("0.00"), Decimal("0.00")),
                },
                "other_insurance": {
                    "average": Decimal("0.00"),
                    "median": Decimal("0.00"),
                    "variance": Decimal("0.00"),
                    "standard_deviation": Decimal("0.00"),
                    "linear_regression_coefficients": (Decimal("0.00"), Decimal("0.00")),
                },
                "rent": {
                    "average": Decimal("1544.53"),
                    "median": Decimal("1122.36"),
                    "variance": Decimal("274998.46"),
                    "standard_deviation": Decimal("524.40"),
                    "linear_regression_coefficients": (Decimal("132.65"), Decimal("814.96")),
                },
                "renters_insurance": {
                    "average": Decimal("19.83"),
                    "median": Decimal("0.00"),
                    "variance": Decimal("786.72"),
                    "standard_deviation": Decimal("28.05"),
                    "linear_regression_coefficients": (Decimal("0.00"), Decimal("19.83")),
                },
                "student_loans": {
                    "average": Decimal("204.70"),
                    "median": Decimal("308.05"),
                    "variance": Decimal("20954.92"),
                    "standard_deviation": Decimal("144.76"),
                    "linear_regression_coefficients": (Decimal("-34.55"), Decimal("394.72")),
                },
                "taxes": {
                    "average": Decimal("34.83"),
                    "median": Decimal("0.00"),
                    "variance": Decimal("13346.97"),
                    "standard_deviation": Decimal("115.53"),
                    "linear_regression_coefficients": (Decimal("-7.31"), Decimal("75.04")),
                },
                "vision_insurance": {
                    "average": Decimal("0.00"),
                    "median": Decimal("0.00"),
                    "variance": Decimal("0.00"),
                    "standard_deviation": Decimal("0.00"),
                    "linear_regression_coefficients": (Decimal("0.00"), Decimal("0.00")),
                },
            },
            "wants": {
                "free_spending": {
                    "average": Decimal("1020.66"),
                    "median": Decimal("1027.80"),
                    "variance": Decimal("77570.47"),
                    "standard_deviation": Decimal("278.51"),
                    "linear_regression_coefficients": (Decimal("29.11"), Decimal("860.56")),
                },
                "misc": {
                    "average": Decimal("0.00"),
                    "median": Decimal("0.00"),
                    "variance": Decimal("0.00"),
                    "standard_deviation": Decimal("0.00"),
                    "linear_regression_coefficients": (Decimal("0.00"), Decimal("0.00")),
                },
                "subscriptions": {
                    "average": Decimal("289.76"),
                    "median": Decimal("325.15"),
                    "variance": Decimal("4139.65"),
                    "standard_deviation": Decimal("64.34"),
                    "linear_regression_coefficients": (Decimal("16.45"), Decimal("199.29")),
                },
                "vacation_spending": {
                    "average": Decimal("507.12"),
                    "median": Decimal("0.00"),
                    "variance": Decimal("767068.93"),
                    "standard_deviation": Decimal("875.82"),
                    "linear_regression_coefficients": (Decimal("21.54"), Decimal("388.66")),
                },
            },
            "savings": {
                "crypto": {
                    "average": Decimal("0.00"),
                    "median": Decimal("0.00"),
                    "variance": Decimal("0.00"),
                    "standard_deviation": Decimal("0.00"),
                    "linear_regression_coefficients": (Decimal("0.00"), Decimal("0.00")),
                },
                "emergency_fund": {
                    "average": Decimal("493.49"),
                    "median": Decimal("467.51"),
                    "variance": Decimal("263223.95"),
                    "standard_deviation": Decimal("513.05"),
                    "linear_regression_coefficients": (Decimal("-11.71"), Decimal("557.90")),
                },
                "investing": {
                    "average": Decimal("251.82"),
                    "median": Decimal("0.00"),
                    "variance": Decimal("171481.67"),
                    "standard_deviation": Decimal("414.10"),
                    "linear_regression_coefficients": (Decimal("-44.44"), Decimal("496.24")),
                },
                "misc": {
                    "average": Decimal("0.00"),
                    "median": Decimal("0.00"),
                    "variance": Decimal("0.00"),
                    "standard_deviation": Decimal("0.00"),
                    "linear_regression_coefficients": (Decimal("0.00"), Decimal("0.00")),
                },
                "retirement": {
                    "average": Decimal("50.00"),
                    "median": Decimal("0.00"),
                    "variance": Decimal("27500.00"),
                    "standard_deviation": Decimal("165.83"),
                    "linear_regression_coefficients": (Decimal("-23.08"), Decimal("176.94")),
                },
            },
            "income": {
                "earnings": {
                    "average": Decimal("4802.20"),
                    "median": Decimal("4182.20"),
                    "variance": Decimal("4150398.42"),
                    "standard_deviation": Decimal("2037.25"),
                    "linear_regression_coefficients": (Decimal("-0.51"), Decimal("4805.01")),
                },
                "tax_returns": {
                    "average": Decimal("20.83"),
                    "median": Decimal("0.00"),
                    "variance": Decimal("4774.31"),
                    "standard_deviation": Decimal("69.10"),
                    "linear_regression_coefficients": (Decimal("9.62"), Decimal("-32.08")),
                },
            },
            "reimbursements": {
                "bills": {
                    "average": Decimal("69.96"),
                    "median": Decimal("75.13"),
                    "variance": Decimal("1219.23"),
                    "standard_deviation": Decimal("34.92"),
                    "linear_regression_coefficients": (Decimal("-2.67"), Decimal("84.65")),
                },
                "credit_card_rewards": {
                    "average": Decimal("53.45"),
                    "median": Decimal("0.00"),
                    "variance": Decimal("6784.19"),
                    "standard_deviation": Decimal("82.37"),
                    "linear_regression_coefficients": (Decimal("10.42"), Decimal("-3.86")),
                },
                "free_spending": {
                    "average": Decimal("101.65"),
                    "median": Decimal("6.00"),
                    "variance": Decimal("25610.96"),
                    "standard_deviation": Decimal("160.03"),
                    "linear_regression_coefficients": (Decimal("23.31"), Decimal("-26.56")),
                },
                "rent": {
                    "average": Decimal("182.50"),
                    "median": Decimal("0.00"),
                    "variance": Decimal("73531.25"),
                    "standard_deviation": Decimal("271.17"),
                    "linear_regression_coefficients": (Decimal("65.03"), Decimal("-175.16")),
                },
            },
        },
        "2023": {},
    }

    return expected_analysis_dict


def get_expected_analysis_dict3():
    """Returns the expected analysis dictionary dictionary pertaining to data from /tests/files/spending3.tsv"""

    expected_analysis_dict = {
        "lifetime": {
            "needs": {
                "car_insurance": {
                    "average": Decimal("143.22"),
                    "median": Decimal("142.80"),
                    "variance": Decimal("6.09"),
                    "standard_deviation": Decimal("2.47"),
                    "linear_regression_coefficients": (Decimal("0.29"), Decimal("139.60")),
                },
                "dental_insurance": {
                    "average": Decimal("0.00"),
                    "median": Decimal("0.00"),
                    "variance": Decimal("0.00"),
                    "standard_deviation": Decimal("0.00"),
                    "linear_regression_coefficients": (Decimal("0.00"), Decimal("0.00")),
                },
                "electric_bill": {
                    "average": Decimal("82.63"),
                    "median": Decimal("79.12"),
                    "variance": Decimal("2125.94"),
                    "standard_deviation": Decimal("46.11"),
                    "linear_regression_coefficients": (Decimal("2.48"), Decimal("51.63")),
                },
                "emergencies": {
                    "average": Decimal("84.22"),
                    "median": Decimal("0.00"),
                    "variance": Decimal("46030.50"),
                    "standard_deviation": Decimal("214.55"),
                    "linear_regression_coefficients": (Decimal("5.64"), Decimal("13.72")),
                },
                "gasoline": {
                    "average": Decimal("183.98"),
                    "median": Decimal("174.94"),
                    "variance": Decimal("6287.19"),
                    "standard_deviation": Decimal("79.29"),
                    "linear_regression_coefficients": (Decimal("-0.36"), Decimal("188.48")),
                },
                "groceries": {
                    "average": Decimal("328.48"),
                    "median": Decimal("348.60"),
                    "variance": Decimal("27332.31"),
                    "standard_deviation": Decimal("165.32"),
                    "linear_regression_coefficients": (Decimal("11.64"), Decimal("182.98")),
                },
                "health_insurance": {
                    "average": Decimal("0.00"),
                    "median": Decimal("0.00"),
                    "variance": Decimal("0.00"),
                    "standard_deviation": Decimal("0.00"),
                    "linear_regression_coefficients": (Decimal("0.00"), Decimal("0.00")),
                },
                "internet_bill": {
                    "average": Decimal("80.61"),
                    "median": Decimal("83.99"),
                    "variance": Decimal("34.08"),
                    "standard_deviation": Decimal("5.84"),
                    "linear_regression_coefficients": (Decimal("0.05"), Decimal("79.98")),
                },
                "laundry": {
                    "average": Decimal("18.65"),
                    "median": Decimal("10.00"),
                    "variance": Decimal("501.07"),
                    "standard_deviation": Decimal("22.38"),
                    "linear_regression_coefficients": (Decimal("2.09"), Decimal("-7.47")),
                },
                "misc": {
                    "average": Decimal("41.68"),
                    "median": Decimal("0.00"),
                    "variance": Decimal("13882.62"),
                    "standard_deviation": Decimal("117.82"),
                    "linear_regression_coefficients": (Decimal("1.71"), Decimal("20.30")),
                },
                "mortgage": {
                    "average": Decimal("0.00"),
                    "median": Decimal("0.00"),
                    "variance": Decimal("0.00"),
                    "standard_deviation": Decimal("0.00"),
                    "linear_regression_coefficients": (Decimal("0.00"), Decimal("0.00")),
                },
                "other_insurance": {
                    "average": Decimal("0.00"),
                    "median": Decimal("0.00"),
                    "variance": Decimal("0.00"),
                    "standard_deviation": Decimal("0.00"),
                    "linear_regression_coefficients": (Decimal("0.00"), Decimal("0.00")),
                },
                "rent": {
                    "average": Decimal("1489.28"),
                    "median": Decimal("1121.00"),
                    "variance": Decimal("320087.59"),
                    "standard_deviation": Decimal("565.76"),
                    "linear_regression_coefficients": (Decimal("64.97"), Decimal("677.15")),
                },
                "renters_insurance": {
                    "average": Decimal("18.31"),
                    "median": Decimal("0.00"),
                    "variance": Decimal("754.14"),
                    "standard_deviation": Decimal("27.46"),
                    "linear_regression_coefficients": (Decimal("-0.00"), Decimal("18.31")),
                },
                "student_loans": {
                    "average": Decimal("257.84"),
                    "median": Decimal("308.05"),
                    "variance": Decimal("104816.55"),
                    "standard_deviation": Decimal("323.75"),
                    "linear_regression_coefficients": (Decimal("-20.80"), Decimal("517.84")),
                },
                "taxes": {
                    "average": Decimal("89.08"),
                    "median": Decimal("0.00"),
                    "variance": Decimal("57944.46"),
                    "standard_deviation": Decimal("240.72"),
                    "linear_regression_coefficients": (Decimal("10.63"), Decimal("-43.80")),
                },
                "vision_insurance": {
                    "average": Decimal("0.00"),
                    "median": Decimal("0.00"),
                    "variance": Decimal("0.00"),
                    "standard_deviation": Decimal("0.00"),
                    "linear_regression_coefficients": (Decimal("0.00"), Decimal("0.00")),
                },
            },
            "wants": {
                "free_spending": {
                    "average": Decimal("1135.67"),
                    "median": Decimal("1071.10"),
                    "variance": Decimal("188009.29"),
                    "standard_deviation": Decimal("433.60"),
                    "linear_regression_coefficients": (Decimal("-6.14"), Decimal("1212.42")),
                },
                "misc": {
                    "average": Decimal("0.00"),
                    "median": Decimal("0.00"),
                    "variance": Decimal("0.00"),
                    "standard_deviation": Decimal("0.00"),
                    "linear_regression_coefficients": (Decimal("0.00"), Decimal("0.00")),
                },
                "subscriptions": {
                    "average": Decimal("245.69"),
                    "median": Decimal("243.98"),
                    "variance": Decimal("9021.56"),
                    "standard_deviation": Decimal("94.98"),
                    "linear_regression_coefficients": (Decimal("10.99"), Decimal("108.32")),
                },
                "vacation_spending": {
                    "average": Decimal("332.59"),
                    "median": Decimal("0.00"),
                    "variance": Decimal("426981.03"),
                    "standard_deviation": Decimal("653.44"),
                    "linear_regression_coefficients": (Decimal("26.31"), Decimal("3.71")),
                },
            },
            "savings": {
                "crypto": {
                    "average": Decimal("86.43"),
                    "median": Decimal("0.00"),
                    "variance": Decimal("12250.12"),
                    "standard_deviation": Decimal("110.68"),
                    "linear_regression_coefficients": (Decimal("-12.18"), Decimal("238.68")),
                },
                "emergency_fund": {
                    "average": Decimal("327.76"),
                    "median": Decimal("250.00"),
                    "variance": Decimal("171842.64"),
                    "standard_deviation": Decimal("414.54"),
                    "linear_regression_coefficients": (Decimal("-6.50"), Decimal("409.02")),
                },
                "investing": {
                    "average": Decimal("257.84"),
                    "median": Decimal("150.00"),
                    "variance": Decimal("106011.77"),
                    "standard_deviation": Decimal("325.59"),
                    "linear_regression_coefficients": (Decimal("-16.49"), Decimal("463.96")),
                },
                "misc": {
                    "average": Decimal("0.00"),
                    "median": Decimal("0.00"),
                    "variance": Decimal("0.00"),
                    "standard_deviation": Decimal("0.00"),
                    "linear_regression_coefficients": (Decimal("0.00"), Decimal("0.00")),
                },
                "retirement": {
                    "average": Decimal("176.91"),
                    "median": Decimal("0.00"),
                    "variance": Decimal("88682.94"),
                    "standard_deviation": Decimal("297.80"),
                    "linear_regression_coefficients": (Decimal("10.05"), Decimal("51.28")),
                },
            },
            "income": {
                "earnings": {
                    "average": Decimal("4633.18"),
                    "median": Decimal("4242.19"),
                    "variance": Decimal("2253272.29"),
                    "standard_deviation": Decimal("1501.09"),
                    "linear_regression_coefficients": (Decimal("32.69"), Decimal("4224.56")),
                },
                "tax_returns": {
                    "average": Decimal("36.69"),
                    "median": Decimal("0.00"),
                    "variance": Decimal("10672.37"),
                    "standard_deviation": Decimal("103.31"),
                    "linear_regression_coefficients": (Decimal("2.45"), Decimal("6.07")),
                },
            },
            "reimbursements": {
                "bills": {
                    "average": Decimal("76.67"),
                    "median": Decimal("78.99"),
                    "variance": Decimal("1270.32"),
                    "standard_deviation": Decimal("35.64"),
                    "linear_regression_coefficients": (Decimal("-1.16"), Decimal("91.17")),
                },
                "credit_card_rewards": {
                    "average": Decimal("48.89"),
                    "median": Decimal("0.00"),
                    "variance": Decimal("9886.87"),
                    "standard_deviation": Decimal("99.43"),
                    "linear_regression_coefficients": (Decimal("0.69"), Decimal("40.27")),
                },
                "free_spending": {
                    "average": Decimal("65.41"),
                    "median": Decimal("0.00"),
                    "variance": Decimal("14417.84"),
                    "standard_deviation": Decimal("120.07"),
                    "linear_regression_coefficients": (Decimal("5.01"), Decimal("2.79")),
                },
                "rent": {
                    "average": Decimal("183.46"),
                    "median": Decimal("0.00"),
                    "variance": Decimal("79655.33"),
                    "standard_deviation": Decimal("282.23"),
                    "linear_regression_coefficients": (Decimal("30.26"), Decimal("-194.79")),
                },
            },
        },
        "2021": {
            "needs": {
                "car_insurance": {
                    "average": Decimal("141.02"),
                    "median": Decimal("140.90"),
                    "variance": Decimal("4.17"),
                    "standard_deviation": Decimal("2.04"),
                    "linear_regression_coefficients": (Decimal("0.58"), Decimal("138.40")),
                },
                "dental_insurance": {
                    "average": Decimal("0.00"),
                    "median": Decimal("0.00"),
                    "variance": Decimal("0.00"),
                    "standard_deviation": Decimal("0.00"),
                    "linear_regression_coefficients": (Decimal("0.00"), Decimal("0.00")),
                },
                "electric_bill": {
                    "average": Decimal("65.81"),
                    "median": Decimal("66.00"),
                    "variance": Decimal("594.68"),
                    "standard_deviation": Decimal("24.39"),
                    "linear_regression_coefficients": (Decimal("-0.68"), Decimal("68.87")),
                },
                "emergencies": {
                    "average": Decimal("28.86"),
                    "median": Decimal("0.00"),
                    "variance": Decimal("7496.62"),
                    "standard_deviation": Decimal("86.58"),
                    "linear_regression_coefficients": (Decimal("-8.75"), Decimal("68.24")),
                },
                "gasoline": {
                    "average": Decimal("175.02"),
                    "median": Decimal("151.94"),
                    "variance": Decimal("2863.59"),
                    "standard_deviation": Decimal("53.51"),
                    "linear_regression_coefficients": (Decimal("-0.32"), Decimal("176.46")),
                },
                "groceries": {
                    "average": Decimal("220.48"),
                    "median": Decimal("195.32"),
                    "variance": Decimal("23085.50"),
                    "standard_deviation": Decimal("151.94"),
                    "linear_regression_coefficients": (Decimal("-28.95"), Decimal("350.76")),
                },
                "health_insurance": {
                    "average": Decimal("0.00"),
                    "median": Decimal("0.00"),
                    "variance": Decimal("0.00"),
                    "standard_deviation": Decimal("0.00"),
                    "linear_regression_coefficients": (Decimal("0.00"), Decimal("0.00")),
                },
                "internet_bill": {
                    "average": Decimal("78.99"),
                    "median": Decimal("78.99"),
                    "variance": Decimal("25.00"),
                    "standard_deviation": Decimal("5.00"),
                    "linear_regression_coefficients": (Decimal("1.52"), Decimal("72.15")),
                },
                "laundry": {
                    "average": Decimal("6.00"),
                    "median": Decimal("0.00"),
                    "variance": Decimal("144.00"),
                    "standard_deviation": Decimal("12.00"),
                    "linear_regression_coefficients": (Decimal("-1.21"), Decimal("11.44")),
                },
                "misc": {
                    "average": Decimal("31.27"),
                    "median": Decimal("0.00"),
                    "variance": Decimal("5013.41"),
                    "standard_deviation": Decimal("70.81"),
                    "linear_regression_coefficients": (Decimal("10.21"), Decimal("-14.68")),
                },
                "mortgage": {
                    "average": Decimal("0.00"),
                    "median": Decimal("0.00"),
                    "variance": Decimal("0.00"),
                    "standard_deviation": Decimal("0.00"),
                    "linear_regression_coefficients": (Decimal("0.00"), Decimal("0.00")),
                },
                "other_insurance": {
                    "average": Decimal("0.00"),
                    "median": Decimal("0.00"),
                    "variance": Decimal("0.00"),
                    "standard_deviation": Decimal("0.00"),
                    "linear_regression_coefficients": (Decimal("0.00"), Decimal("0.00")),
                },
                "rent": {
                    "average": Decimal("1066.27"),
                    "median": Decimal("1035.44"),
                    "variance": Decimal("1522.63"),
                    "standard_deviation": Decimal("39.02"),
                    "linear_regression_coefficients": (Decimal("11.87"), Decimal("1012.85")),
                },
                "renters_insurance": {
                    "average": Decimal("17.85"),
                    "median": Decimal("0.00"),
                    "variance": Decimal("743.45"),
                    "standard_deviation": Decimal("27.27"),
                    "linear_regression_coefficients": (Decimal("1.08"), Decimal("12.99")),
                },
                "student_loans": {
                    "average": Decimal("424.75"),
                    "median": Decimal("308.05"),
                    "variance": Decimal("189537.09"),
                    "standard_deviation": Decimal("435.36"),
                    "linear_regression_coefficients": (Decimal("13.70"), Decimal("363.10")),
                },
                "taxes": {
                    "average": Decimal("34.50"),
                    "median": Decimal("0.00"),
                    "variance": Decimal("10712.25"),
                    "standard_deviation": Decimal("103.50"),
                    "linear_regression_coefficients": (Decimal("-10.45"), Decimal("81.52")),
                },
                "vision_insurance": {
                    "average": Decimal("0.00"),
                    "median": Decimal("0.00"),
                    "variance": Decimal("0.00"),
                    "standard_deviation": Decimal("0.00"),
                    "linear_regression_coefficients": (Decimal("0.00"), Decimal("0.00")),
                },
            },
            "wants": {
                "free_spending": {
                    "average": Decimal("1289.32"),
                    "median": Decimal("1115.41"),
                    "variance": Decimal("308581.58"),
                    "standard_deviation": Decimal("555.50"),
                    "linear_regression_coefficients": (Decimal("59.56"), Decimal("1021.30")),
                },
                "misc": {
                    "average": Decimal("0.00"),
                    "median": Decimal("0.00"),
                    "variance": Decimal("0.00"),
                    "standard_deviation": Decimal("0.00"),
                    "linear_regression_coefficients": (Decimal("0.00"), Decimal("0.00")),
                },
                "subscriptions": {
                    "average": Decimal("151.74"),
                    "median": Decimal("161.72"),
                    "variance": Decimal("3114.31"),
                    "standard_deviation": Decimal("55.81"),
                    "linear_regression_coefficients": (Decimal("1.22"), Decimal("146.25")),
                },
                "vacation_spending": {
                    "average": Decimal("78.21"),
                    "median": Decimal("0.00"),
                    "variance": Decimal("24469.85"),
                    "standard_deviation": Decimal("156.43"),
                    "linear_regression_coefficients": (Decimal("37.87"), Decimal("-92.21")),
                },
            },
            "savings": {
                "crypto": {
                    "average": Decimal("224.73"),
                    "median": Decimal("228.64"),
                    "variance": Decimal("772.02"),
                    "standard_deviation": Decimal("27.79"),
                    "linear_regression_coefficients": (Decimal("2.05"), Decimal("215.50")),
                },
                "emergency_fund": {
                    "average": Decimal("260.00"),
                    "median": Decimal("300.00"),
                    "variance": Decimal("50400.00"),
                    "standard_deviation": Decimal("224.50"),
                    "linear_regression_coefficients": (Decimal("-58.18"), Decimal("521.81")),
                },
                "investing": {
                    "average": Decimal("353.20"),
                    "median": Decimal("436.00"),
                    "variance": Decimal("40608.16"),
                    "standard_deviation": Decimal("201.51"),
                    "linear_regression_coefficients": (Decimal("-0.51"), Decimal("355.50")),
                },
                "misc": {
                    "average": Decimal("0.00"),
                    "median": Decimal("0.00"),
                    "variance": Decimal("0.00"),
                    "standard_deviation": Decimal("0.00"),
                    "linear_regression_coefficients": (Decimal("0.00"), Decimal("0.00")),
                },
                "retirement": {
                    "average": Decimal("120.00"),
                    "median": Decimal("0.00"),
                    "variance": Decimal("65600.00"),
                    "standard_deviation": Decimal("256.12"),
                    "linear_regression_coefficients": (Decimal("-60.61"), Decimal("392.74")),
                },
            },
            "income": {
                "earnings": {
                    "average": Decimal("4296.41"),
                    "median": Decimal("4295.08"),
                    "variance": Decimal("518469.93"),
                    "standard_deviation": Decimal("720.05"),
                    "linear_regression_coefficients": (Decimal("-13.68"), Decimal("4357.97")),
                },
                "tax_returns": {
                    "average": Decimal("31.90"),
                    "median": Decimal("0.00"),
                    "variance": Decimal("9158.49"),
                    "standard_deviation": Decimal("95.70"),
                    "linear_regression_coefficients": (Decimal("-9.67"), Decimal("75.42")),
                },
            },
            "reimbursements": {
                "bills": {
                    "average": Decimal("88.08"),
                    "median": Decimal("82.82"),
                    "variance": Decimal("616.91"),
                    "standard_deviation": Decimal("24.84"),
                    "linear_regression_coefficients": (Decimal("4.67"), Decimal("67.06")),
                },
                "credit_card_rewards": {
                    "average": Decimal("49.63"),
                    "median": Decimal("0.00"),
                    "variance": Decimal("16107.86"),
                    "standard_deviation": Decimal("126.92"),
                    "linear_regression_coefficients": (Decimal("0.41"), Decimal("47.79")),
                },
                "free_spending": {
                    "average": Decimal("23.83"),
                    "median": Decimal("0.00"),
                    "variance": Decimal("1431.55"),
                    "standard_deviation": Decimal("37.84"),
                    "linear_regression_coefficients": (Decimal("-4.07"), Decimal("42.14")),
                },
                "rent": {
                    "average": Decimal("0.00"),
                    "median": Decimal("0.00"),
                    "variance": Decimal("0.00"),
                    "standard_deviation": Decimal("0.00"),
                    "linear_regression_coefficients": (Decimal("0.00"), Decimal("0.00")),
                },
            },
        },
        "2022": {
            "needs": {
                "car_insurance": {
                    "average": Decimal("144.16"),
                    "median": Decimal("143.34"),
                    "variance": Decimal("2.24"),
                    "standard_deviation": Decimal("1.50"),
                    "linear_regression_coefficients": (Decimal("0.32"), Decimal("142.40")),
                },
                "dental_insurance": {
                    "average": Decimal("0.00"),
                    "median": Decimal("0.00"),
                    "variance": Decimal("0.00"),
                    "standard_deviation": Decimal("0.00"),
                    "linear_regression_coefficients": (Decimal("0.00"), Decimal("0.00")),
                },
                "electric_bill": {
                    "average": Decimal("79.52"),
                    "median": Decimal("86.74"),
                    "variance": Decimal("1296.77"),
                    "standard_deviation": Decimal("36.01"),
                    "linear_regression_coefficients": (Decimal("2.55"), Decimal("65.50")),
                },
                "emergencies": {
                    "average": Decimal("117.18"),
                    "median": Decimal("0.00"),
                    "variance": Decimal("83963.86"),
                    "standard_deviation": Decimal("289.77"),
                    "linear_regression_coefficients": (Decimal("9.07"), Decimal("67.29")),
                },
                "gasoline": {
                    "average": Decimal("207.94"),
                    "median": Decimal("208.13"),
                    "variance": Decimal("7787.95"),
                    "standard_deviation": Decimal("88.25"),
                    "linear_regression_coefficients": (Decimal("0.86"), Decimal("203.21")),
                },
                "groceries": {
                    "average": Decimal("387.60"),
                    "median": Decimal("410.18"),
                    "variance": Decimal("20459.01"),
                    "standard_deviation": Decimal("143.03"),
                    "linear_regression_coefficients": (Decimal("30.36"), Decimal("220.62")),
                },
                "health_insurance": {
                    "average": Decimal("0.00"),
                    "median": Decimal("0.00"),
                    "variance": Decimal("0.00"),
                    "standard_deviation": Decimal("0.00"),
                    "linear_regression_coefficients": (Decimal("0.00"), Decimal("0.00")),
                },
                "internet_bill": {
                    "average": Decimal("83.99"),
                    "median": Decimal("83.99"),
                    "variance": Decimal("0.00"),
                    "standard_deviation": Decimal("0.00"),
                    "linear_regression_coefficients": (Decimal("0.00"), Decimal("83.99")),
                },
                "laundry": {
                    "average": Decimal("17.08"),
                    "median": Decimal("12.50"),
                    "variance": Decimal("381.08"),
                    "standard_deviation": Decimal("19.52"),
                    "linear_regression_coefficients": (Decimal("4.14"), Decimal("-5.69")),
                },
                "misc": {
                    "average": Decimal("64.25"),
                    "median": Decimal("0.00"),
                    "variance": Decimal("24722.35"),
                    "standard_deviation": Decimal("157.23"),
                    "linear_regression_coefficients": (Decimal("12.89"), Decimal("-6.64")),
                },
                "mortgage": {
                    "average": Decimal("0.00"),
                    "median": Decimal("0.00"),
                    "variance": Decimal("0.00"),
                    "standard_deviation": Decimal("0.00"),
                    "linear_regression_coefficients": (Decimal("0.00"), Decimal("0.00")),
                },
                "other_insurance": {
                    "average": Decimal("0.00"),
                    "median": Decimal("0.00"),
                    "variance": Decimal("0.00"),
                    "standard_deviation": Decimal("0.00"),
                    "linear_regression_coefficients": (Decimal("0.00"), Decimal("0.00")),
                },
                "rent": {
                    "average": Decimal("1544.53"),
                    "median": Decimal("1122.36"),
                    "variance": Decimal("274998.46"),
                    "standard_deviation": Decimal("524.40"),
                    "linear_regression_coefficients": (Decimal("132.65"), Decimal("814.96")),
                },
                "renters_insurance": {
                    "average": Decimal("19.83"),
                    "median": Decimal("0.00"),
                    "variance": Decimal("786.72"),
                    "standard_deviation": Decimal("28.05"),
                    "linear_regression_coefficients": (Decimal("0.00"), Decimal("19.83")),
                },
                "student_loans": {
                    "average": Decimal("204.70"),
                    "median": Decimal("308.05"),
                    "variance": Decimal("20954.92"),
                    "standard_deviation": Decimal("144.76"),
                    "linear_regression_coefficients": (Decimal("-34.55"), Decimal("394.72")),
                },
                "taxes": {
                    "average": Decimal("34.83"),
                    "median": Decimal("0.00"),
                    "variance": Decimal("13346.97"),
                    "standard_deviation": Decimal("115.53"),
                    "linear_regression_coefficients": (Decimal("-7.31"), Decimal("75.04")),
                },
                "vision_insurance": {
                    "average": Decimal("0.00"),
                    "median": Decimal("0.00"),
                    "variance": Decimal("0.00"),
                    "standard_deviation": Decimal("0.00"),
                    "linear_regression_coefficients": (Decimal("0.00"), Decimal("0.00")),
                },
            },
            "wants": {
                "free_spending": {
                    "average": Decimal("1020.66"),
                    "median": Decimal("1027.80"),
                    "variance": Decimal("77570.47"),
                    "standard_deviation": Decimal("278.51"),
                    "linear_regression_coefficients": (Decimal("29.11"), Decimal("860.56")),
                },
                "misc": {
                    "average": Decimal("0.00"),
                    "median": Decimal("0.00"),
                    "variance": Decimal("0.00"),
                    "standard_deviation": Decimal("0.00"),
                    "linear_regression_coefficients": (Decimal("0.00"), Decimal("0.00")),
                },
                "subscriptions": {
                    "average": Decimal("289.76"),
                    "median": Decimal("325.15"),
                    "variance": Decimal("4139.65"),
                    "standard_deviation": Decimal("64.34"),
                    "linear_regression_coefficients": (Decimal("16.45"), Decimal("199.29")),
                },
                "vacation_spending": {
                    "average": Decimal("507.12"),
                    "median": Decimal("0.00"),
                    "variance": Decimal("767068.93"),
                    "standard_deviation": Decimal("875.82"),
                    "linear_regression_coefficients": (Decimal("21.54"), Decimal("388.66")),
                },
            },
            "savings": {
                "crypto": {
                    "average": Decimal("0.00"),
                    "median": Decimal("0.00"),
                    "variance": Decimal("0.00"),
                    "standard_deviation": Decimal("0.00"),
                    "linear_regression_coefficients": (Decimal("0.00"), Decimal("0.00")),
                },
                "emergency_fund": {
                    "average": Decimal("493.49"),
                    "median": Decimal("467.51"),
                    "variance": Decimal("263223.95"),
                    "standard_deviation": Decimal("513.05"),
                    "linear_regression_coefficients": (Decimal("-11.71"), Decimal("557.90")),
                },
                "investing": {
                    "average": Decimal("251.82"),
                    "median": Decimal("0.00"),
                    "variance": Decimal("171481.67"),
                    "standard_deviation": Decimal("414.10"),
                    "linear_regression_coefficients": (Decimal("-44.44"), Decimal("496.24")),
                },
                "misc": {
                    "average": Decimal("0.00"),
                    "median": Decimal("0.00"),
                    "variance": Decimal("0.00"),
                    "standard_deviation": Decimal("0.00"),
                    "linear_regression_coefficients": (Decimal("0.00"), Decimal("0.00")),
                },
                "retirement": {
                    "average": Decimal("50.00"),
                    "median": Decimal("0.00"),
                    "variance": Decimal("27500.00"),
                    "standard_deviation": Decimal("165.83"),
                    "linear_regression_coefficients": (Decimal("-23.08"), Decimal("176.94")),
                },
            },
            "income": {
                "earnings": {
                    "average": Decimal("4802.20"),
                    "median": Decimal("4182.20"),
                    "variance": Decimal("4150398.42"),
                    "standard_deviation": Decimal("2037.25"),
                    "linear_regression_coefficients": (Decimal("-0.51"), Decimal("4805.01")),
                },
                "tax_returns": {
                    "average": Decimal("20.83"),
                    "median": Decimal("0.00"),
                    "variance": Decimal("4774.31"),
                    "standard_deviation": Decimal("69.10"),
                    "linear_regression_coefficients": (Decimal("9.62"), Decimal("-32.08")),
                },
            },
            "reimbursements": {
                "bills": {
                    "average": Decimal("69.96"),
                    "median": Decimal("75.13"),
                    "variance": Decimal("1219.23"),
                    "standard_deviation": Decimal("34.92"),
                    "linear_regression_coefficients": (Decimal("-2.67"), Decimal("84.65")),
                },
                "credit_card_rewards": {
                    "average": Decimal("53.45"),
                    "median": Decimal("0.00"),
                    "variance": Decimal("6784.19"),
                    "standard_deviation": Decimal("82.37"),
                    "linear_regression_coefficients": (Decimal("10.42"), Decimal("-3.86")),
                },
                "free_spending": {
                    "average": Decimal("101.65"),
                    "median": Decimal("6.00"),
                    "variance": Decimal("25610.96"),
                    "standard_deviation": Decimal("160.03"),
                    "linear_regression_coefficients": (Decimal("23.31"), Decimal("-26.56")),
                },
                "rent": {
                    "average": Decimal("182.50"),
                    "median": Decimal("0.00"),
                    "variance": Decimal("73531.25"),
                    "standard_deviation": Decimal("271.17"),
                    "linear_regression_coefficients": (Decimal("65.03"), Decimal("-175.16")),
                },
            },
        },
        "2023": {
            "needs": {
                "car_insurance": {
                    "average": Decimal("145.92"),
                    "median": Decimal("145.60"),
                    "variance": Decimal("0.31"),
                    "standard_deviation": Decimal("0.55"),
                    "linear_regression_coefficients": (Decimal("-0.13"), Decimal("146.12")),
                },
                "dental_insurance": {
                    "average": Decimal("0.00"),
                    "median": Decimal("0.00"),
                    "variance": Decimal("0.00"),
                    "standard_deviation": Decimal("0.00"),
                    "linear_regression_coefficients": (Decimal("0.00"), Decimal("0.00")),
                },
                "electric_bill": {
                    "average": Decimal("134.01"),
                    "median": Decimal("155.98"),
                    "variance": Decimal("5065.77"),
                    "standard_deviation": Decimal("71.17"),
                    "linear_regression_coefficients": (Decimal("-36.06"), Decimal("188.10")),
                },
                "emergencies": {
                    "average": Decimal("123.74"),
                    "median": Decimal("104.09"),
                    "variance": Decimal("16083.02"),
                    "standard_deviation": Decimal("126.82"),
                    "linear_regression_coefficients": (Decimal("65.21"), Decimal("25.92")),
                },
                "gasoline": {
                    "average": Decimal("134.47"),
                    "median": Decimal("118.42"),
                    "variance": Decimal("5969.40"),
                    "standard_deviation": Decimal("77.26"),
                    "linear_regression_coefficients": (Decimal("-3.98"), Decimal("140.44")),
                },
                "groceries": {
                    "average": Decimal("421.10"),
                    "median": Decimal("413.48"),
                    "variance": Decimal("10344.52"),
                    "standard_deviation": Decimal("101.71"),
                    "linear_regression_coefficients": (Decimal("46.55"), Decimal("351.27")),
                },
                "health_insurance": {
                    "average": Decimal("0.00"),
                    "median": Decimal("0.00"),
                    "variance": Decimal("0.00"),
                    "standard_deviation": Decimal("0.00"),
                    "linear_regression_coefficients": (Decimal("0.00"), Decimal("0.00")),
                },
                "internet_bill": {
                    "average": Decimal("74.49"),
                    "median": Decimal("69.99"),
                    "variance": Decimal("80.75"),
                    "standard_deviation": Decimal("8.99"),
                    "linear_regression_coefficients": (Decimal("-5.80"), Decimal("83.19")),
                },
                "laundry": {
                    "average": Decimal("55.00"),
                    "median": Decimal("55.00"),
                    "variance": Decimal("25.00"),
                    "standard_deviation": Decimal("5.00"),
                    "linear_regression_coefficients": (Decimal("2.00"), Decimal("52.00")),
                },
                "misc": {
                    "average": Decimal("0.00"),
                    "median": Decimal("0.00"),
                    "variance": Decimal("0.00"),
                    "standard_deviation": Decimal("0.00"),
                    "linear_regression_coefficients": (Decimal("0.00"), Decimal("0.00")),
                },
                "mortgage": {
                    "average": Decimal("0.00"),
                    "median": Decimal("0.00"),
                    "variance": Decimal("0.00"),
                    "standard_deviation": Decimal("0.00"),
                    "linear_regression_coefficients": (Decimal("0.00"), Decimal("0.00")),
                },
                "other_insurance": {
                    "average": Decimal("0.00"),
                    "median": Decimal("0.00"),
                    "variance": Decimal("0.00"),
                    "standard_deviation": Decimal("0.00"),
                    "linear_regression_coefficients": (Decimal("0.00"), Decimal("0.00")),
                },
                "rent": {
                    "average": Decimal("2381.05"),
                    "median": Decimal("2380.39"),
                    "variance": Decimal("3.62"),
                    "standard_deviation": Decimal("1.90"),
                    "linear_regression_coefficients": (Decimal("0.86"), Decimal("2379.76")),
                },
                "renters_insurance": {
                    "average": Decimal("14.88"),
                    "median": Decimal("0.00"),
                    "variance": Decimal("663.80"),
                    "standard_deviation": Decimal("25.76"),
                    "linear_regression_coefficients": (Decimal("-5.95"), Decimal("23.80")),
                },
                "student_loans": {
                    "average": Decimal("0.00"),
                    "median": Decimal("0.00"),
                    "variance": Decimal("0.00"),
                    "standard_deviation": Decimal("0.00"),
                    "linear_regression_coefficients": (Decimal("0.00"), Decimal("0.00")),
                },
                "taxes": {
                    "average": Decimal("388.25"),
                    "median": Decimal("225.00"),
                    "variance": Decimal("204039.19"),
                    "standard_deviation": Decimal("451.71"),
                    "linear_regression_coefficients": (Decimal("375.90"), Decimal("-175.60")),
                },
                "vision_insurance": {
                    "average": Decimal("0.00"),
                    "median": Decimal("0.00"),
                    "variance": Decimal("0.00"),
                    "standard_deviation": Decimal("0.00"),
                    "linear_regression_coefficients": (Decimal("0.00"), Decimal("0.00")),
                },
            },
            "wants": {
                "free_spending": {
                    "average": Decimal("1096.57"),
                    "median": Decimal("1188.94"),
                    "variance": Decimal("117662.73"),
                    "standard_deviation": Decimal("343.02"),
                    "linear_regression_coefficients": (Decimal("20.75"), Decimal("1065.45")),
                },
                "misc": {
                    "average": Decimal("0.00"),
                    "median": Decimal("0.00"),
                    "variance": Decimal("0.00"),
                    "standard_deviation": Decimal("0.00"),
                    "linear_regression_coefficients": (Decimal("0.00"), Decimal("0.00")),
                },
                "subscriptions": {
                    "average": Decimal("348.37"),
                    "median": Decimal("348.62"),
                    "variance": Decimal("0.19"),
                    "standard_deviation": Decimal("0.43"),
                    "linear_regression_coefficients": (Decimal("0.30"), Decimal("347.92")),
                },
                "vacation_spending": {
                    "average": Decimal("444.91"),
                    "median": Decimal("366.74"),
                    "variance": Decimal("147217.32"),
                    "standard_deviation": Decimal("383.69"),
                    "linear_regression_coefficients": (Decimal("140.87"), Decimal("233.61")),
                },
            },
            "savings": {
                "crypto": {
                    "average": Decimal("0.00"),
                    "median": Decimal("0.00"),
                    "variance": Decimal("0.00"),
                    "standard_deviation": Decimal("0.00"),
                    "linear_regression_coefficients": (Decimal("0.00"), Decimal("0.00")),
                },
                "emergency_fund": {
                    "average": Decimal("0.00"),
                    "median": Decimal("0.00"),
                    "variance": Decimal("0.00"),
                    "standard_deviation": Decimal("0.00"),
                    "linear_regression_coefficients": (Decimal("0.00"), Decimal("0.00")),
                },
                "investing": {
                    "average": Decimal("37.50"),
                    "median": Decimal("25.00"),
                    "variance": Decimal("1718.75"),
                    "standard_deviation": Decimal("41.46"),
                    "linear_regression_coefficients": (Decimal("-35.00"), Decimal("90.00")),
                },
                "misc": {
                    "average": Decimal("0.00"),
                    "median": Decimal("0.00"),
                    "variance": Decimal("0.00"),
                    "standard_deviation": Decimal("0.00"),
                    "linear_regression_coefficients": (Decimal("0.00"), Decimal("0.00")),
                },
                "retirement": {
                    "average": Decimal("699.90"),
                    "median": Decimal("700.00"),
                    "variance": Decimal("0.03"),
                    "standard_deviation": Decimal("0.16"),
                    "linear_regression_coefficients": (Decimal("0.04"), Decimal("699.84")),
                },
            },
            "income": {
                "earnings": {
                    "average": Decimal("4968.04"),
                    "median": Decimal("4694.75"),
                    "variance": Decimal("417521.78"),
                    "standard_deviation": Decimal("646.16"),
                    "linear_regression_coefficients": (Decimal("249.84"), Decimal("4593.28")),
                },
                "tax_returns": {
                    "average": Decimal("96.25"),
                    "median": Decimal("0.00"),
                    "variance": Decimal("27792.19"),
                    "standard_deviation": Decimal("166.71"),
                    "linear_regression_coefficients": (Decimal("115.50"), Decimal("-77.00")),
                },
            },
            "reimbursements": {
                "bills": {
                    "average": Decimal("68.28"),
                    "median": Decimal("77.40"),
                    "variance": Decimal("2526.66"),
                    "standard_deviation": Decimal("50.27"),
                    "linear_regression_coefficients": (Decimal("-34.91"), Decimal("120.65")),
                },
                "credit_card_rewards": {
                    "average": Decimal("33.35"),
                    "median": Decimal("0.00"),
                    "variance": Decimal("3337.17"),
                    "standard_deviation": Decimal("57.77"),
                    "linear_regression_coefficients": (Decimal("13.34"), Decimal("13.34")),
                },
                "free_spending": {
                    "average": Decimal("60.66"),
                    "median": Decimal("31.00"),
                    "variance": Decimal("5019.67"),
                    "standard_deviation": Decimal("70.85"),
                    "linear_regression_coefficients": (Decimal("-19.86"), Decimal("90.45")),
                },
                "rent": {
                    "average": Decimal("645.00"),
                    "median": Decimal("645.00"),
                    "variance": Decimal("0.00"),
                    "standard_deviation": Decimal("0.00"),
                    "linear_regression_coefficients": (Decimal("0.00"), Decimal("645.00")),
                },
            },
        },
    }

    return expected_analysis_dict
