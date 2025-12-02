import sys
import os

# 指向 bs4 的父目录
local_bs4_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, local_bs4_path)

from bs4 import BeautifulSoup, SoupStrainer

import bs4
print("Loaded bs4 from:", bs4.__file__)

def main():
    if len(sys.argv) < 2:
        print("Usage: python task2.py <input_file>")
        return

    input_file = sys.argv[1]

    with open(input_file, 'r', encoding='utf-8') as f:
        strainer = SoupStrainer('a')
        soup = BeautifulSoup(f, 'lxml', parse_only=strainer)

    for tag in soup.find_all(True):
        print(tag)

if __name__ == "__main__":
    main()
