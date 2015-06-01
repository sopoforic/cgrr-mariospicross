mariospicross
=============

This module allows reading and editing puzzles for the Game Boy game _Mario's
Picross_.

Usage
=====

`marios_picross_puzzle_editor_gui.py` provides a simple GUI for editing a
_Mario's Picross_ ROM to modify the puzzles. Under the hood, it uses
`mariospicross.py`.

To parse a ROM for puzzles, use `read_puzzles_from_rom`:

```python
with open("path/to/picross.gb", "rb") as romfile:
    data = romfile.read()
puzzles = mariospicross.read_puzzles_from_rom(data)
```

See the docstring on `read_puzzles` for the format of the parsed puzzles.

To insert puzzles back into a rom, use `insert_puzzles`

```python
puzzles = [{...}] # whatever puzzles you've made
with open("path/to/picross.gb", "rb") as romfile:
    data = romfile.read()
newdata = mariospicross.insert_puzzles(data, puzzles)
with open("path/to/new_rom.gb", "wb") as romfile:
    romfile.write(newdata)
```

The new ROM should work anywhere the original would.

Requirements
============

* Python 2.7+ or 3.2+
* cgrr from https://github.com/sopoforic/cgrr

You can install this with `pip install -r requirements.txt`.

License
=======

This module is available under the GPL v3 or later. See the file COPYING for
details.

[![Build Status](https://travis-ci.org/sopoforic/cgrr-mariospicross.svg?branch=master)](https://travis-ci.org/sopoforic/cgrr-mariospicross)
[![Code Health](https://landscape.io/github/sopoforic/cgrr-mariospicross/master/landscape.svg?style=flat)](https://landscape.io/github/sopoforic/cgrr-mariospicross/master)
