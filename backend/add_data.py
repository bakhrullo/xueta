import pandas as pd

excel_data = pd.read_excel('Kara-Tashkent.xlsx')
# Read the values of the file in the dataframe
data = pd.DataFrame(excel_data, columns=[
                    'Тел'])
# Print the content
print("The content of the file is:\n", data)