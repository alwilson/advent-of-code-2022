#!/usr/bin/env python3

def parse(file):
    elf_cals = []
    with open(file) as fd:
        cals = []
        for line in fd:
            line = line.strip()
            if line == "":
                elf_cals.append(cals)
                cals = []
            else:
                cals.append(int(line))

    return elf_cals


def solve(file):
    elf_cals = parse(file)

    tot_cals = [sum(cals) for cals in elf_cals]
    tot_cals.sort()
    
    print(f'Part 1 - {file}: {tot_cals[-1]}')
    print(f'Part 2 - {file}: {sum(tot_cals[-3:])}')


solve('./example.txt')
solve('./input.txt')