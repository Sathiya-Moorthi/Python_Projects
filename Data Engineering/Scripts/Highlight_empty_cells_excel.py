import pandas as pd
import re
from runtime import runtime


# Function to highlight empty cells and long email cells
def highlight_cells(val, col_name, email_columns):
    if pd.isnull(val) or val == '':
        return 'background-color: yellow'
    elif col_name in email_columns and isinstance(val, str) and len(val) > 49:
        return 'background-color: red'
    else:
        return ''

# Function to apply the highlighting to each cell in the DataFrame
def apply_highlighting(sheet, email_columns):
    styled_sheet = sheet.style.apply(lambda x: [highlight_cells(x.iloc[i], x.index[i], email_columns) for i in range(len(x))], axis=1)
    return styled_sheet

# Function to check email address columns for character limit
def check_email_columns(sheet):
    email_regex = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
    email_columns = [col for col in sheet.columns if sheet[col].apply(lambda x: isinstance(x, str) and bool(email_regex.match(x))).any()]

    for column in email_columns:
        long_emails = sheet[column][sheet[column].str.len() > 49]
        if not long_emails.empty:
            print(f"Warning: Email addresses in column '{column}' exceed 49 characters at rows: {long_emails.index.tolist()}")

    return email_columns

# Function to process each sheet in the Excel file
def process_excel_file(excel_file):
    xls = pd.ExcelFile(excel_file)
    with pd.ExcelWriter("processed_" + excel_file, engine='xlsxwriter') as writer:
        for sheet_name in xls.sheet_names:
            sheet = pd.read_excel(xls, sheet_name=sheet_name)
            email_columns = check_email_columns(sheet)
            styled_sheet = apply_highlighting(sheet, email_columns)
            styled_sheet.to_excel(writer, sheet_name=sheet_name, index=False)
            print(f"Sheet '{sheet_name}' processed and saved to the output file")

# Example usage:
process_excel_file("Financial Sample.xlsx")

runtime()

# the below link contains all the errors that I have faced while running this program and other convo reg Highlight_empty_cells_excel, must visit to learn more

"""------------------------------------ chatgpt : https://chatgpt.com/share/419e0ba2-7e4a-4de7-8f1d-dcefbcbc2a62 ------------------------------------------ """



