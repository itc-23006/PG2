import pyperclip
import re

def find_strong_passwords():
    password_regex = re.compile(r'(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%^&*]).{8,}')
    text = str(pyperclip.paste())
    matches = password_regex.findall(text)
    
    if matches:
        pyperclip.copy('\n'.join(matches))
        print('クリップボードにコピーしました:')
        print('\n'.join(matches))
    else:
        print('強いパスワードは見つかりませんでした。')

find_strong_passwords()
