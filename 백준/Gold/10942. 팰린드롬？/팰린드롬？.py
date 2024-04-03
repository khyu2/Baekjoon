import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
a = [*map(int, input().split())]
d = [[-1 for _ in range(n+10)] for _ in range(n+10)]

def go(s, e):
  if d[s][e] != -1: return d[s][e]
  if s > e: return 1
  d[s][e] = go(s + 1, e - 1) if a[s] == a[e] else 0
  return d[s][e]

for i in range(int(input())):
  x, y = map(int, input().split())
  print(go(x - 1, y - 1))
# print(d)