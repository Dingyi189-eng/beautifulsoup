
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from bs4 import BeautifulSoup
from bs4.soup_replacer import SoupReplacer


def main():
    if len(sys.argv) < 2:
        print("Usage: python task6.py <input_file>")
        return

    replacer = SoupReplacer("b", "blockquote")

    with open(sys.argv[1], "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser", replacer=replacer)

    with open("output_blockquote.html", "w", encoding="utf-8") as f:
        f.write(soup.prettify())

    print("Replaced all <b> tags with <blockquote>.")

if __name__ == "__main__":
    main()
