def is_phone_number(text):
    return len(text) == 12 and text[:3].isdigit() and text[3] == '-' and text[4:7].isdigit() and text[7] == '-' and text[8:].isdigit()

print('415-555-4242 は電話番号:')
print(is_phone_number('415-555-4242'))
print('Moshi moshi は電話番号:')
print(is_phone_number('Moshi moshi'))
