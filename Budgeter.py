'''Historical budget and future budgeting tool.

Run this module from the command line. It is the intended entry point for
the Budgeter package.
'''

from openpyxl import load_workbook
from pprint import pprint

from config import (
    SHEET_NAME, START_ROW, FILE_PATH, KNOWN_GROUPS,
    DATE_COL, SUBJECT_COL, NET_COL, BALANCE_COL
)
from budgeter.classes import Config, Grouping
from budgeter.functions import process_data, report_groups

UNKNOWN = Grouping('unknown')
CONFIG = Config(
    start_row=START_ROW,
    date_col=DATE_COL,
    subject_col=SUBJECT_COL,
    net_col=NET_COL,
    balance_col=BALANCE_COL,
    known_groups=KNOWN_GROUPS
)

book = load_workbook(FILE_PATH, data_only=True)
print('Workbook opened: ' + FILE_PATH)

sheet = book[SHEET_NAME]
print('Reading Sheet: ' + str(sheet))

process_data(CONFIG, sheet, UNKNOWN)                           

book.close()
print('Book closed.')

if len(UNKNOWN.labels) > 0:
    print('Unknown labels:')
    pprint(sorted(UNKNOWN.labels.keys()))

report_groups(CONFIG.known_groups)
