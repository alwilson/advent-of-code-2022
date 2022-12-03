#!/usr/bin/env python3

def parse(file):
    plays = [line.strip().split(' ') for line in open(file)]
    return plays


def solve(file):
    plays = parse(file)

    score = 0
    for play in plays:
        if play[0] == 'A':
            if play[1] == 'X': score += 1; score += 3
            if play[1] == 'Y': score += 2; score += 6
            if play[1] == 'Z': score += 3; score += 0
        if play[0] == 'B':
            if play[1] == 'X': score += 1; score += 0
            if play[1] == 'Y': score += 2; score += 3
            if play[1] == 'Z': score += 3; score += 6
        if play[0] == 'C':
            if play[1] == 'X': score += 1; score += 6
            if play[1] == 'Y': score += 2; score += 0
            if play[1] == 'Z': score += 3; score += 3

    print(f'Part 1 - {file}: {score}')

    score = 0
    for play in plays:
        if play[0] == 'A':
            if play[1] == 'Z': score += 2; score += 6
            if play[1] == 'Y': score += 1; score += 3
            if play[1] == 'X': score += 3; score += 0
        if play[0] == 'B':
            if play[1] == 'Z': score += 3; score += 6
            if play[1] == 'Y': score += 2; score += 3
            if play[1] == 'X': score += 1; score += 0
        if play[0] == 'C':
            if play[1] == 'Z': score += 1; score += 6
            if play[1] == 'Y': score += 3; score += 3
            if play[1] == 'X': score += 2; score += 0

    print(f'Part 2 - {file}: {score}')


solve('./example.txt')
solve('./input.txt')