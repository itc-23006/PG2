import pyperclip
import re

def find_dates():
    date_regex = re.compile(r'(\b\d{4}[-/]\d{1,2}[-/]\d{1,2}\b|\b\d{1,2}[-/]\d{1,2}[-/]\d{4}\b|\b\d{1,2}\s\w+\s\d{4}\b)', re.VERBOSE)
    text = str(pyperclip.paste())
    matches = date_regex.findall(text)

    if matches:
        pyperclip.copy('\n'.join(matches))
        print('クリップボードにコピーしました:')
        print('\n'.join(matches))
    else:
        print('日付は見つかりませんでした。')

find_dates()
