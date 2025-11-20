import sys
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
sys.path.insert(0, project_root)

from bs4 import BeautifulSoup
from bs4.soup_replacer import SoupReplacer


def main():
    if len(sys.argv) < 2:
        print("Usage: python task7.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    if not os.path.exists(input_file):
        print(f"Error: File '{input_file}' not found.")
        sys.exit(1)

    def add_class_test(tag):
        if tag.name == "p":
            tag.attrs["class"] = ["test"]

    replacer = SoupReplacer(xformer=add_class_test)

    with open(input_file, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser", replacer=replacer)

    output_file = os.path.join(os.path.dirname(__file__), "output_p_class_test.html")
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(soup.prettify())

    print(f"Successfully added class='test' to all <p> tags.")
    print(f"Output saved to: {output_file}")

if __name__ == "__main__":
    main()

