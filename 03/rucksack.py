#!/usr/bin/env python3

def find_dup(str1, str2):
    for char_1 in str1:
        for char_2 in str2:
            if char_1 == char_2:
                return char_1
    return None

def get_priority(item: str):
    """@item is really a character
    a-z: 1-26
    A-Z: 27-52

    ord('A') == 65
    ord('a') == 97
    """
    OFFSET_A = ord('A')
    OFFSET_a = ord('a')

    if item.islower():
        return ord(item) - OFFSET_a + 1
    else:
        return ord(item) - OFFSET_A + 1 + 26


def find_dup_sum():
    dup_sum = 0
    with open('./03/input.txt') as f:
        for rucksack in f.read().split('\n'):
            if rucksack == '':
                continue
            comp_len = len(rucksack) // 2
            comp_1 = rucksack[:comp_len]
            comp_2 = rucksack[comp_len:]
            assert (len(comp_1) == len(comp_2))

            dup_item = find_dup(comp_1, comp_2)
            prio = get_priority(dup_item)
            dup_sum += prio
            print(f'{rucksack}: {dup_item} - {prio}')

    print(f'{dup_sum}')

def find_badge(group: list):
    found_badges = {}
    group = sorted(group)

    # reference smallest rucksack
    ruck_1 = group[0]
    ruck_2 = group[1]
    ruck_3 = group[2]

    for item in ruck_1:
        if item in ruck_2 and item in ruck_3:
            return item

def find_badge_sum():
    badge_sum = 0
    group = []
    with open('./03/input.txt') as f:
        for rucksack in f.read().split('\n'):
            if rucksack == '':
                continue

            if len(group) < 3:
                group.append(rucksack)

            if len(group) == 3:
                badge = find_badge(group)
                print(f'found badge {badge}')
                badge_sum += get_priority(badge)
                group = []

    print(f'badge sum {badge_sum}')

find_dup_sum()
find_badge_sum()