'''This module is reserved for general utility classes.'''

from datetime import datetime

class Config(object):
    ''' Stores broad configuration data.'''
    def __init__(
        self,
        start_row,
        date_col,
        subject_col,
        net_col,
        balance_col,
        known_groups
    ):
        self.start_row = start_row
        self.date_col = date_col
        self.subject_col = subject_col
        self.net_col = net_col
        self.balance_col = balance_col
        self.known_groups = known_groups

class Partial(object):
    """Describe an entry that should only partially toward its parent Grouping."""
    def __init__(self, name, portion=1.0):
        self.label = name
        self.portion = portion

class Grouping(object):
    """Describe a collection of categorically-similar transaction records."""
    def __init__(self, name, *labels):
        self.name = name
        self.labels = {}
        for label in labels:
            self._add_label(label)
        self.records = []
        self.net = 0.0
        self.income = 0.0
        self.outgo = 0.0
        self.flux = 0.0
        self.last_date = datetime.fromtimestamp(0).date()
        self.first_date = datetime.max.date()
                
    def __contains__(self, label):
        return self.labels.contains(label)

    def _add_label(self, label):
        if isinstance(label, str):
            self.labels[label] = 1.0
        elif isinstance(label, Grouping):
            for k, v in label.labels.items():
                self.labels[k] = max(v, self.labels.get(k, 0.0))
        elif isinstance(label, Partial):
            name = label.label
            portion = label.portion
            if isinstance(name, str):
                self.labels[name] = max(portion, self.labels.get(name, 0.0))
            elif isinstance(name, Grouping):
                for k, v in name.labels.items():
                    self.labels[k] = max(v*portion, self.labels.get(k, 0.0))
            else:
                raise ValueError("Illegal inner label " + label)
        else:
            raise ValueError("Illegal top-level label " + label)

    def include_record(self, row):
        """Add transaction described by Excel Row <row> to these expenses."""
        if row.subject in self.labels:
            try:
                date = row.date
                net = row.net
            except ValueError as e:
                print('Failure to read row {}'.format(row))
                raise
            new_record = Record(date, net)
            self._process_record(new_record)
            return True
        else:
            return False

    def _process_record(self, record):
            self.records.append(record)
            amount = record.amount
            self.net += amount
            self.flux += abs(amount)
            if amount > 0:
                self.income += amount
            else:
                self.outgo += -amount
            date = record.date()
            if date > self.last_date:
                self.last_date = date
            if date < self.first_date:
                self.first_date = date        


class Record(object):
    def __init__(self, date, amount):
        self.date = date
        self.amount = amount


class Row(object):
    def __init__(self, row_num, sheet, config):
        self.row_num = row_num
        self.date = self.read_date(
            sheet=sheet,
            row=row_num,
            col=config.date_col
        )
        self.subject = self._read(
            sheet=sheet,
            row=row_num,
            col=config.subject_col
        )
        self.net = self._read(sheet=sheet, row=row_num, col=config.net_col)
        self.balance = self._read(
            sheet=sheet,
            row=row_num,
            col=config.balance_col
        )

    def __str__(self):
        return 'Row {} ({}): {}'.format(self.row_num, self.date, self.subject)

    def _read(self, sheet, row, col):
        return sheet.cell(row=row, column=self.col_num(col)).value

    def read_date(self, sheet, row, col):
        raw = self._read(sheet=sheet, row=row, col=col)
        if raw is None:
            return None
        else:
            return raw.date

    def col_num(self, raw):
        if isinstance(raw, int):
            return raw
        elif isinstance(raw, str):
            return ord(raw[0]) - ord('A') + 1

    def is_empty(self):
        return (self.subject == "") or (self.subject is None)
