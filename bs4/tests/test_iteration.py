import unittest
from bs4 import BeautifulSoup
from bs4 import NavigableString

class TestSoupIteration(unittest.TestCase):

    def test_iterate_simple(self):
        html = "<html><body><p>Hello</p></body></html>"
        soup = BeautifulSoup(html, "html.parser")
        nodes = list(soup)
        print("test_iterate_simple:", [n.name if hasattr(n, 'name') else str(n) for n in nodes])
        # Top-level soup has at least one child
        self.assertGreaterEqual(len(nodes), 1)

    def test_iterate_order(self):
        html = "<div><p>A</p><p>B</p></div>"
        soup = BeautifulSoup(html, "html.parser")
        names = [node.name for node in soup]
        print("test_iterate_order:", names)
        # Top-level soup has only one child: <div>
        self.assertEqual(names, ["div"])

    def test_iterate_string(self):
        html = "<p>Test</p>"
        soup = BeautifulSoup(html, "html.parser")
        # Text is inside <p>, not top-level soup
        text_found = any(
            isinstance(node, NavigableString) and node == "Test"
            for node in soup
        )
        print("test_iterate_string: Text found at top level?", text_found)
        self.assertFalse(text_found)  # Should NOT find text at top level

    def test_iterate_deep_tree(self):
        html = "<a><b><c>X</c></b></a>"
        soup = BeautifulSoup(html, "html.parser")
        nodes_str = [str(n) for n in soup]
        combined = "".join(nodes_str)
        print("test_iterate_deep_tree:", combined)
        # Combined string should include the whole <a> tree
        self.assertIn("<a><b><c>X</c></b></a>", combined)

    def test_iterate_empty(self):
        soup = BeautifulSoup("", "html.parser")
        nodes = list(soup)
        print("test_iterate_empty:", nodes)
        # Empty soup has no children
        self.assertEqual(nodes, [])

if __name__ == "__main__":
    unittest.main()


