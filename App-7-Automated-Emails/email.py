import yagmail
import pandas as pd
import numpy as np
# email = yagmail.SMTP(user="aditya4855@gmail.com", password="")
# email.send(to="", subject="", contents="", attachments="")



# Replace 'your_excel_file.xlsx' with the path to your Excel file
file_path = 'D:\\PYTHON\\OOPS\\files\\App-7-Automated-Emails\\people.xlsx'

# Read the Excel file into a pandas DataFrame
df = pd.read_excel(file_path)

# Now you can work with the DataFrame 'df'
# For example, you can print the first few rows of the DataFrame
print(df.head())


