import sys
import os
import unittest

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
sys.path.insert(0, project_root)

from bs4 import BeautifulSoup
from bs4 import NavigableString, Doctype
from bs4.element import Tag

class TestIteration(unittest.TestCase):

    def test_iterate_simple(self):
        html = "<html><body><p>Hello</p></body></html>"
        soup = BeautifulSoup(html, "html.parser")
        nodes = list(soup)
        node_names = []
        for n in nodes:
            if isinstance(n, Tag):
                node_names.append(n.name)
            elif isinstance(n, NavigableString):
                node_names.append(str(n))
            elif hasattr(n, "name"):
                node_names.append(n.name)
            else:
                node_names.append(str(n))
        print("test_iterate_simple:", node_names)
        self.assertTrue(any(isinstance(n, Tag) and n.name == "html" for n in nodes))

    def test_iterate_text_nodes(self):
        html = "<html><body><p>Hello</p></body></html>"
        soup = BeautifulSoup(html, "html.parser")
        texts = [str(n) for n in soup if isinstance(n, NavigableString) and n.strip()]
        print("test_iterate_text_nodes", texts)
        self.assertIn("Hello", texts)

    def test_iterate_doctype(self):
        html = "<!DOCTYPE html><p>Hi</p>"
        soup = BeautifulSoup(html, "html.parser")
        doctypes = [n for n in soup if isinstance(n, Doctype)]
        print("test_iterate_doctype:", doctypes)
        self.assertTrue(any(isinstance(n, Doctype) for n in doctypes))

    def test_iterate_deep_tree(self):
        html = "<div><p>A</p><p>B</p></div>"
        soup = BeautifulSoup(html, "html.parser")
        names = [n.name for n in soup if isinstance(n, Tag)]
        print("test_iterate_deep_tree:", names)
        self.assertIn("div", names)
        self.assertIn("p", names)

    def test_iterate_empty(self):
        soup = BeautifulSoup("", "html.parser")
        nodes = list(soup)
        self.assertTrue(len(nodes) == 0 or (len(nodes) == 1 and nodes[0].name == '[document]'))

if __name__ == "__main__":
    unittest.main()
