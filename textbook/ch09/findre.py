import os
import re

def search_in_files(directory, regex_pattern):
    pattern = re.compile(regex_pattern)
    
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".txt"):
                file_path = os.path.join(root, file)
                
                with open(file_path, 'r', encoding='utf-8') as f:
                    for line_number, line in enumerate(f, start=1):
                        if pattern.search(line):
                            print(f"File: {file_path}, Line {line_number}: {line.strip()}")

directory = input("検索したいディレクトリのパスを入力してください: ")
regex_pattern = input("検索したい正規表現パターンを入力してください: ")

search_in_files(directory, regex_pattern)
