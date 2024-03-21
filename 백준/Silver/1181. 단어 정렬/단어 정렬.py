import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
a = list(input() for _ in range(n))

print(*sorted(set(a), key=lambda x: (len(x), x)))