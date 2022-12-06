#!/usr/bin/env python3

def parse(file):
  lines = [line.strip() for line in open(file)]
  return lines


def solve(file, part):
    lines = parse(file)
    n = 4 if part == 1 else 14

    for line in lines:
      for i in range(0, len(line)-n):
        marker = line[i:i+n]
        if len(set(marker)) == n:
          print(f'Part {part} - {file}: {marker=} {i+n}')
          break

solve('./example.txt', 1)
solve('./input.txt', 1)

solve('./example.txt', 2)
solve('./input.txt', 2)