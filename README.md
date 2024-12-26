# Bingo Game Generator
A module for generating bingo cards, each consisting of 5 bingo boards, each bingo board (3*5 x 5) have a unique number in each cell for that board. You feed in the prize distribution data and generate the desired amount of bingo cards. It will give you a tuple; the list of bingo cards and a dictionary indicating the winning row combination for each prize. The winning board will be distributed using the round robin algorithm in the bingo card.

For a demo of the module:

    python bingo_demo.py


