#!/usr/bin/env python3

import re

class Assignment():
    def __init__(self, range) -> None:
        self.range = range

    def __str__(self) -> str:
        return f'{self.range[0]}-{self.range[1]}'

    def contains(self, a):
        """ does self contain a ?"""
        return self.range[0] <= a.range[0] and self.range[1] >= a.range[1]

    def overlaps(self, a):
        """ does self overlap a at all?"""
        if self.range[0] > a.range[1] or self.range[1] < a.range[0]:
            return False
        return True

inc_count = 0
ovl_count = 0
with open(('04/input.txt')) as f:
    for line in f.read().split('\n'):
        if line == '':
            continue
        (range_a, range_b) = line.split(',')
        nums = re.findall(r'\d+', line)

        ass_a = Assignment([int(x) for x in nums[0:2]])
        ass_b = Assignment([int(x) for x in nums[2:4]])

        if ass_a.contains(ass_b) or ass_b.contains(ass_a):
            inc_count += 1;

        if ass_a.overlaps(ass_b):
            ovl_count += 1;

print(f'total contains {inc_count}')
print(f'total overlap {ovl_count}')