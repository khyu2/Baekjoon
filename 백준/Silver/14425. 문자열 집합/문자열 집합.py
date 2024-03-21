import sys
input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())
a = set()

count = 0
for i in range(n):
  a.add(input())
for i in range(m):
  if input() in a:
    count += 1

print(count)