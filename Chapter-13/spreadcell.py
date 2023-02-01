import  openpyxl


workbook = openpyxl.load_workbook()
workbook_copy = openpyxl.Workbook()
sheet = workbook.active
sheet_copy = workbook_copy.active
for columns in range(1, sheet.max_column + 1):
    for rows in range(1, sheet.max_row + 1):
            sheet_copy.cell(row = columns, column = rows).value = sheet.cell(row=rows, column=columns).value
    workbook_copy.save()
    
