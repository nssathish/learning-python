import openpyxl
wb = openpyxl.load_workbook("Book1.xlsx")
sheet = wb['Sheet1']
cell = sheet['a2']
cell = sheet.cell(1,1)
print(cell.internal_value)