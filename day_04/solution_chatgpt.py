#!/usr/bin/env python3

def parse(file):
    lines = [line.strip() for line in open(file)]
    return lines


def solve(file):
    lines = parse(file)

    # Parse the input to obtain a list of pairs of ranges
    range_pairs = []
    for line in lines:
      # Each line represents a pair of ranges
      # Split the line by ',' to obtain the individual ranges
      range1, range2 = line.split(',')
      # Split each range by '-' to obtain the start and end of the range
      start1, end1 = map(int, range1.split('-'))
      start2, end2 = map(int, range2.split('-'))
      # Add the pair of ranges to the list of pairs
      range_pairs.append(((start1, end1), (start2, end2)))

    # Keep track of the number of pairs where one range fully contains the other
    num_contained_pairs = 0

    # Iterate through the list of pairs of ranges
    for (start1, end1), (start2, end2) in range_pairs:
      # If one range is fully contained by the other, increment the counter
      if (start1 >= start2 and end1 <= end2) or (start2 >= start1 and end2 <= end1):
        num_contained_pairs += 1

    # Return the number of pairs where one range fully contains the other
    print(num_contained_pairs)


    # Parse the input to obtain a list of pairs of ranges
    range_pairs = []
    for line in lines:
      # Each line represents a pair of ranges
      # Split the line by ',' to obtain the individual ranges
      range1, range2 = line.split(',')
      # Split each range by '-' to obtain the start and end of the range
      start1, end1 = map(int, range1.split('-'))
      start2, end2 = map(int, range2.split('-'))
      # Add the pair of ranges to the list of pairs
      range_pairs.append(((start1, end1), (start2, end2)))

    # Keep track of the number of pairs where the ranges overlap
    num_overlapping_pairs = 0

    # Iterate through the list of pairs of ranges
    for (start1, end1), (start2, end2) in range_pairs:
      # If the ranges overlap, increment the counter
      if (start1 <= end2 and end1 >= start2) or (start2 <= end1 and end2 >= start1):
        num_overlapping_pairs += 1

    # Return the number of pairs where the ranges overlap
    print(num_overlapping_pairs)


solve('./example.txt')
solve('./input.txt')