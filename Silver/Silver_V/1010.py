from math import comb
import sys

T = int(input())

for i in range(T):
    W, E = map(int, sys.stdin.readline().rstrip().split())
    print(comb(E, W))

