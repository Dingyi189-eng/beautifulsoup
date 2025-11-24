import sys
from bs4 import BeautifulSoup, NavigableString, Doctype

filename = sys.argv[1]

with open(filename, "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")

def traverse_and_print(soup, level=0):
    indent = "  " * level
    for node in soup:
        if isinstance(node, Doctype):
            print(f"{indent}(Doctype: {node})")
        elif isinstance(node, NavigableString):
            text = str(node).strip()
            if text:
                print(f"{indent}(String: '{text}')")
        elif hasattr(node, "name"):
            print(f"{indent}<Tag name='{node.name}'>")
            traverse_and_print(node, level + 1)

traverse_and_print(soup)

