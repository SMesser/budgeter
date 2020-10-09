'''Historical budget and future budgeting tool.

Run this module from the command line. It is the intended entry point for
the Budgeter package.
'''

import logging
from openpyxl import load_workbook
from pprint import pformat

from config import (
    BALANCE_COL, DATE_COL, DEBUG, FILE_PATH,
    KNOWN_GROUPS, NET_COL, OUTPUT_DIR,
    SHEET_NAME, START_ROW, SUBJECT_COL
)
from budgeter.classes import Config, Grouping
from budgeter.functions import process_data, report_groups

# Configure logging - This is the root logger, so use an empty name
logger = logging.getLogger('')
logger.setLevel(logging.DEBUG)
terminal_log = logging.StreamHandler()
# Overwrite the output.txt file for each run
file_output = logging.FileHandler(OUTPUT_DIR + 'output.txt', mode='w')
formatter = logging.Formatter('%(message)s')

if DEBUG:
    terminal_log.setLevel(logging.DEBUG)
    file_output.setLevel(logging.DEBUG)
else:
    terminal_log.setLevel(logging.INFO)
    file_output.setLevel(logging.INFO)

terminal_log.setFormatter(formatter)
file_output.setFormatter(formatter)
logger.addHandler(terminal_log)
logger.addHandler(file_output)

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
logger.info('Workbook opened: ' + FILE_PATH)

sheet = book[SHEET_NAME]
logger.info('Reading Sheet: ' + str(sheet))

process_data(CONFIG, sheet, UNKNOWN)                           

book.close()
logger.info('Book closed.')

if len(UNKNOWN.labels) > 0:
    logger.info('Unknown labels:')
    logger.info(pformat(sorted(UNKNOWN.labels.keys())))

report_groups(CONFIG.known_groups)
