import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
a = [int(input()) for _ in range(n)]

print(' '.join(map(str, sorted(a))))