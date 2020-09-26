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
    'fee for ATM withdrawal',
    # Use a Partial instance when you want only some of the associated expenses
    # to count toward the collection.
    Partial('Credit card paid online, including late fees', 0.1),
    'Tax preparer',
    'Company travel reimburse',
    'Initial deposit on house',
    'Check printing charge',
    'Check Reorder',
)
CAR = Grouping(
    'car purchase & maintenance',
    'Car downpayment',
    'Car payment',
    'Mechanic',
    'Auto insurance premium',
    'Car rental',
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
    'rent - 4321 University Blvd',
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
MARRIAGE = Grouping(
    'my marriage',
    'Wedding Bubbles',
    'wedding reception',
    "Dress alterations",
    'wedding gift',
    'KoGiBow - Bakery / wedding cake',
    'Loan from Dad & Darlene to buy Steve out of house',
    'Marta Licona (11720 Viers Mill Road - 1/2 tree removal)',
    'Michele Zavos Law Group, PLLC',
    'Jamie Lennon - test tube labels',
    'Jeffrey W. Vinson / 50 % House Appraisal for Divorce Negotiations',
    'RRUUC - Full payment for wedding ceremony reservation',
    'Repay loan from Dad',
    'River Road Unitarian Church',
    'Ruth Evers (earrings & wedding bands)',
    "Uncle Julio's / Wedding Caterer",
    'Wedding Reception Hall / BCCRS - second check',
    'Williams - Sonoma (wedding registry close-out)',
    'Zavos Juncker Law Group; divorce',
    'Zavos Juncker Law Group; trust fund for divorce settlement',
    'Zavos-Juncker Law Group',
    'Zavos-Juncker Law Group; refund for excess retainer',
)
MEDICAL = Grouping(
    'medical',
    'Advanced Medical Care / GP Dr. Ajmal',
    'Adventist Health Care (ER 8/16)',
    'Andrew Sorkin / dentist checkup',
    'Andrew Sorkin / dentist copay',
    'Andrew Sorkin / fillings',
    'Bank of America - Escrow Interest',
    'Bank of America - Mortgage',
    'Bank of America - Mortgage Application fee',
    'Bank of America / Mortgage',
    'Bank of America Escrow Reimburse',
    'Bank of America – Mortgage',
    'Community Radiology Associates / throat X-rays',
    'Dentist (Dr. Andrew Sorkin)',
    'Dr. Ajmal',
    'Dr. Andrew Sorkin (dentist)',
    'Dr. Michael Dempsey (Endocrinologist)',
    'ER (Medical Emergency Professionals)',
    'Endocrinologist (Michael Dempsey)',
    'Endocrinologist (Michael Dempsey) - Records Request',
    'Friendship Heights Chiropractic',
    'Friendship Heights Chiropractic (10 sessions)',
    'Friendship Heights Chiropractic (15 sessions)',
    'Friendship Heights Chiropractor',
    'Grace Care, LLC (crutches)',
    'Groover, Christie & Merritt (X-rays)',
    'HSA Autodebit',
    'Initial deposit on house: 11725 College View Drive',
    'LabCorp',
    'LabCorp (bloodwork)',
    'LabCorp (stool sample)',
    'LabCorp / STD tests',
    'LabCorp / Vitamin D test',
    'LabCorp / multiple tests',
    'Massage / Mike Delvecchio',
    "Med Star Physician's Group (oral inspection)",
    'MedStar Physicians (Gum Inspection)',
    'MedStar Washington Hospital Center',
    'Michael Dempsey',
    'Michael Dempsey (endocrinologist)',
    'Mike Delvecchio',
    'Mike Delvecchio (missed massage)',
    'Mike Delvecchio (massage)',
    'NRH Medical Rehabilitation (ankle PT)',
    'Physician Assoc. (Aug. 17 visit)',
    'Physician Associates (orthopedist 9/21)',
    'Physicians Associates',
    'Physicians Associates / food caught in throat',
    'Refund (?) from Friendship Heights Chiropractor',
    'Sanaa Sharnoubi counseling', 
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
    'Paid Pepco over phone, including service charge',
    'Pepco',
    'Pepco - College View Drive',
    'Pepco Rebate',
)
PROFESSIONAL = Grouping(
    'professional',
    'travel reimburse',
    'convention reimburse',
    'Corporate Citi Card',
    'professional development class',
)
SAVINGS = Grouping(
    'savings',
    'Auto Transfer to HSA',
    'Auto Transfer to Mutual Fund',
    'Auto Xfer to savings',
    'Manual Transfer to Money Market Savings',
)
TAX = Grouping(
    'tax',
    'Clerk, United States Tax Court',
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
    MARRIAGE,
    PROFESSIONAL
)
LOW_LIFE = Grouping(
    'low life',
    # Other groupings can also be used in a Partial instance.
    Partial(CREDIT_CARD, 0.5),
    Partial(MIXED, 0.5),
    REQUIRED
)
HIGH_LIFE = Grouping('high life', CREDIT_CARD, OPTIONAL, MIXED, REQUIRED)


# Leave KNOWN_GROUPS here, but add / remove components as necessary.
KNOWN_GROUPS = [
    BANKING, CAR, CHARITY, CREDIT_CARD, EDUCATION, GAS, HIGH_LIFE, HOUSING,
    INCOME, LOANS, LOW_LIFE,
    OPTIONAL, MAINTENANCE, MARRIAGE, MEDICAL,
    MIXED, POWER, PROFESSIONAL, REQUIRED, SAVINGS, TAX,
    TELECOM, WATER, UTILITY
]