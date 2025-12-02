import sys
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
sys.path.insert(0, project_root)

from bs4 import BeautifulSoup, NavigableString, Doctype

filename = sys.argv[1]

with open(filename, "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")

def print_node(soup):
    for node in soup:  # 调用 node.__iter__()，迭代所有子节点
        if isinstance(node, NavigableString):
            text = node.strip()
            if text:
                print(f"Text: {text}")
        else:
            print(f"Tag: <{node.name}>")

print_node(soup)


