import sys, os, openpyxl

if not len(sys.argv) == 2:
    print('Usage: python excel2txt.py file_name.xlsx')
    print('  One argument must required.')
    print('example: python excel2txt.py example.xlsx')
    sys.exit()
file_path = sys.argv[1]

if not os.path.isfile(file_path):
    print(file_path)
    print(file_path + ' is not exist.')
    sys.exit()
ext = 'xlsx'
if ext in file_path.rsplit('.')[-1]:

    try:
        wb = openpyxl.load_workbook(file_path)
        ws = wb.active
        ws_title = ws.title
    except AttributeError:
        print('Sheet dose not exist in "' + file_path + '".')
        sys.exit()

    dir_name = 'excel2txt_' + ws_title
    try:
        os.mkdir(dir_name)
    except FileExistsError:
        print('Directory of ' + dir_name + ' exists.')
        sys.exit()
    os.chdir(dir_name)

    for col in range(ws.max_column):
        file_name = ws_title + '_' + str(col) + '.txt'
        file = open(file_name, mode='w', encoding='utf-8')
        for cell in list(ws.columns)[col]:
            file.write(str(cell.value) + '\n')
        file.close()

else:
    print(file_path + ' is not excel file.')
    sys.exit()

