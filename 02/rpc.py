#!/usr/bin/env python

# rock paper scissor
# them
# A - rock
# B - Paper
# C - scissor

# us
# X - rock
# Y - Paper
# Z - scissor

ROCK = 1
PAPER = 2
SCISSOR = 3

LOSE = 0
DRAW = 3
WIN = 6

class Move():
    def __init__(self, move, char) -> None:
        self.move = move
        self.char = char

points = {
    ROCK: 1,
    PAPER: 2,
    SCISSOR: 3
}

beats = {
    ROCK: SCISSOR,
    PAPER: ROCK,
    SCISSOR: PAPER
}

them = {
    'A': ROCK,
    'B': PAPER,
    'C': SCISSOR
}

us = {
    'X': ROCK,
    'Y': PAPER,
    'Z': SCISSOR
}

guide = open("./02/input.txt", "r")

total = 0
for line in guide.read().split('\n'):
    if line == '':
        continue
    theirs, ours = line.split()
    their_move = them[theirs]
    our_move = us[ours]
    total += points[our_move]
    if beats[their_move] == our_move:
        total += LOSE
    elif beats[our_move] == their_move:
        total += WIN
    else:
        total += DRAW

print(f"total our points {total}")