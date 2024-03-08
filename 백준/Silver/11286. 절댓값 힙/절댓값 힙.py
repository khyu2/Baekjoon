import sys
import heapq
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
q = []

for _ in range(n):
  cmd = int(input())
  if cmd:
    if cmd > 0: heapq.heappush(q, [cmd, cmd])
    else: heapq.heappush(q, [abs(cmd), cmd])
  else:
    if len(q):
      top = heapq.heappop(q)
      if top[1] != top[0]: print(-top[0])
      else: print(top[0])
    else: print(0)
