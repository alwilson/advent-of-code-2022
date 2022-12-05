#!/usr/bin/env python3

def parse(file):
  lines = [line for line in open(file)]
  stacks = [[] for i in range(len(lines[0])//4)]

  lines_i = iter(lines)
  while (line := next(lines_i, None)) is not None:
    if line.strip() == '':
      break
    
    s_i = 0
    for i in range(1, len(line), 4):
      c = line[i]
      if c.isalpha():
        stacks[s_i].insert(0, c)
      s_i += 1

  moves = []
  while (line := next(lines_i, None)) is not None:
    split = line.split()
    moves.append((int(split[1]), int(split[3])-1, int(split[5])-1))

  return stacks, moves


def solve1(file):
    stacks, moves = parse(file)

    for (num, src, dst) in moves:
      for i in range(num):
        temp = stacks[src].pop()
        stacks[dst].append(temp)
    print(f'Part 1 - {file}:', ''.join([stack[-1] for stack in stacks]))


def solve2(file):
    stacks, moves = parse(file)

    for (num, src, dst) in moves:
      temp_l = []
      for i in range(num):
        temp = stacks[src].pop()
        temp_l.insert(0, temp)
      
      stacks[dst] += temp_l
    print(f'Part 2 - {file}:', ''.join([stack[-1] for stack in stacks]))


solve1('./example.txt')
solve1('./input.txt')

solve2('./example.txt')
solve2('./input.txt')