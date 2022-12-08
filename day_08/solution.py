#!/usr/bin/env python3

import pprint as pp

def parse(file, debug=False):
  trees = [[int(x) for x in line.strip()] for line in open(file)]
  return trees

def show_seen(trees, seen):
    for y in range(0, len(trees)):
      for x in range(0, len(trees[0])):
        if (x,y) in seen:
          print('X', end='')
        else:
          print(' ', end='')
      print()


def solve1(file, debug=False):
    trees = parse(file, debug)

    seen = {}

    # Mark edges seen
    for x in range(len(trees[0])):
      seen[(0           ,x)] = True
      seen[(len(trees)-1,x)] = True
    for x in range(len(trees)):
      seen[(x,               0)] = True
      seen[(x, len(trees[0])-1)] = True

    # Looking South
    for x in range(1, len(trees[0])-1):
      curr_h = trees[0][x]
      for y in range(1, len(trees)-1):
        if trees[y][x] > curr_h:
          seen[(x,y)] = True
          curr_h = trees[y][x]

    # Looking North
    for x in range(1, len(trees[0])-1):
      curr_h = trees[len(trees)-1][x]
      for y in range(len(trees)-1-1, 0, -1):
        if trees[y][x] > curr_h:
          seen[(x,y)] = True
          curr_h = trees[y][x]

    # Looking East
    for y in range(1, len(trees)-1):
      curr_h = trees[y][0]
      for x in range(1, len(trees[0])-1):
        if trees[y][x] > curr_h:
          seen[(x,y)] = True
          curr_h = trees[y][x]

    # Looking West
    for y in range(1, len(trees)-1):
      curr_h = trees[y][len(trees[0])-1]
      for x in range(len(trees[0])-1-1, 0, -1):
        if trees[y][x] > curr_h:
          seen[(x,y)] = True
          curr_h = trees[y][x]

    if debug: show_seen(trees, seen)
    print(f'Part 1 - {file}: {len(seen.keys())=}')


def solve2(file, debug=False):
    trees = parse(file, debug)

    max_score = 0
    for y in range(1, len(trees)-1):
      for x in range(1, len(trees[0])-1):
        score = 1
        curr_h = trees[y][x]

        # Looking South
        dist_seen = 0
        for ny in range(y+1, len(trees)):
          dist_seen += 1
          if trees[ny][x] >= curr_h:
            break
        if debug: print(f'{dist_seen=}')
        if dist_seen > 0:
          score *= dist_seen

        # Looking North
        dist_seen = 0
        for ny in range(y-1, -1, -1):
          dist_seen += 1
          if trees[ny][x] >= curr_h:
            break
        if debug: print(f'{dist_seen=}')
        if dist_seen > 0:
          score *= dist_seen

        # Looking East
        dist_seen = 0
        for nx in range(x+1, len(trees[0])):
          dist_seen += 1
          if trees[y][nx] >= curr_h:
            break
        if debug: print(f'{dist_seen=}')
        if dist_seen > 0:
          score *= dist_seen

        # Looking West
        dist_seen = 0
        for nx in range(x-1, -1, -1):
          dist_seen += 1
          if trees[y][nx] >= curr_h:
            break
        if debug: print(f'{dist_seen=}')
        if dist_seen > 0:
          score *= dist_seen
          
        if debug: print(f'({x},{y}) {curr_h=}: {score=}')

        if score > max_score:
          max_score = score
          if debug: print(f'({x},{y}): {score=}')

    print(f'Part 2 - {file}: {max_score=}')


solve1('./example.txt')
solve1('./input.txt')

solve2('./example.txt')
solve2('./input.txt')