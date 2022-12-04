import  openpyxl

book = openpyxl.load_workbook("")

sheet = book.active

cell = sheet.cell(row=3,column=2)

print(cell.value)
