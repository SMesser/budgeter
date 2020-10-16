'''This module defines the top-level operations of Budgeter.'''
from datetime import date, datetime
from logging import getLogger

from .classes import Grouping, Row
logger = getLogger(__name__)

def process_data(config, sheet, unknown):
    '''Loop through the worksheet, updating the Groupings one row at a time'''
    row_num = config.start_row
    done = False
    while not done:
        logger.debug('Reading row {}'.format(row_num))
        row = Row(sheet=sheet, row_num=row_num, config=config)
        if (row.is_empty()):
            done = True
        else:
            logger.debug('Row {} contains data: "{}"'.format(row_num, row.subject))
            found = False
            match = set()
            for group in config.known_groups:
                if group.include_record(row):
                    match.add(group)
            if len(match) == 0:
                unknown.labels[row.subject] = 1.0
            elif len(match) > 1:
                logger.debug(
                    'Row {} satisfies multiple groups: {}'.format(
                        row.subject,
                        match
                    )
                )
        row_num += 1

def restrict_group_to_date_range(group, first, last):
    '''Take an existing group and filter it to records within a date range.'''
    # Copy the group name, but initialize with empty labels, since Grouping
    # stores labels as a dict but initializes it from a list.
    new_group = Grouping(
        '{} between {} and {}'.format(group.name, first, last),
        *[]
    )
    # Copy the labels dict to the new group, including Partial values.
    new_group.labels = dict(group.labels)
    # Copy over the individual records, running them through _process_record() so that
    # various totals are updated appropriately.
    for record in group.records:
        if (record.date >= first) and (record.date <= last):
            new_group._process_record(record)
    return new_group


def report_single_group(group):
    """Describe a group of transactions and their stats."""
    if len(group.records) == 0:
        msg = 'No matching records for group "{}".'.format(group.name)
        logger.warning(msg)
        return '\t {}\n'.format(msg)
    else:
        output_string = ''
        first = group.first_date
        last = group.last_date
        output_string += '\tRange: {} - {}\n'.format(
            first.strftime('%m/%d/%Y'),
            last.strftime('%m/%d/%Y')
        )
        years = (last - first).days/365.25
        if years > 0:
            output_string += '\tNet: {:.2f},\t{:.2f}/year\n'.format(
                group.net,
                group.net/years
            )
            output_string += '\tIncome: {:.2f},\t{:.2f}/year\n'.format(
                group.income,
                group.income/years
            )
            output_string += '\tOutgo: {:.2f},\t{:.2f}/year\n'.format(
                group.outgo,
                group.outgo/years
            )
            output_string += '\tFlux: {:.2f},\t{:.2f}/year\n'.format(
                group.flux,
                group.flux/years
            )
        else:
            msg = 'Per-Year calculations unavailable for single-date group "{}".'.format(group.name)
            logger.warning(msg)
            output_string += '\t{}\n'.format(msg)
            output_string += '\tNet: {:.2f}\n'.format(group.net)
            output_string += '\tIncome: {:.2f}\n'.format(group.income)
            output_string += '\tOutgo: {:.2f}\n'.format(group.outgo)
            output_string += '\tFlux: {:.2f}\n'.format(group.flux)
        return output_string

def report_groups(known_groups):
    '''Output results to terminal'''
    output_string = ''
    for group in known_groups:
        logger.info('Evaluating ' + group.name)
        output_string += group.name + ':\n' + report_single_group(group) + '\n'
        output_string += '  {} for past year:\n'.format(group.name)
        today = datetime.now().date()
        try:
            last_year = date(today.year - 1, today.month, today.day)
        except ValueError:
            # Most likely, today is Feb 29 and last year was not a leap year
            last_year = date(today.year - 1, today.month, today.day-1)
        output_string += report_single_group(restrict_group_to_date_range(
            group,
            first=last_year,
            last=today
        ))
    return output_string
