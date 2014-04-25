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
"""Parses Mario's Picross data."""
import logging
import struct
import os

import yapsy

import utilities
from utilities import File, FileReader

class MariosPicross(yapsy.IPlugin.IPlugin):
    """Parses Mario's Picross data."""

    # I was able to put this together easily thanks to a document by Killa B
    # describing the layout of these levels and where they're located in the
    # ROM. You can find it at:
    #
    # http://www.zophar.net/fileuploads/3/21546xutra/picrossleveldata.txt

    key = "marios_picross_a"
    title = "Mario's Picross"
    developer = "Jupiter Corp."
    description = "Mario's Picross (Game Boy)"

    identifying_files = [
        File("mariop.gb", 262144, "ccaf9331318d4dfe3d1ee681928a74fd"), # US
    ]

    # 1 -> True, 0 -> False
    int_to_bitfield = lambda r: [bool((r >> (15 - n) & 1)) for n in range(16)]
    # True -> 1, False -> 0
    bitfield_to_int = lambda r: sum([2 ** n for n in range(16) if r[15-n]])

    puzzle_reader = FileReader(
        format = [
            ("row1",   "H"),
            ("row2",   "H"),
            ("row3",   "H"),
            ("row4",   "H"),
            ("row5",   "H"),
            ("row6",   "H"),
            ("row7",   "H"),
            ("row8",   "H"),
            ("row9",   "H"),
            ("row10",  "H"),
            ("row11",  "H"),
            ("row12",  "H"),
            ("row13",  "H"),
            ("row14",  "H"),
            ("row15",  "H"),
            ("width",  "B"),
            ("height", "B"),
        ],
        massage_in = {
            "row1"  : int_to_bitfield,
            "row2"  : int_to_bitfield,
            "row3"  : int_to_bitfield,
            "row4"  : int_to_bitfield,
            "row5"  : int_to_bitfield,
            "row6"  : int_to_bitfield,
            "row7"  : int_to_bitfield,
            "row8"  : int_to_bitfield,
            "row9"  : int_to_bitfield,
            "row10" : int_to_bitfield,
            "row11" : int_to_bitfield,
            "row12" : int_to_bitfield,
            "row13" : int_to_bitfield,
            "row14" : int_to_bitfield,
            "row15" : int_to_bitfield,
        },
        massage_out = {
            "row1"  : bitfield_to_int,
            "row2"  : bitfield_to_int,
            "row3"  : bitfield_to_int,
            "row4"  : bitfield_to_int,
            "row5"  : bitfield_to_int,
            "row6"  : bitfield_to_int,
            "row7"  : bitfield_to_int,
            "row8"  : bitfield_to_int,
            "row9"  : bitfield_to_int,
            "row10" : bitfield_to_int,
            "row11" : bitfield_to_int,
            "row12" : bitfield_to_int,
            "row13" : bitfield_to_int,
            "row14" : bitfield_to_int,
            "row15" : bitfield_to_int,
        },
        byte_order = ">",
    )

    @staticmethod
    def verify(path):
        """Verify that the provided path is the supported game."""
        return utilities.verify(MariosPicross.identifying_files, path)

    @staticmethod
    def read_puzzles_from_rom(data):
        """Return all levels stored in the ROM given by data."""
        from io import BytesIO
        # Thanks to Killa B for writing these addresses down.
        PUZZLES_BEGIN = 0x92b0
        PUZZLES_END   = 0xa2b0
        puzzle_chunk = BytesIO(data[PUZZLES_BEGIN:PUZZLES_END])
        return MariosPicross.read_puzzles(puzzle_chunk)

    @staticmethod
    def read_puzzles(data):
        """Return a list of all levels stored in data.

        The format for an individual puzzle that looks like this

            XXXXX
            OOXOO
            OOXOO
            OOXOO

        Will be

        { "row1" : [True,  True,  True,  True,  True]  + [False]*11,
          "row2" : [False, False, True,  False, False] + [False]*11,
          "row3" : [False, False, True,  False, False] + [False]*11,
          "row4" : [False, False, True,  False, False] + [False]*11,
          "row5" : [False, False, True,  False, False] + [False]*11,
          "row6" : [False]*16,
          . . . rows 7-14 look the same . . .
          "row15"  : [False]*16,
          "width"  : 5,
          "height" : 5,
        }

        Notice that every puzzle will contain 15 rows of 15 columns each, and
        its actual size is specified by the 'width' and 'height' entries in the
        dict.

        """
        puzzles = []
        for puzzle in iter(lambda: data.read(MariosPicross.puzzle_reader.struct.size), b""):
            puzzles.append(MariosPicross.puzzle_reader.unpack(puzzle))
        return puzzles
