import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from bs4 import BeautifulSoup, SoupStrainer
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python task3.py <input_file>")
        return

    input_file = sys.argv[1]

    with open(input_file, 'r', encoding='utf-8') as f:
        strainer = SoupStrainer(True)
        soup = BeautifulSoup(f, 'lxml', parse_only=strainer)

    tags = {tag.name for tag in soup.find_all(True)}
    print("All tags in document:", tags)

if __name__ == "__main__":
    main()
