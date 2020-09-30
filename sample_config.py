'''This file describes how your transactions should be read & categorized.'''
from budgeter.classes import Grouping, Partial

# Describe the structure of the Excel file recording 
START_ROW = 5
SHEET_NAME = "Checking"
DATE_COL = "B"
SUBJECT_COL = "C"
NET_COL = "F"
BALANCE_COL = "G"

# Describe the location and source path for the Excel file
finance_dir = './'
FILE_PATH = finance_dir + 'sample_finances.xlsx'

# Describe each category of similar records
BANKING = Grouping(
    'banking fees & cash flow', # First string in each Grouping is its name.
    # All subsequent strings, Partials, and Groupings are members.
    # Use a simple string to match all entries with that subject.
    # Note that these strings ARE case-sensitive.
    'fee for ATM withdrawal',
    'ATM w/drawal',
    # Use a Partial instance when you want only some of the associated expenses
    # to count toward the collection.
    Partial('Credit card paid online, including late fees', 0.1),
    'Tax preparer',
    'Company travel reimburse',
    'Initial deposit on house',
    'Check printing charge',
    'Check Reorder',
)
# This format of Grouping declaration also works, and may be more readable
CAR = Grouping(
    'car purchase & maintenance',
    *[
        'Car downpayment',
        'Car payment',
        'Mechanic',
        'Auto insurance premium',
        'Car rental',
    ]
)
CHARITY = Grouping(
    'charity & gifts',
    'Amnesty International',
    'Audobon Naturalist Society / May Day',
    'Charity Silent Auction',
    'Girl Scout Cookies',
    "repair ex's car",
    'Church offering',
)
CREDIT_CARD = Grouping(
    'credit card',
    'Visa Card',
    'American Express',
    'MasterCard',
)
EDUCATION = Grouping(
    'education',
    'tuition',
    'University paycheck',
)
GAS = Grouping(
    'gas',
    'Gas Bill',
)
HOUSING = Grouping(
    'housing rent & mortgage',
    'Mortgage',
    'Escrow Interest',
    'House downpayment',
    'rent - University Blvd',
    "Homeowner's Insurance",
    'Rent',
    'rent',
    'partial Rent',
)
INCOME = Grouping(
    'salary & other forms of direct income',
    'paycheck',
    'direct department',
    'income',
    'annual bonus',
    'Interest',
)
LOANS = Grouping(
    'loans',
    'car payment',
    'refund of ATM withdrawal fee',
    'APS double payment reimburse',
    'ATM fee rebate',
    'Mortgage',
    "Homeowner's Insurance",
    'Mortgage Escrow Refund',
    'Transfer to PayPal',
)
MAINTENANCE = Grouping(
    'home maintenance & improvement',
    'washer repair',
    'replace windows',
    'lawn mower',
    'siding repair',
    'blinds',
    'Plumber',
    'Roofing',
)
MEDICAL = Grouping(
    'medical',
    'Advanced Medical Care / GP Dr. A',
    'Adventist Health Care',
    'Dentist copay',
    'dentist - fillings',
    'Escrow Interest',
    'Mortgage',
    'Mortgage Application fee',
    'Dentist',
    'Doctor A',
    'Dr. D',
    'ER',
    'Chiropractor',
    'X-rays',
    'HSA Autodebit',
    'Initial deposit on house',
    'LabCorp',
    'Massage',
    'Physical Therapy',
)
MIXED = Grouping(
    'mixed usage',
    'ATM fee',
    'ATM fees',
    'ATM withdrawal',
    # Use a member which is a Grouping to get nested categories
    CREDIT_CARD
)
POWER = Grouping(
    'power',
    'Entergy',
)
PROFESSIONAL = Grouping(
    'professional',
    'travel reimburse',
    'convention reimburse',
    'Corporate Card',
    'professional development class',
)
SAVINGS = Grouping(
    'savings',
    'Auto Xfer to savings',
)
TAX = Grouping(
    'tax',
    'Estimated Tax',
    'Fed. Estimated Tax',
    'Federal Estimated Tax',
    'Federal Income Tax',
    'Federal Tax',
    'Federal Tax Refund',
    'Property Tax + Interest',
    'State Income Tax',
    'United States Treasury',
)
TELECOM = Grouping(
    'communication',
    'Stamps',
    'Verizon',
    'Cricket Wireless',
)
WATER = Grouping(
    'water',
    'American Water works',
)
UTILITY = Grouping('utility', GAS, TELECOM, WATER, POWER)

REQUIRED = Grouping('required', BANKING, HOUSING, MAINTENANCE, UTILITY, TAX)
OPTIONAL = Grouping(
    'optional',
    'conference wear',
    'Anime',
    'Passport',
    'Chiropractor',
    'Game Stop',
    "ball game",
    'new computer',
    'guest bed',
    'dresser',
    CHARITY,
    EDUCATION,
    PROFESSIONAL
)

# I use this LOW_LIFE to estimate what a tight budget looks like.
LOW_LIFE = Grouping(
    'low life',
    # Other groupings can also be used in a Partial instance.
    Partial(CREDIT_CARD, 0.5),
    Partial(MIXED, 0.5),
    REQUIRED
)

# I use this HIGH_LIFE Grouping to estimate a comfortable budget.
HIGH_LIFE = Grouping('high life', CREDIT_CARD, OPTIONAL, MIXED, REQUIRED)


# Leave KNOWN_GROUPS here, but add / remove components as necessary.
KNOWN_GROUPS = [
    BANKING, CAR, CHARITY, CREDIT_CARD, EDUCATION, GAS, HIGH_LIFE, HOUSING,
    INCOME, LOANS, LOW_LIFE,
    OPTIONAL, MAINTENANCE, MEDICAL,
    MIXED, POWER, PROFESSIONAL, REQUIRED, SAVINGS, TAX,
    TELECOM, WATER, UTILITY
]
