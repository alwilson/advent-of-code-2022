#!/usr/bin/env python3

import pprint as pp

# Parse ls/cd commands and output into a 'file system' of dictionaries.
# 'this_dir_size' is a special key tracking directory size
def parse(file, debug=False):
  fs = {}
  path_s = [fs]
  cwd = fs
  lines = [line.strip() for line in open(file)]
  for line in lines:
    split = line.split()
    if debug: print(split)

    match split:
      case ['$', *rest]:
        if debug: print('\tfound command', rest)
        match rest:
          case ['cd', path]:
            if path == '..':
              cwd = path_s.pop()
            else:
              path_s.append(cwd)
              if path not in cwd:
                cwd[path] = {}
              cwd = cwd[path]
              cwd['this_dir_size'] = 0

      # NOTE: The cd command tells us all we need to know about directories
      #       If we don't visit a directory we must not care what's inside
      case ['dir', dir_name]:
        if debug: print('\tfound dir named: ', dir_name)
        pass

      case [size, file_name]:
        if debug: print('\tfound file named ', file_name)
        cwd[file_name] = int(size)
        cwd['this_dir_size'] += int(size)

      case _:
        print('\tUnknown command or output!')
        exit(-1)

  return fs

# Update all directories with the sum of their child directories
def update_sizes(root):
    for key, val in root.items():
      if type(val) is dict:
        root['this_dir_size'] += update_sizes(root[key])

    this_size = root['this_dir_size']
    return this_size

# Sum all directories that are above the size requirement
def part1(root):
    sum = 0
    for key, val in root.items():
      if type(val) is dict:
        sum += part1(root[key])

    this_size = root['this_dir_size']
    if this_size <= 100000:
      return sum + this_size
    else:
      return sum + 0

# Find all dir sizes that meet the min size requirement
def part2(root, min_size):
    sizes = []
    for key, val in root.items():
      if type(val) is dict:
        sizes += part2(root[key], min_size)

    this_size = root['this_dir_size']
    if this_size >= min_size:
      return sizes + [this_size]
    else:
      return sizes

def solve(file, debug=False):
    fs = parse(file, debug)

    root = fs['/']
    update_sizes(root)
    
    if debug: pp.pprint(root)
    part1_sum = part1(root)
    print(f'Part 1 - {file}: {part1_sum}')

    avail = 70000000 - root['this_dir_size']
    needed = 30000000 - avail
    sizes = part2(root, needed)
    print(f'Part 2 - {file}: {min(sizes)} ({len(sizes)=})')


# solve('./example.txt', True)
solve('./example.txt')
solve('./input.txt')