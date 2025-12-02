import unittest
import sys
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
sys.path.insert(0, project_root)

from bs4 import BeautifulSoup
from bs4.soup_replacer import SoupReplacer


class TestSoupReplacer(unittest.TestCase):

    # Test name_xformer modifying tag name
    def test_name_xformer(self):
        html = "<b>bold</b>"
        replacer = SoupReplacer(name_xformer=lambda tag: "blockquote" if tag.name == "b" else tag.name)
        soup = BeautifulSoup(html, "html.parser", replacer=replacer)
        self.assertIsNotNone(soup.find("blockquote"))

    # Test attrs_xformer modifying attributes
    def test_attrs_xformer(self):
        html = '<p class="old">text</p>'
        def change_attrs(tag):
            return {"class": ["new"]}
        replacer = SoupReplacer(attrs_xformer=change_attrs)
        soup = BeautifulSoup(html, "html.parser", replacer=replacer)
        self.assertEqual(soup.find("p")["class"], ["new"])

    # Test xformer
    def test_xformer_side_effect(self):
        html = "<div></div>"
        def add_attr(tag):
            tag["data-test"] = "yes"
        replacer = SoupReplacer(xformer=add_attr)
        soup = BeautifulSoup(html, "html.parser", replacer=replacer)
        self.assertEqual(soup.find("div")["data-test"], "yes")

    # Test combined transformers
    def test_combined_transformers(self):
        html = '<p class="old">Hello</p>'
        def change_attrs(tag):
            return {"class": ["test"]}
        replacer = SoupReplacer(
            name_xformer=lambda tag: "span" if tag.name == "p" else tag.name,
            attrs_xformer=change_attrs,
            xformer=lambda tag: tag.__setitem__("data-added", "yes")
        )
        soup = BeautifulSoup(html, "html.parser", replacer=replacer)
        tag = soup.find("span")
        self.assertIsNotNone(tag)
        self.assertEqual(tag["class"], ["test"])
        self.assertEqual(tag["data-added"], "yes")

    # Test nested tags
    def test_nested_tags(self):
        html = "<div><p>text</p></div>"
        replacer = SoupReplacer(name_xformer=lambda tag: "section" if tag.name=="p" else tag.name)
        soup = BeautifulSoup(html, "html.parser", replacer=replacer)
        tag = soup.find("section")
        self.assertIsNotNone(tag)
        self.assertEqual(tag.text, "text")

    # Test unaffected tags
    def test_empty_or_nonexistent_tags(self):
        html = "<div></div>"
        replacer = SoupReplacer(
            name_xformer=lambda tag: "span" if tag.name=="p" else tag.name,
            attrs_xformer=lambda tag: {"class": ["new"]} if tag.name=="p" else tag.attrs
        )
        soup = BeautifulSoup(html, "html.parser", replacer=replacer)
        tag = soup.find("div")
        self.assertIsNotNone(tag)
        self.assertNotIn("class", tag.attrs)


if __name__ == "__main__":
    unittest.main()

