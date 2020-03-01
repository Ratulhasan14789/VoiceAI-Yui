from openpyxl import load_workbook, Workbook
pdataxl= load_workbook(filename='Yui_data/RAM/pdatas.xlsx')
pdata= pdataxl.active
print(pdata['A1'].value)