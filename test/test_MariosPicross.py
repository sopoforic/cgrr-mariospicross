# Classic Game Resource Reader (CGRR): Parse resources from classic games.
# Copyright (C) 2014  Tracy Poff
#
# This file is part of CGRR.
#
# CGRR is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# CGRR is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with CGRR.  If not, see <http://www.gnu.org/licenses/>.
import logging

class Test_marios_picross_a:

    def setup(self):
        import io
        
        from yapsy.PluginManager import PluginManager

        manager = PluginManager()
        manager.setPluginPlaces(["formats"])
        manager.collectPlugins()
        self.plugin = manager.getPluginByName("Mario's Picross").plugin_object
        # This mock data is a copy of a real score file
        mock = (b'\xf8\x00 \x00 \x00 \x00 \x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x05\xff'
                b'\xc0\xc0\x00\xc0\x00\xc0\x00\xff\xc0\xc0\x00\xc0\x00\xc0\x00'
                b'\xc0\x00\xff\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\n\n'
                b'\xff\xfe\xff\xfe\xe0\x00\xe0\x00\xe0\x00\xe0\x00\xff\xfe\xff'
                b'\xfe\x00\x0e\x00\x0e\x00\x0e\x00\x0e\xff\xfe\xff\xfe\x00\x00'
                b'\x0f\x0f\xff\xc0\xff\xc0\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x0c'
                b'\x00\x0c\x00\x0c\x00\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\n\n')
        self.puzzlesdata = io.BytesIO(mock)

    def teardown(self):
        self.plugin = None
        self.puzzlesdata = None

    def test_read_puzzles(self):
        X = True
        O = False
        correct = [
 {'height': 5,
  'row1':  [X, X, X, X, X, O, O, O, O, O, O, O, O, O, O, O],
  'row2':  [O, O, X, O, O, O, O, O, O, O, O, O, O, O, O, O],
  'row3':  [O, O, X, O, O, O, O, O, O, O, O, O, O, O, O, O],
  'row4':  [O, O, X, O, O, O, O, O, O, O, O, O, O, O, O, O],
  'row5':  [O, O, X, O, O, O, O, O, O, O, O, O, O, O, O, O],
  'row6':  [O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O],
  'row7':  [O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O],
  'row8':  [O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O],
  'row9':  [O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O],
  'row10': [O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O],
  'row11': [O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O],
  'row12': [O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O],
  'row13': [O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O],
  'row14': [O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O],
  'row15': [O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O],
  'width': 5},
 {'height': 10,
  'row1':  [X, X, X, X, X, X, X, X, X, X, O, O, O, O, O, O],
  'row2':  [X, X, O, O, O, O, O, O, O, O, O, O, O, O, O, O],
  'row3':  [X, X, O, O, O, O, O, O, O, O, O, O, O, O, O, O],
  'row4':  [X, X, O, O, O, O, O, O, O, O, O, O, O, O, O, O],
  'row5':  [X, X, X, X, X, X, X, X, X, X, O, O, O, O, O, O],
  'row6':  [X, X, O, O, O, O, O, O, O, O, O, O, O, O, O, O],
  'row7':  [X, X, O, O, O, O, O, O, O, O, O, O, O, O, O, O],
  'row8':  [X, X, O, O, O, O, O, O, O, O, O, O, O, O, O, O],
  'row9':  [X, X, O, O, O, O, O, O, O, O, O, O, O, O, O, O],
  'row10': [X, X, X, X, X, X, X, X, X, X, O, O, O, O, O, O],
  'row11': [O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O],
  'row12': [O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O],
  'row13': [O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O],
  'row14': [O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O],
  'row15': [O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O],
  'width': 10},
 {'height': 15,
  'row1':  [X, X, X, X, X, X, X, X, X, X, X, X, X, X, X, O],
  'row2':  [X, X, X, X, X, X, X, X, X, X, X, X, X, X, X, O],
  'row3':  [X, X, X, O, O, O, O, O, O, O, O, O, O, O, O, O],
  'row4':  [X, X, X, O, O, O, O, O, O, O, O, O, O, O, O, O],
  'row5':  [X, X, X, O, O, O, O, O, O, O, O, O, O, O, O, O],
  'row6':  [X, X, X, O, O, O, O, O, O, O, O, O, O, O, O, O],
  'row7':  [X, X, X, X, X, X, X, X, X, X, X, X, X, X, X, O],
  'row8':  [X, X, X, X, X, X, X, X, X, X, X, X, X, X, X, O],
  'row9':  [O, O, O, O, O, O, O, O, O, O, O, O, X, X, X, O],
  'row10': [O, O, O, O, O, O, O, O, O, O, O, O, X, X, X, O],
  'row11': [O, O, O, O, O, O, O, O, O, O, O, O, X, X, X, O],
  'row12': [O, O, O, O, O, O, O, O, O, O, O, O, X, X, X, O],
  'row13': [X, X, X, X, X, X, X, X, X, X, X, X, X, X, X, O],
  'row14': [X, X, X, X, X, X, X, X, X, X, X, X, X, X, X, O],
  'row15': [O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O],
  'width': 15},
 {'height': 10,
  'row1':  [X, X, X, X, X, X, X, X, X, X, O, O, O, O, O, O],
  'row2':  [X, X, X, X, X, X, X, X, X, X, O, O, O, O, O, O],
  'row3':  [O, O, O, O, X, X, O, O, O, O, O, O, O, O, O, O],
  'row4':  [O, O, O, O, X, X, O, O, O, O, O, O, O, O, O, O],
  'row5':  [O, O, O, O, X, X, O, O, O, O, O, O, O, O, O, O],
  'row6':  [O, O, O, O, X, X, O, O, O, O, O, O, O, O, O, O],
  'row7':  [O, O, O, O, X, X, O, O, O, O, O, O, O, O, O, O],
  'row8':  [O, O, O, O, X, X, O, O, O, O, O, O, O, O, O, O],
  'row9':  [O, O, O, O, X, X, O, O, O, O, O, O, O, O, O, O],
  'row10': [O, O, O, O, X, X, O, O, O, O, O, O, O, O, O, O],
  'row11': [O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O],
  'row12': [O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O],
  'row13': [O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O],
  'row14': [O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O],
  'row15': [O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O],
  'width': 10}
        ]

        assert self.plugin.read_puzzles(self.puzzlesdata) == correct
