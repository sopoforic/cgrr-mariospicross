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
"""GUI for editing Mario's Picross levels."""
import logging

from tkinter import (Tk, Frame, Canvas, Menu, Label, Button,
                     DISABLED, NORMAL, W, E, N, S)
from tkinter.filedialog import askopenfilename, asksaveasfile

import MariosPicross

logging.basicConfig(level=logging.DEBUG)

class MainWindow(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, background="white")

        self.plugin = MariosPicross

        self.parent = parent

        self.initUI()

    def initUI(self):
        self.parent.title("Mario's Picross Puzzle Editor")
        self.puzzles = None

        # Build the menu
        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)
        fileMenu = Menu(menubar)
        self.fileMenu = fileMenu
        fileMenu.add_command(label="Open Mario's Picross ROM...",
                              command=self.onOpen)
        fileMenu.add_command(label="Save ROM as...",
                             command=self.onSave,
                             state=DISABLED)
        fileMenu.add_separator()
        fileMenu.add_command(label="Exit", command=self.onExit)
        menubar.add_cascade(label="File", menu=fileMenu)

        # Navigation
        Label(self.parent).grid(row=0, column=0)
        Label(self.parent).grid(row=0, column=4)
        self.parent.grid_columnconfigure(0, weight=1)
        self.parent.grid_columnconfigure(4, weight=1)

        prevButton = Button(self.parent,
                            text="<--",
                            command=self.onPrev,
                            state=DISABLED
        )
        self.prevButton = prevButton
        prevButton.grid(row=0, column=1)

        puzzle_number = 1
        self.puzzle_number = puzzle_number
        puzzleNumber = Label(self.parent, text="Puzzle #{}".format(puzzle_number))
        self.puzzleNumber = puzzleNumber
        puzzleNumber.grid(row=0, column=2)

        nextButton = Button(self.parent,
                            text="-->",
                            command=self.onNext,
                            state=DISABLED
        )
        self.nextButton = nextButton
        nextButton.grid(row=0, column=3)

        # Canvas
        canvas = Canvas(self.parent)
        self.canvas = canvas
        for i in range(15):
            for j in range(15):
                fillcolor = "gray80"
                self.canvas.create_rectangle(10+20*j,     10+20*i,
                                             10+20*(j+1), 10+20*(i+1),
                                             fill=fillcolor,
                                             tags="{},{}".format(i, j)
                )
        self.canvas.bind("<ButtonPress-1>", self.onClick)
        canvas.grid(row=1, columnspan=5, sticky=W+E+N+S)
        self.parent.grid_rowconfigure(1, weight=1)

    def onOpen(self):
        filepath = askopenfilename()
        with open(filepath, "rb") as f:
            self.rom = f.read()
        self.puzzles = self.plugin.read_puzzles_from_rom(self.rom)
        self.fileMenu.entryconfig(1, state=DISABLED)
        self.fileMenu.entryconfig(2, state=NORMAL)
        self.nextButton['state'] = NORMAL
        self.prevButton['state'] = NORMAL
        self.draw_puzzle()

    def onSave(self):
        with asksaveasfile(mode='wb') as outfile:
            outfile.write(self.rom)
            self.plugin.insert_puzzles(outfile, self.puzzles[1:])

    def onExit(self):
        self.quit()

    def draw_puzzle(self):
        for i in range(15):
            for j in range(15):
                fillcolor = (
                    "gray40" if self.puzzles[self.puzzle_number]['puzzle'][i][j]
                    else "gray80")
                self.canvas.itemconfig("{},{}".format(i,j), fill=fillcolor)

    def onPrev(self):
        if self.puzzle_number == 1:
            self.puzzle_number = 256
        else:
            self.puzzle_number -= 1
        self.puzzleNumber['text'] = "Puzzle #{}".format(self.puzzle_number)
        self.draw_puzzle()

    def onNext(self):
        if self.puzzle_number == 256:
            self.puzzle_number = 1
        else:
            self.puzzle_number += 1
        self.puzzleNumber['text'] = "Puzzle #{}".format(self.puzzle_number)
        self.draw_puzzle()

    def onClick(self, event):
        if not self.puzzles:
            return
        num = event.widget.find_closest(event.x, event.y)[0]
        i = num // 15
        j = (num - 1) % 15
        value = self.puzzles[self.puzzle_number]['puzzle'][i][j]
        self.puzzles[self.puzzle_number]['puzzle'][i][j] = not value
        fillcolor = (
                    "gray40" if self.puzzles[self.puzzle_number]['puzzle'][i][j]
                     else "gray80"
        )
        self.canvas.itemconfig(num, fill=fillcolor)

        # set the puzzle size
        if (any([self.puzzles[self.puzzle_number]['puzzle'][i][j]
                 for i in range(15)
                 for j in range(10, 15)]) or
            any([self.puzzles[self.puzzle_number]['puzzle'][i][j]
                 for i in range(10,15)
                 for j in range(15)])):
            self.puzzles[self.puzzle_number]['width'] = 15
            self.puzzles[self.puzzle_number]['height'] = 15
        elif (any([self.puzzles[self.puzzle_number]['puzzle'][i][j]
                   for i in range(10)
                   for j in range(5, 10)]) or
              any([self.puzzles[self.puzzle_number]['puzzle'][i][j]
                   for i in range(5,10)
                   for j in range(10)])):
            self.puzzles[self.puzzle_number]['width'] = 10
            self.puzzles[self.puzzle_number]['height'] = 10
        else:
            self.puzzles[self.puzzle_number]['width'] = 5
            self.puzzles[self.puzzle_number]['height'] = 5

def main():


    root = Tk()
    root.geometry("320x350+300+300")
    root.resizable(0,0)
    app = MainWindow(root)
    root.mainloop()

if __name__ == '__main__':
    main()
