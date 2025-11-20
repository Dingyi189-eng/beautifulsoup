# Milestone-2

## part1
how to run:
```
cd apps/m2
```
### task2.py
Print all hyperlinks using SoupStrainer.
```
python task2.py example.html
```
### task3.py
Print all tags in the document using SoupStrainer.
```
python task3.py example.html
```
### task4.py
Print all tags that have an id attribute using SoupStrainer.
```
python task4.py example.html
```

## part2
1. BeautifulSoup.__init__
   File: bs4/__init__.py
   Line: 209
2. Tag.find_all
   File: bs4/element.py
   Line: 2715
3. Tag.find
   File: bs4/element.py
   Line: 2684
4. Tag.find_parent
   File: bs4/element.py
   Line: 992
5. Tag.get
   File: bs4/element.py
   Line: 2160
6. Tag.prettify
   File: bs4/element.py
   Line: 2601
7. SoupStrainer.__init__()
   File: bs4/filter.py
   Line: 345
8. Tag.name
   File: bs4/element.py
   Line: 1648
9. Tag.attrs
   File: bs4/element.py
   Line: 1674

## part3
### task6.py
Replace all b tags with blockquote tags.
```
cd apps/m2
```
```
python task6.py example.html
```
### test_soup_replacer.py
Pytest unit tests for SoupReplacer.
```
pip install pytest
```
```
cd bs4/tests
```
```
pytest test_soup_replacer.py
```
