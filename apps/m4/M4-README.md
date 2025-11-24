# Milestone-4

## Overview
Milestone 4 adds iteration support directly to the BeautifulSoup class.
By implementing the `__iter__()` method and a recursive generator,
```
def __iter__(self):
    return self._traverse(self)

def _traverse(self, node):
    yield node
    for child in getattr(node, 'children', []):
        yield from self._traverse(child)
```
Soup object can now be used in any Python iterator context.

A user can write:
```
for node in soup:
    print(node)
```
and BeautifulSoup will traverse every node in the parse tree.

### How It Works

Python’s `for ... in ...` loop requires the object to implement:

- `__iter__()` → return an iterator

Once this method exists, the Soup object can be used in any iterator context.


## Direction Structure
```
beautifulsoup/
├── apps/
│   └── m4/
│       └── task8.py
├── bs4/
│   ├── tests/
│   │   └── test_iteration.py
│   └── __init__.py
```

## task8.py
### Overview

This application demonstrates the new iteration feature.
Given an HTML file, it loads the document using BeautifulSoup and prints every node following depth-first traversal.

### How to Run
```
cd apps/m4
```
```
python task8.py example.html
```

## test_iteration.py
### Overview

This test suite validates all iteration behavior required in Milestone 4.
The tests include:
- Iterating over a simple tree
- Ensuring the root appears first (depth-first)
- Ensuring text nodes are detected (or excluded at top level)
- Traversing deeply nested structures
- Handling empty documents correctly
### How to Run

```
cd bs4/tests
```
```
python test_iteration.py
```