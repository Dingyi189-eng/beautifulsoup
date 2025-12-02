import unittest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from bs4 import BeautifulSoup
from bs4.soup_replacer import SoupReplacer

class TestSoupReplacer(unittest.TestCase):

    def test_replace_b_with_blockquote(self):
        html = "<p>Hello <b>world</b></p>"
        replacer = SoupReplacer("b", "blockquote")
        soup = BeautifulSoup(html, "html.parser", replacer=replacer)
        self.assertIn("<blockquote>world</blockquote>", str(soup))

    def test_no_change_for_other_tags(self):
        html = "<p>Hello <i>world</i></p>"
        replacer = SoupReplacer("b", "blockquote")
        soup = BeautifulSoup(html, "html.parser", replacer=replacer)
        self.assertIn("<i>world</i>", str(soup))

if __name__ == "__main__":
    unittest.main()
