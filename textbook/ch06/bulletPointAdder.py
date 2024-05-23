import pyperclip

try:
    text = pyperclip.paste()

    lines = text.split('\n')
    for i in range(len(lines)):
        lines[i] = '* ' + lines[i]
    
    text = '\n'.join(lines)
    pyperclip.copy(text)

    print("Text successfully copied with bullet points.")
except pyperclip.PyperclipException as e:
    print("An error occurred with Pyperclip:", e)
