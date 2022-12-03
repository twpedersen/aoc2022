#!/usr/bin/env python3

# rock paper scissor
# them
# A - rock
# B - Paper
# C - scissor

# us
# X - rock
# Y - Paper
# Z - scissor

ROCK_PTS = 1
PAPER_PTS = 2
SCISSOR_PTS = 3

LOSE = 0
DRAW = 3
WIN = 6

class Shape():
    def __init__(self, name, points) -> None:
        self.name = name
        self.points = points

    def beats(self):
        if self == ROCK:
            return SCISSOR
        elif self == PAPER:
            return ROCK
        elif self == SCISSOR:
            return PAPER

    def fight(self, a):
        if self.beats() == a:
            return WIN
        elif a.beats() == self:
            return LOSE
        elif self == a:
            return DRAW
        else:
            raise Exception

    def get_shape(self, outcome):
        if outcome == LOSE:
            return self.beats()
        elif outcome == DRAW:
            return self
        elif outcome == WIN:
            return self.beats().beats()
        else:
            raise Exception

ROCK = Shape("rock", ROCK_PTS)
PAPER = Shape("paper", PAPER_PTS)
SCISSOR = Shape("scissor", SCISSOR_PTS)

def char_to_shape(char):
    if char == 'X' or char == 'A':
        return ROCK
    elif char == 'B' or char == 'Y':
        return PAPER
    elif char == 'C' or char == 'Z':
        return SCISSOR
    else:
        raise Exception

def get_outcome(char):
    if char == 'X':
        return LOSE
    elif char == 'Y':
        return DRAW
    elif char == 'Z':
        return WIN
    else:
        raise Exception

total = 0
with open("./02/input.txt", "r") as guide:
    for line in guide.read().split('\n'):
        if line == '':
            continue
        theirs, ours = line.split()
        theirs = char_to_shape(theirs)
        ours = char_to_shape(ours)
        total += ours.points
        total += ours.fight(theirs)

print(f"scenario 1 total our points {total}")

total = 0

with open("./02/input.txt", "r") as guide:
    for line in guide.read().split('\n'):
        if line == '':
            continue
        theirs, ours = line.split()
        theirs = char_to_shape(theirs)
        outcome = get_outcome(ours)
        ours = theirs.get_shape(outcome)
        if outcome != ours.fight(theirs):
            print('unexpected outcome')
        total += ours.fight(theirs)
        total += ours.points

print(f"scenario 2 total our points {total}")