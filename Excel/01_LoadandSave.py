from openpyxl import Workbook
from openpyxl.reader.excel import load_workbook

wb = load_workbook('balances.xlsx')
#wb.save('document_template.xltx', as_template=True)
wb.save('balances01.xlsx')
