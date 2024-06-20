import sys, openpyxl

src = sys.argv[1]
if not len(sys.argv) == 2:
print('Usage: python transposeExcelMatrix.py filename.xlsx')
print(' One argument must required.')
print('example: python blankRowInserter.py example.xlsx')
sys.exit()
try:
wb = openpyxl.load_workbook(src)
except FileNotFoundError:
print('Filename "' + src + '" is not exist.')
sys.exit()
ws = wb.active

new_wb = openpyxl.Workbook()
new_ws = new_wb.active
new_ws.title = ws.title

max_row = ws.max_row
max_col = ws.max_column

for row in range(1, max_row + 1):
for col in range(1, max_col + 1):
new_ws.cell(row=col, column=row).value = ws.cell(row=row, column=col).value

new_wb.save('transpose_' + src)
