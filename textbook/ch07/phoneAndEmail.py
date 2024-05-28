import pyperclip
import re

def find_phone_and_email():
    phone_regex = re.compile(r'''(
        (\d{3}|\(\d{3}\))?              
        (\s|-|\.)?                      
        (\d{3})                         
        (\s|-|\.)                       
        (\d{4})                         
        (\s*(ext|x|ext.)\s*(\d{2,5}))?  
    )''', re.VERBOSE)

    email_regex = re.compile(r'''(
        [a-zA-Z0-9._%+-]+  
        @                  
        [a-zA-Z0-9.-]+     
        (\.[a-zA-Z]{2,4}) 
    )''', re.VERBOSE)

    text = str(pyperclip.paste())
    matches = []

    matches.extend([
        '-'.join([groups[1], groups[3], groups[5]]) + (f' x{groups[8]}' if groups[8] else '')
        for groups in phone_regex.findall(text)
    ])

    matches.extend([groups[0] for groups in email_regex.findall(text)])

    if matches:
        pyperclip.copy('\n'.join(matches))
        print('クリップボードにコピーしました:')
        print('\n'.join(matches))
    else:
        print('電話番号やメールアドレスは見つかりませんでした。')

find_phone_and_email()
