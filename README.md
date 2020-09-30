This package is a tool I used to help me with my household budgeting.

# ABOUT

For several years, I've maintained an Excel file showing the transactions in my checking and savings accounts. I built this tool as a way to mine that data for information about my personal expenses and income.

While it shows every check or money transfer I've had over the years, it does not group those items on its own. In addition, it has single line items for expenses that could be considered in under multiple headings. The item names are also _ad_ _hoc_, and include items I didn't anticipate when I first created the file.

This "Budgeter" tool creates multiple groups of expenses & income based on the subject / name of each transaction. It then calculates the "income," "outgo," "net" (income - outgo) and "flux" (income + outgo) associated with each group. Each group is shown with its range of dates. The income, outgo, net and flux numbers for each are presented both as aggregate amounts and as rates (e.g. dollars per year).

## Features

* Groupings may be nested. This lets me define aggregates across multiple categories of expenses: For example, I have a "utility" group which includes "water", "power", "communication" and "gas."

* Individual line items may count toward multiple groups: "Property tax" might be listed under both "housing" and "tax," for example.

* Particular line items may count as being only partially in a group. If I assume about half my credit card expenses (which aren't broken down further) are actually optional, I can thus make a "tight budget" estimate which assumes my credit card expenses are cut in half while other groupings (medical, housing, utilities) are kept at full.

# Dependencies

Python 3.8.0
openpyxl==3.0.2

# USAGE

* Build an Excel file which resembles "sample_excel.xlsx."
* Rename "sample_config.py" and modify its contents to reflect your desired groupings, plus some details of your Excel file's set up.
* Run `python Budgeter.py` from the command line.

# TODO

* Add an output chart / charts using plotly
* Distinguish between last-year and lifetime records. Currently all statistics reference lifetime behavior.
* Reconcile sample_finances.xlsx with sample_config.py
* Produce pandas DataFrame version of output.
* Add unit tests.