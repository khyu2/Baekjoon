import sys
import heapq
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
q = []

for _ in range(n):
  cmd = int(input())
  if cmd == 0:
    if len(q) == 0: print(0)
    else: print(-heapq.heappop(q))
  else:
    heapq.heappush(q, -cmd)

