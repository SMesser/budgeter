'''This module defines the top-level operations of Budgeter.'''
from .classes import Row

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


def report_groups(known_groups):
    '''Output results to terminal'''
    for group in known_groups:
        print(group.name + ':')
        first = group.first_date
        last = group.last_date
        print('\tRange: {} - {}'.format(
            first.strftime('%m/%d/%Y'),
            last.strftime('%m/%d/%Y')
        ))
        years = (last - first).days/365.25
        print('\tNet: {:.2f},\t{:.2f}/year'.format(group.net, group.net/years))
        print('\tIncome: {:.2f},\t{:.2f}/year'.format(
            group.income,
            group.income/years
        ))
        print('\tOutgo: {:.2f},\t{:.2f}/year'.format(group.outgo, group.outgo/years))
        print('\tFlux: {:.2f},\t{:.2f}/year'.format(group.flux, group.flux/years))
