#!/usr/bin/env python3

import pprint as pp


def parse(file, debug=False):
  lines = [line.strip() for line in open(file)]

  grid = {}
  start = (0, 0)
  end = (0, 0)
  for y, line in enumerate(lines):
    for x, c in enumerate(line):
      if c == 'S':
        start = (x,y)
        c = 'a'
      if c == 'E':
        end = (x,y)
        c = 'z'
      grid[(x,y)] = ord(c) - ord('a')

  return start, end, grid


def print_heights(s, e, grid):
  x_min = min([v[0] for v in list(grid.keys())])
  x_max = max([v[0] for v in list(grid.keys())])
  y_min = min([v[1] for v in list(grid.keys())])
  y_max = max([v[1] for v in list(grid.keys())])

  for y in range(y_min, y_max+1):
    for x in range(x_min, x_max+1):
      if (x,y) == s:
        print('S', end='')
      elif (x,y) == e:
        print('E', end='')
      else:
        print(chr(grid[(x,y)] + ord('a')), end='')
    print()
  print()


def print_visited(s, e, grid, visited):
  x_min = min([v[0] for v in list(grid.keys())])
  x_max = max([v[0] for v in list(grid.keys())])
  y_min = min([v[1] for v in list(grid.keys())])
  y_max = max([v[1] for v in list(grid.keys())])

  for y in range(y_min, y_max+1):
    for x in range(x_min, x_max+1):
      if (x,y) == s:
        print('S', end='')
      elif (x,y) == e:
        print('E', end='')
      elif (x,y) in visited:
        print('*', end='')
      else:
        print(chr(grid[(x,y)] + ord('a')), end='')
    print()
  print()


def dijkstras(s, e, grid, debug=False):
  frontier = [s]
  visited = {}
  visited[s] = True
  steps = 0
    
  if debug: print(frontier)
  if debug: print_visited(s, e, grid, visited)

  while len(frontier) > 0 and e not in frontier:
    new_frontier = []

    for p in frontier:
      h = grid[p]
      np = (p[0], p[1]+1)
      if np in grid and np not in visited and np not in new_frontier and grid[np] <= h+1:
        new_frontier.append(np)
      np = (p[0], p[1]-1)
      if np in grid and np not in visited and np not in new_frontier and grid[np] <= h+1:
        new_frontier.append(np)
      np = (p[0]+1, p[1])
      if np in grid and np not in visited and np not in new_frontier and grid[np] <= h+1:
        new_frontier.append(np)
      np = (p[0]-1, p[1])
      if np in grid and np not in visited and np not in new_frontier and grid[np] <= h+1:
        new_frontier.append(np)

    for p in frontier:
      visited[p] = True
    frontier = new_frontier 
    
    if debug: print(frontier)
    if debug: print_visited(s, e, grid, visited)

    steps += 1

  return steps  


def dijkstras_p2(s, e, grid, debug=False):
  frontier = [s]
  visited = {}
  visited[s] = True
  steps = 0
    
  if debug: print(frontier)
  if debug: print_visited(s, e, grid, visited)

  while len(frontier) > 0 and not any([grid[f] == 0 for f in frontier]):
    new_frontier = []

    for p in frontier:
      h = grid[p]
      np = (p[0], p[1]+1)
      if np in grid and np not in visited and np not in new_frontier and grid[np] >= h-1:
        new_frontier.append(np)
      np = (p[0], p[1]-1)
      if np in grid and np not in visited and np not in new_frontier and grid[np] >= h-1:
        new_frontier.append(np)
      np = (p[0]+1, p[1])
      if np in grid and np not in visited and np not in new_frontier and grid[np] >= h-1:
        new_frontier.append(np)
      np = (p[0]-1, p[1])
      if np in grid and np not in visited and np not in new_frontier and grid[np] >= h-1:
        new_frontier.append(np)

    for p in frontier:
      visited[p] = True
    frontier = new_frontier 
    
    if debug: print(frontier)
    if debug: print_visited(s, e, grid, visited)

    steps += 1

  return steps 


def solve1(file, debug=False):
  start, end, grid = parse(file, debug)
  if debug: print(start, end)
  if debug: print_heights(start, end, grid)
  steps = dijkstras(start, end, grid, debug)
  print(f'Part 1 - {file}: {steps=}')


def solve2(file, debug=False):
  start, end, grid = parse(file, debug)
  if debug: print(start, end)
  if debug: print_heights(start, end, grid)
  steps = dijkstras_p2(end, start, grid, debug)
  print(f'Part 2 - {file}: {steps=}')


solve1('./example.txt', False)
solve1('./input.txt', False)
 
solve2('./example.txt')
solve2('./input.txt')