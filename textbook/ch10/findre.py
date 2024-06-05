import os, re

def find_missing_numbers(directory, prefix):
    files = os.listdir(directory)
    
    pattern = re.compile(r'^' + re.escape(prefix) + r'(\d+)\.txt$')
    numbers = []

    for file in files:
        match = pattern.match(file)
        if match:
            numbers.append(int(match.group(1)))

    numbers.sort()
    
    missing_numbers = []
    for i in range(1, numbers[-1]):
        if i not in numbers:
            missing_numbers.append(i)
    
    return missing_numbers

directory = '/path/to/your/directory'
prefix = 'spam'
missing_numbers = find_missing_numbers(directory, prefix)
print(f'Missing numbers: {missing_numbers}')
