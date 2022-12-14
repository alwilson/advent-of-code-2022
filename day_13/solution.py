#!/usr/bin/env python3

import pprint as pp
from functools import cmp_to_key


def parse(file, debug=False):
  lines = [line.strip() for line in open(file)]

  pairs = []
  pair = []
  for line in lines:
    if len(line) > 0:
      pair.append(eval(line))
      if len(pair) == 2:
        pairs.append(pair)
        pair = []

  return pairs


def parse_p2(file, debug=False):
  lines = [line.strip() for line in open(file)]

  pkts = []
  for line in lines:
    if len(line) > 0:
      pkts.append(line)

  pkts.append('[[2]]')
  pkts.append('[[6]]')

  return pkts


# NOTE This was exploring other ways of returning comparison values other than True/False
def compair_p2(p0, p1) -> int:
  p0 = eval(p0)
  p1 = eval(p1)
  return compair_num([p0, p1], 0, False)


# NOTE This was exploring other ways of returning comparison values other than True/False
def compair_num(p, level, debug=False) -> int:
  p0 = p[0]
  p1 = p[1]
  if debug: print('\t'*level, p0)
  if debug: print('\t'*level, p1)

  if type(p0) is int and type(p1) is int:
    if p0 > p1:
      if debug: print('\t'*level, 'Lower integer didn\'t come first')
      return -1
    elif p0 < p1:
      if debug: print('\t'*level, 'Lower integer came first, all input correct')
      return 1
    else:
      return 0

  elif type(p0) is list and type(p1) is int:
    return compair_num([p0, [p1]], level+1, debug)

  elif type(p0) is int and type(p1) is list:
    return compair_num([[p0], p1], level+1, debug)

  elif type(p0) is list and type(p1) is list:
    for i0, i1 in zip(p0, p1):
      ret = compair_num([i0, i1], level+1, debug)
      if ret in [-1, 1]:
        return ret
    
    if len(p1) < len(p0):
      return -1
    elif len(p1) > len(p0):
      return 1
    else:
      return 0
  else:
    return 0


def compair_p1(p0, p1) -> int:
  p0 = eval(p0)
  p1 = eval(p1)
  ret, _ = compair([p0, p1], 0, False)
  return 1 if ret else -1


def compair(p, level, debug=False):
  p0 = p[0]
  p1 = p[1]
  if debug: print('\t'*level, p0)
  if debug: print('\t'*level, p1)
  
  while len(p0) > 0:
    if len(p1) == 0:
      if debug: print('\t'*level, '2nd pair not long enough')
      return False, 0

    i0 = p0.pop(0)
    i1 = p1.pop(0)

    if type(i0) is int and type(i1) is int:
      if i0 > i1:
        if debug: print('\t'*level, 'Lower integer didn\'t come first')
        return False, -1
      
      if i0 < i1:
        if debug: print('\t'*level, 'Lower integer came first, all input correct')
        return True, 1

    if type(i0) is list and type(i1) is int:
      ret, left = compair([i0, [i1]], level+1, debug)
      if not ret:
        return False, 0
      if left > 0:
        return True, left

    if type(i0) is int and type(i1) is list:
      ret, left = compair([[i0], i1], level+1, debug)
      if not ret:
        return False, 0
      if left > 0:
        return True, left

    if type(i0) is list and type(i1) is list:
      ret, left = compair([i0, i1], level+1, debug)
      if not ret:
        return False, 0
      if left > 0:
        return True, left

  if len(p1) > 0:
    if debug: print('\t'*level, 'Exit early, left side ran out first!')
  return True, len(p1)


def solve1(file, debug=False):
  pairs = parse(file, debug)

  idx_sum = 0
  for pi, p in enumerate(pairs):
    ret, _ = compair(p, 0)
    if ret:
      idx_sum += pi+1
      if debug: print(f'{pi+1} Passed!')

  print(f'Part 1 - {file}: {idx_sum=}')


def solve2(file, debug=False):
  pkts = parse_p2(file, debug)

  pkts = sorted(pkts, key=cmp_to_key(compair_p1))

  pkts = pkts[::-1]
  if debug: pp.pprint(pkts)

  i2 = pkts.index('[[2]]')+1
  i6 = pkts.index('[[6]]')+1
  print(f'Part 2 - {file}: {i2*i6=}')


solve1('./example.txt')
solve1('./input.txt')
 
solve2('./example.txt')
solve2('./input.txt')