#!/usr/bin/env python3

import pprint as pp


def parse(file, debug=False):
  lines = [line.strip() for line in open(file)]

  monkeys = []
  monkey = {}
  for line in lines:
    split = line.split()
    match split:
      case ['Monkey', n]:
        monkey = {}
        monkey['inspects'] = 0
      case ['Starting', *n]:
        monkey['items'] = [int(v.replace(',','')) for v in n[1:]]
      case ['Operation:', *n]:
        monkey['op'] = n[3:]
      case ['Test:', *n]:
        monkey['test'] = int(n[-1])
      case ['If', 'true:', *n]:
        monkey['true'] = int(n[-1])
      case ['If', 'false:', *n]:
        monkey['false'] = int(n[-1])
        monkeys.append(monkey)
    
  return monkeys


def worry_calc(op, worry: int):
  match op:
    case ['+', n]:
      if n == 'old':
        return worry + worry
      else:
        return worry + int(n)
    case ['*', n]:
      if n == 'old':
        return worry * worry
      else:
        return worry * int(n)
    case _:
      return 0


def solve1(file, debug=False):
  monkeys = parse(file, debug)

  if debug: pp.pprint(monkeys)
  if debug: print()

  per_monkey = False
  per_round = False

  for round in range(20):

    for mi, m in enumerate(monkeys):
      if per_monkey: print(f'Monkey {mi}:')
      m['inspects'] += len(m['items'])
      for i in m['items']:
        worry = worry_calc(m['op'], i)
        worry = worry // 3

        if per_monkey: print(f'\t{i=}')
        if per_monkey: print(f'\t\t{worry=}')

        if worry % m['test'] == 0:
          if per_monkey: print(f'\t\tIS  divisible by {m["test"]}')
          if per_monkey: print(f'\t\t{worry} thrown to {m["true"]}')

          monkeys[m['true']]['items'].append(worry)
        else:
          if per_monkey: print(f'\t\tNOT divisible by {m["test"]}')
          if per_monkey: print(f'\t\t{worry} thrown to {m["false"]}')

          monkeys[m['false']]['items'].append(worry)
      m['items'] = []

    if per_round: print(f'Round {round+1}')
    for mi, m in enumerate(monkeys):
      if per_round: print(f'\tMonkey {mi}: {", ".join([str(i) for i in m["items"]])}')

  print()
  for mi, m in enumerate(monkeys):
      print(f'Monkey {mi} inspected {m["inspects"]} times')

  print()
  inspects = [m['inspects'] for m in monkeys]
  inspects.sort()
  print(f'Top 2 inspects multiplied: {inspects[-1] * inspects[-2]}')
  print()


def solve2(file, debug=False):
  monkeys = parse(file, debug)

  if debug: pp.pprint(monkeys)
  if debug: print()

  per_monkey = False
  per_round = False

  total_prod = 1
  for m in monkeys:
    total_prod *= m['test']

  for round in range(10_000):

    for mi, m in enumerate(monkeys):
      if per_monkey: print(f'Monkey {mi}:')
      m['inspects'] += len(m['items'])
      for i in m['items']:
        worry = worry_calc(m['op'], i)
        # worry = worry // 3 - We are very worried now!

        if per_monkey: print(f'\t{i=}')
        if per_monkey: print(f'\t\t{worry=}')

        if worry % m['test'] == 0:
          if per_monkey: print(f'\t\tIS  divisible by {m["test"]}')
          if per_monkey: print(f'\t\t{worry} thrown to {m["true"]}')

          monkeys[m['true']]['items'].append(worry % total_prod)
        else:
          if per_monkey: print(f'\t\tNOT divisible by {m["test"]}')
          if per_monkey: print(f'\t\t{worry} thrown to {m["false"]}')

          monkeys[m['false']]['items'].append(worry % total_prod)
      m['items'] = []


    if round in [0, 20-1] + list(range(999, 10_000, 1000)):
      if per_round: print(f'Round {round+1}')
      for mi, m in enumerate(monkeys):
        if per_round: print(f'\tMonkey {mi}: {", ".join([str(i) for i in m["items"]])}')
        if per_round: print(f'Monkey {mi} inspected {m["inspects"]} times')
      if per_round: print()

  print()
  for mi, m in enumerate(monkeys):
      print(f'Monkey {mi} inspected {m["inspects"]} times')

  print()
  inspects = [m['inspects'] for m in monkeys]
  inspects.sort()
  print(f'Top 2 inspects multiplied: {inspects[-1] * inspects[-2]}')
  print()


solve1('./example.txt')
solve1('./input.txt')
 
solve2('./example.txt')
solve2('./input.txt')