[简体中文](README.zh.md) | English

# RawGrassTranslator

## Description

In the translation industry, there are "raw meat" and "cooked meat", where "raw meat" refers to something that has not been translated, and "cooked meat" refers to something that has been translated. However, some things will be completely separated from the original meaning after being translated many times by the machine. We call it "raw grass". Raw Grass Translator helps you turn "raw meat" into "raw grass" with Google Translate.


## Installation

This program does not need to be installed and is ready to use right away.

If you want to run the source code from Python, you need to install [Google Translate module for Python](https://github.com/ssut/py-googletrans).

It can be installed with one command:

```bash
python -m pip install googletrans
```

Alternatively, if you want to use Python 3, you can use the following command:

```bash
python3 -m pip install googletrans
```

## Instructions

### Windows

You don't need to install Python, just double-click `rawgrass.exe` and follow the instructions.

You can also run `rawgrass.py` from Python, but only if you have the [Google Translate module for Python](https://github.com/ssut/py-googletrans) installed.

### macOS / Linux

You need to run the source code, so you need to install the [Google Translate module for Python](https://github.com/ssut/py-googletrans). See the ["Installation"](#Installation) section.

The file `rawgrass-python.py` has `#!/usr/bin/env python` at the beginning and is executable and can be run directly in the terminal (type `./rawgrass-python.py`).

The file `rawgrass-python3.py` has `#!/usr/bin/env python3` at the beginning and is executable and can be run directly in the terminal (type `./rawgrass-python3.py`).

Of course, it is also possible to run `rawgrass.py` directly from Python.

## Contribution

1.  Fork the repository
2.  Create Feat_xxx branch
3.  Commit your code
4.  Create Pull Request
