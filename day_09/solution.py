#!/usr/bin/env python3

import pprint as pp

def parse(file, debug=False):
  lines = [line.strip() for line in open(file)]
  moves = []
  for line in lines:
    split = line.split()
    moves.append((split[0], int(split[1])))
  return moves


def print_board(visited, t, h):
  for y in range(5, -1, -1):
    for x in range(6):
      if (x,y) == h:
        print('H', end='')
      elif (x,y) == t:
        print('T', end='')
      elif (x, y) == (0, 0):
        print('s', end='')
      elif (x,y) in visited:
        print('*', end='')
      else:
        print('.', end='')
    print()
  print()

def update_tail(visited, t, h):
  if abs(h[0] - t[0]) > 1:
    if h[0] > t[0]:
      t = (t[0]+1, t[1])
    else:
      t = (t[0]-1, t[1])

    if h[1] > t[1]:
      t = (t[0], t[1]+1)
    if h[1] < t[1]:
      t = (t[0], t[1]-1)

  if abs(h[1] - t[1]) > 1:
    if h[1] > t[1]:
      t = (t[0], t[1]+1)
    else:
      t = (t[0], t[1]-1)

    if h[0] > t[0]:
      t = (t[0]+1, t[1])
    if h[0] < t[0]:
      t = (t[0]-1, t[1])

  
  return t


def solve1(file, debug=False):
    moves = parse(file, debug)

    h = (0, 0)
    t = (0, 0)
    visited = {}
    visited[t] = True


    for move in moves:
      if debug: print(move)
      if move[0] == 'R':
        for _ in range(move[1]):
          h = (h[0]+1, h[1])
          t = update_tail(visited, t, h)
          visited[t] = True
          if debug: print_board(visited, t, h)
      if move[0] == 'L':
        for _ in range(move[1]):
          h = (h[0]-1, h[1])
          t = update_tail(visited, t, h)
          visited[t] = True
          if debug: print_board(visited, t, h)
      if move[0] == 'U':
        for _ in range(move[1]):
          h = (h[0], h[1]+1)
          t = update_tail(visited, t, h)
          visited[t] = True
          if debug: print_board(visited, t, h)
      if move[0] == 'D':
        for _ in range(move[1]):
          h = (h[0], h[1]-1)
          t = update_tail(visited, t, h)
          visited[t] = True
          if debug: print_board(visited, t, h)

    print(f'Part 1 - {file}: {len(visited.keys())}')


def print_board_w_rope(visited, t, h):
  x_min = min([v[0] for v in list(visited.keys())+[h]+t])
  x_max = max([v[0] for v in list(visited.keys())+[h]+t])
  y_min = min([v[1] for v in list(visited.keys())+[h]+t])
  y_max = max([v[1] for v in list(visited.keys())+[h]+t])

  for y in range(y_max, y_min-1, -1):
    for x in range(x_min, x_max+1):
      if (x,y) == h:
        print('H', end='')
      elif (x,y) in t:
        for ti in range(9):
          if (x,y) == t[ti]:
            print(f'{ti+1}', end='')
            break
      elif (x, y) == (0, 0):
        print('s', end='')
      elif (x,y) in visited:
        print('*', end='')
      else:
        print('.', end='')
    print()
  print()


def move_rope(visited, t, h, debug=False):
  new_t = []
  k_prev = update_tail(visited, t[0], h)
  new_t.append(k_prev)
  for ki in range(1,9):
    k_prev = update_tail(visited, t[ki], k_prev)
    new_t.append(k_prev)
  t = new_t

  visited[t[-1]] = True
  if debug: print_board_w_rope(visited, t, h)
  return t

def solve2(file, debug=False):
    moves = parse(file, debug)

    h = (0, 0)
    t = [(0, 0) for _ in range(9)]
    visited = {}
    visited[t[-1]] = True


    for move in moves:
      if debug: print(move)
      if move[0] == 'R':
        for _ in range(move[1]):
          h = (h[0]+1, h[1])
          t = move_rope(visited, t, h, debug)
          visited[t[-1]] = True
      if move[0] == 'L':
        for _ in range(move[1]):
          h = (h[0]-1, h[1])
          t = move_rope(visited, t, h, debug)
          visited[t[-1]] = True
      if move[0] == 'U':
        for _ in range(move[1]):
          h = (h[0], h[1]+1)
          t = move_rope(visited, t, h, debug)
          visited[t[-1]] = True
      if move[0] == 'D':
        for _ in range(move[1]):
          h = (h[0], h[1]-1)
          t = move_rope(visited, t, h, debug)
          visited[t[-1]] = True

    if debug: print_board_w_rope(visited, t, h)
    print(f'Part 2 - {file}: {len(visited.keys())}')


solve1('./example.txt')
solve1('./input.txt')
 
solve2('./example.txt')
solve2('./big_example.txt')
solve2('./input.txt')