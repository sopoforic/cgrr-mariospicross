# Classic Game Resource Reader (CGRR): Parse resources from classic games.
# Copyright (C) 2014-2015  Tracy Poff
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
        import mariospicross

        self.mariospicross = mariospicross
        # This is a set of four puzzles that read 'T', 'E', 'S', 'T' in several
        # sizes.
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
        self.mariospicross = None
        self.puzzlesdata = None

    def test_read_puzzles(self):
        """Verify that read_puzzles correctly decodes known input."""
        X = True
        O = False
        correct = [
            {'height' : 5,
             'width'  : 5,
             'puzzle' : [
               [X, X, X, X, X, O, O, O, O, O, O, O, O, O, O, O],
               [O, O, X, O, O, O, O, O, O, O, O, O, O, O, O, O],
               [O, O, X, O, O, O, O, O, O, O, O, O, O, O, O, O],
               [O, O, X, O, O, O, O, O, O, O, O, O, O, O, O, O],
               [O, O, X, O, O, O, O, O, O, O, O, O, O, O, O, O],
               [O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O],
               [O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O],
               [O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O],
               [O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O],
               [O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O],
               [O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O],
               [O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O],
               [O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O],
               [O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O],
               [O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O],
             ]
            },
            {'height' : 10,
             'width'  : 10,
             'puzzle' : [
               [X, X, X, X, X, X, X, X, X, X, O, O, O, O, O, O],
               [X, X, O, O, O, O, O, O, O, O, O, O, O, O, O, O],
               [X, X, O, O, O, O, O, O, O, O, O, O, O, O, O, O],
               [X, X, O, O, O, O, O, O, O, O, O, O, O, O, O, O],
               [X, X, X, X, X, X, X, X, X, X, O, O, O, O, O, O],
               [X, X, O, O, O, O, O, O, O, O, O, O, O, O, O, O],
               [X, X, O, O, O, O, O, O, O, O, O, O, O, O, O, O],
               [X, X, O, O, O, O, O, O, O, O, O, O, O, O, O, O],
               [X, X, O, O, O, O, O, O, O, O, O, O, O, O, O, O],
               [X, X, X, X, X, X, X, X, X, X, O, O, O, O, O, O],
               [O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O],
               [O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O],
               [O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O],
               [O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O],
               [O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O],
             ],
            },
            {'height' : 15,
             'width'  : 15,
             'puzzle' : [
               [X, X, X, X, X, X, X, X, X, X, X, X, X, X, X, O],
               [X, X, X, X, X, X, X, X, X, X, X, X, X, X, X, O],
               [X, X, X, O, O, O, O, O, O, O, O, O, O, O, O, O],
               [X, X, X, O, O, O, O, O, O, O, O, O, O, O, O, O],
               [X, X, X, O, O, O, O, O, O, O, O, O, O, O, O, O],
               [X, X, X, O, O, O, O, O, O, O, O, O, O, O, O, O],
               [X, X, X, X, X, X, X, X, X, X, X, X, X, X, X, O],
               [X, X, X, X, X, X, X, X, X, X, X, X, X, X, X, O],
               [O, O, O, O, O, O, O, O, O, O, O, O, X, X, X, O],
               [O, O, O, O, O, O, O, O, O, O, O, O, X, X, X, O],
               [O, O, O, O, O, O, O, O, O, O, O, O, X, X, X, O],
               [O, O, O, O, O, O, O, O, O, O, O, O, X, X, X, O],
               [X, X, X, X, X, X, X, X, X, X, X, X, X, X, X, O],
               [X, X, X, X, X, X, X, X, X, X, X, X, X, X, X, O],
               [O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O],
             ]
            },
            {'height' : 10,
             'width'  : 10,
             'puzzle' : [
               [X, X, X, X, X, X, X, X, X, X, O, O, O, O, O, O],
               [X, X, X, X, X, X, X, X, X, X, O, O, O, O, O, O],
               [O, O, O, O, X, X, O, O, O, O, O, O, O, O, O, O],
               [O, O, O, O, X, X, O, O, O, O, O, O, O, O, O, O],
               [O, O, O, O, X, X, O, O, O, O, O, O, O, O, O, O],
               [O, O, O, O, X, X, O, O, O, O, O, O, O, O, O, O],
               [O, O, O, O, X, X, O, O, O, O, O, O, O, O, O, O],
               [O, O, O, O, X, X, O, O, O, O, O, O, O, O, O, O],
               [O, O, O, O, X, X, O, O, O, O, O, O, O, O, O, O],
               [O, O, O, O, X, X, O, O, O, O, O, O, O, O, O, O],
               [O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O],
               [O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O],
               [O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O],
               [O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O],
               [O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O],
             ]
            }
        ]

        assert self.mariospicross.read_puzzles(self.puzzlesdata) == correct

    def test_write_puzzles(self):
        """Test roundtripping with write_puzzles."""

        puzzles = self.mariospicross.read_puzzles(self.puzzlesdata)

        assert self.mariospicross.write_puzzles(puzzles) == self.puzzlesdata.getvalue()
