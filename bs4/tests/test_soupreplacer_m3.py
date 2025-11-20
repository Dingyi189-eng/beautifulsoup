import sys
import os
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
sys.path.insert(0, project_root)

from bs4 import BeautifulSoup
from bs4.soup_replacer import SoupReplacer

# Test that name_xformer correctly changes the tag name during parsing.
def test_name_xformer():
    html = "<b>bold</b>"
    replacer = SoupReplacer(name_xformer=lambda tag: "blockquote" if tag.name=="b" else tag.name)
    soup = BeautifulSoup(html, "html.parser", replacer=replacer)
    assert soup.find("blockquote") is not None
    print("test_name_xformer passed")

# Test that attrs_xformer correctly modifies tag attributes.
def test_attrs_xformer():
    html = '<p class="old">text</p>'
    def change_attrs(tag):
        return {"class": ["new"]}
    replacer = SoupReplacer(attrs_xformer=change_attrs)
    soup = BeautifulSoup(html, "html.parser", replacer=replacer)
    assert soup.find("p")["class"] == ["new"]
    print("test_attrs_xformer passed")

# Test that xformer can perform side-effect changes on a tag.
def test_xformer_side_effect():
    html = "<div></div>"
    def add_attr(tag):
        tag["data-test"] = "yes"
    replacer = SoupReplacer(xformer=add_attr)
    soup = BeautifulSoup(html, "html.parser", replacer=replacer)
    assert soup.find("div")["data-test"] == "yes"
    print("test_xformer_side_effect passed")

# Test that multiple transformers (name_xformer, attrs_xformer, xformer) work together.
def test_combined_transformers():
    html = '<p class="old">Hello</p>'
    def change_attrs(tag):
        return {"class": ["test"]}
    replacer = SoupReplacer(
        name_xformer=lambda tag: "span" if tag.name=="p" else tag.name,
        attrs_xformer=change_attrs,
        xformer=lambda tag: tag.__setitem__("data-added", "yes")
    )
    soup = BeautifulSoup(html, "html.parser", replacer=replacer)
    tag = soup.find("span")
    assert tag is not None
    assert tag["class"] == ["test"]
    assert tag["data-added"] == "yes"
    print("test_combined_transformers passed")

# Test that transformers correctly handle nested tags.
def test_nested_tags():
    html = "<div><p>text</p></div>"
    replacer = SoupReplacer(name_xformer=lambda tag: "section" if tag.name=="p" else tag.name)
    soup = BeautifulSoup(html, "html.parser", replacer=replacer)
    tag = soup.find("section")
    assert tag is not None
    assert tag.text == "text"
    print("test_nested_tags passed")

# Test that transformers do not affect tags that are not targeted.
def test_empty_or_nonexistent_tags():
    html = "<div></div>"
    replacer = SoupReplacer(
        name_xformer=lambda tag: "span" if tag.name=="p" else tag.name,
        attrs_xformer=lambda tag: {"class": ["new"]} if tag.name=="p" else tag.attrs
    )
    soup = BeautifulSoup(html, "html.parser", replacer=replacer)
    tag = soup.find("div")
    assert tag is not None
    assert "class" not in tag.attrs
    print("test_empty_or_nonexistent_tags passed")

if __name__ == "__main__":
    test_name_xformer()
    test_attrs_xformer()
    test_xformer_side_effect()
    test_combined_transformers()
    test_nested_tags()
    test_empty_or_nonexistent_tags()
    print("All tests passed!")
