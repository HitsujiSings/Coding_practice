from openpyxl import Workbook
wb = Workbook()

ws = wb.active
ws1 = wb.create_sheet()
ws1.title = "New Title"

wb.save('balances.xlsx')
