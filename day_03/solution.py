#!/usr/bin/env python3

def parse(file):
    sacks = [line.strip() for line in open(file)]
    return sacks


def solve(file):
    sacks = parse(file)

    score = 0
    for sack in sacks:
        comp1 = set(sack[0:len(sack)//2])
        comp2 = set(sack[len(sack)//2:])

        comp_inter = comp1.intersection(comp2)
        c = comp_inter.pop()
        if c.isupper(): score += ord(c) - ord('A') + 27
        else:           score += ord(c) - ord('a') + 1

    print(f'Part 1 - {file}: {score}') 

    score = 0
    sacks_i = iter(sacks)
    for sack1 in sacks_i:
        sack1 = set(sack1)
        sack2 = set(next(sacks_i))
        sack3 = set(next(sacks_i))

        all_sacks_inter = sack1.intersection(sack2).intersection(sack3)
        c = all_sacks_inter.pop()
        if c.isupper(): score += ord(c) - ord('A') + 27
        else:           score += ord(c) - ord('a') + 1

    print(f'Part 2 - {file}: {score}') 


solve('./example.txt')
solve('./input.txt')