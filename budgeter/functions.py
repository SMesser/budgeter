'''This module defines the top-level operations of Budgeter.'''
from datetime import date, datetime
from .classes import Grouping, Row

def process_data(config, sheet, unknown):
    '''Loop through the worksheet, updating the Groupings one row at a time'''
    row_num = config.start_row
    done = False
    while not done:
        # print('Reading row {}'.format(row_num))
        row = Row(sheet=sheet, row_num=row_num, config=config)
        if (row.is_empty()):
            done = True
        else:
            # print('Row {} contains data: "{}"'.format(row_num, row.subject))
            found = False
            match = set()
            for group in config.known_groups:
                if group.include_record(row):
                    match.add(group)
            if len(match) == 0:
                unknown.labels[row.subject] = 1.0
            elif len(match) > 1:
                '''print(
                    'Row {} satisfies multiple groups: {}'.format(
                        row.subject,
                        match
                    )
                ) '''
        row_num += 1

def restrict_group_to_date_range(group, first, last):
    '''Take an existing group and filter it to records within a date range.'''
    # Copy the group name, but initialize with empty labels, since Grouping
    # stores labels as a dict but initializes it from a list.
    new_group = Grouping(group.name, *[])
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
        print('\tNo matching records.')
    else:
        first = group.first_date
        last = group.last_date
        print('\tRange: {} - {}'.format(
            first.strftime('%m/%d/%Y'),
            last.strftime('%m/%d/%Y')
        ))
        years = (last - first).days/365.25
        if years > 0:
            print('\tNet: {:.2f},\t{:.2f}/year'.format(
                group.net,
                group.net/years
            ))
            print('\tIncome: {:.2f},\t{:.2f}/year'.format(
                group.income,
                group.income/years
            ))
            print('\tOutgo: {:.2f},\t{:.2f}/year'.format(
                group.outgo,
                group.outgo/years
            ))
            print('\tFlux: {:.2f},\t{:.2f}/year'.format(
                group.flux,
                group.flux/years
            ))
        else:
            print(
                '\tPer-Year calculations unavailable for single-date groups.'
            )
            print('\tNet: {:.2f}'.format(group.net))
            print('\tIncome: {:.2f}'.format(group.income))
            print('\tOutgo: {:.2f}'.format(group.outgo))
            print('\tFlux: {:.2f}'.format(group.flux))

def report_groups(known_groups):
    '''Output results to terminal'''
    for group in known_groups:
        print(group.name + ':')
        report_single_group(group)
        print('  {} for past year:'.format(group.name))
        today = datetime.now().date()
        try:
            last_year = date(today.year - 1, today.month, today.day)
        except ValueError:
            # Most likely, today is Feb 29 and last year was not a leap year
            last_year = date(today.year - 1, today.month, today.day-1)
        report_single_group(restrict_group_to_date_range(
            group,
            first=last_year,
            last=today
        ))

