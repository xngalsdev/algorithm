import sys

N = int(sys.stdin.readline())
pc = print(sum(int(sys.stdin.readline()) for _ in range(N))-(N-1))