import sys, os, openpyxl

if not len(sys.argv) == 2:
    print('Usage: python txt2excel.py Directory')
    print('  One argument must required.')
    print('example: python txt2excel.py dir_name')
    sys.exit()
dir_path = sys.argv[1]
try:
    os.chdir(dir_path)
except FileNotFoundError:
    print(dir_path + ' is not exist.')
    sys.exit()
except NotADirectoryError:
    print(dir_path + ' is not a directory.')
    sys.exit()

wb = openpyxl.Workbook()
ws = wb.active

dir_files = os.listdir('.')
ext = ('txt', 'text')
files = []
for dir_file in dir_files:
    if dir_file.split('.')[-1] in ext:
        files.append(dir_file)
files.sort()

for col, file in zip(range(1, len(files) + 1), files):
    f = open(file)
    lines = f.readlines()
    for row, line in zip(range(1, len(lines) + 1), lines):
        cell = ws.cell(row=row, column=col)
        cell.value = line.rstrip()  

wb.save('txt2excel_result.xlsx')
