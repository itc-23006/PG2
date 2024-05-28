import re

def custom_strip(text):
    return re.sub(r'^\s+|\s+$', '', text)

print(f"'{custom_strip('   Hello, World!   ')}'")
print(f"'{custom_strip('   Leading space removed')} '")
print(f"'{custom_strip('Trailing space removed   ')}'")
print(f"'{custom_strip('   No spaces to strip')} '")
