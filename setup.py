from distutils.core import setup
import py2exe

setup(
    name="Mario's Picross Puzzle Editor GUI",
    description="GUI editor for puzzles in the Game Boy Mario's Picross ROM",
    author="Tracy Poff",
    author_email="tracy.poff@gmail.com",
    windows=['marios_picross_puzzle_editor_gui.py']
)
