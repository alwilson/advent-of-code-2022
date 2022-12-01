#!/usr/bin/env python3

A=[sum([int(B) for B in L.split('\n')]) for L in open('i').read().split('\n\n')]
A.sort()
print(A[-1], sum(A[-3:]))