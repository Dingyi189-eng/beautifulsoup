# Milestone-3

## Overview
Milestone3 extends the SoupReplacer API to support parsing-time transformations of HTML/XML tags.
Compared to Milestone 2, the new API supports flexible transformations using functions (name_xformer, attrs_xformer, xformer) rather than just simple tag replacement.

## Directory Structure
```
beautifulsoup/
├── apps/
│   └── m3/
│       └── task7.py
├── bs4/
│   ├── tests/
│   │   └── test_soupreplacer_m3.py
│   └── soup_replacer.py
```

## task7.py
### Overview
Find all the <p> tags and add (or replace) a class attribute class="test" using SoupReplacer's xformer API.
### How to Run
```
cd apps/m3
```
```
python task7.py example.html
```

## test_soupreplacer_m3.py
### Overview
This test suite validates all key features of the SoupReplacer API in Milestone 3. It checks that tag names can be transformed dynamically (name_xformer), attributes can be modified (attrs_xformer), and arbitrary side-effect transformations can be applied (xformer) during parsing. 
The tests also cover combined transformations on a single tag, nested tags, and scenarios where no transformation is needed to ensure non-targeted tags remain unchanged.
### How to Run
```
cd bs4/tests
```
```
python test_soupreplacer_m3.py
```

## Technical Brief
In Milestone 2, `SoupReplacer` allowed simple tag replacements (`og_tag → alt_tag`) during parsing, which avoids extra tree traversal and improves performance for large HTML/XML files.

In Milestone 3, I extended it to support more flexible transformations using functions:
- `name_xformer` to change tag names
- `attrs_xformer` to modify attributes
- `xformer` for general-purpose side effects

These new options make it easy to apply complex changes while parsing, keeping the API efficient and more reusable.

**Recommendation:** Adopt the Milestone 3 API as the main extension. Provide documentation and examples for common transformations, and consider adding prebuilt transformers for frequent use cases. This API improves both flexibility and performance, making BeautifulSoup more powerful for developers.
