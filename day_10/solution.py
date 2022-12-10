#!/usr/bin/env python3

import pprint as pp

def parse(file, debug=False):
  lines = [line.strip() for line in open(file)]
  return lines

def calc_sig_str(cycle, x, debug=False):
    record_cycles = [20,60,100,140,180,220]
    if cycle in record_cycles:
      if debug: print(cycle, x)
      return cycle * x
    return 0 

def solve1(file, debug=False):
    lines = parse(file, debug)

    cycle = 1
    x = 1
    sig_str = 0
    for line in lines:
      split = line.split()
      match split:
        case ['noop']:
          cycle += 1
          sig_str += calc_sig_str(cycle, x, debug)
        case ['addx', num]:
          cycle += 1
          sig_str += calc_sig_str(cycle, x, debug)
          x += int(num)
          cycle += 1
          sig_str += calc_sig_str(cycle, x, debug)
    print(f'Part 1 - {file}: {sig_str}')

def draw_crt(cycle, x):
  if cycle % 40 == 0:
    print()
  if cycle >= 240:
    return
  pos = cycle % 40
  pixel = '#' if x in [pos-1, pos, pos+1] else '.'
  print(pixel, end='')

def solve2(file, debug=False):
    lines = parse(file, debug)

    cycle = 0
    x = 1
    draw_crt(cycle, x)
    for line in lines:
      split = line.split()
      match split:
        case ['noop']:
          cycle += 1
          draw_crt(cycle, x)
        case ['addx', num]:
          cycle += 1
          draw_crt(cycle, x)
          x += int(num)
          cycle += 1
          draw_crt(cycle, x)
    print(f'Part 2 - {file} {cycle}')


solve1('./example.txt')
solve1('./input.txt')
 
solve2('./example.txt')
solve2('./input.txt')