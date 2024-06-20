import sys, openpyxl

args = sys.argv[1:4]
if not len(args) == 3:
    print('Usage: python blankRowInserter.py int int filename.xlsx')
    print('Three arguments are required.')
    print('example: python blankRowInserter.py 3 5 example.xlsx')
    sys.exit()

n = int(args[0])  
m = int(args[1])  
file_name = args[2] 


if n <= 0:
    print('The First argument must input 1 or more.')
    sys.exit()

if m < 0:
    print('The Second argument must input a 0 or more.')
    sys.exit()

try:
    wb = openpyxl.load_workbook(args[2])
except FileNotFoundError:
    print('Filename "' + args[2] + '" is not exist.')
    sys.exit()
sheet = wb.active
sheet_title = sheet.title
max_row = sheet.max_row
max_column = sheet.max_column


result_wb = openpyxl.Workbook()
result_sheet = result_wb.active
result_sheet.title = sheet_title

data = []
for i in range(max_row):
    data.append(list(sheet.rows)[i])

row = 1
column = 1
for data_row in data:
    if row == n:
        row = row + m
    for cell in data_row:
        result_sheet.cell(row=row, column=column).value = cell.value
        column += 1  
    row += 1  
    column = 1  

result_wb.save('blank_row_' + file_name)
