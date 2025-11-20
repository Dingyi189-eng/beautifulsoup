import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from bs4 import BeautifulSoup, SoupStrainer
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python task2.py <input_file>")
        return

    input_file = sys.argv[1]

    with open(input_file, 'r', encoding='utf-8') as f:
        strainer = SoupStrainer('a')
        soup = BeautifulSoup(f, 'lxml', parse_only=strainer)

    for link in soup:
        print(link)

if __name__ == "__main__":
    main()
