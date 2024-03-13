import heapq
import sys
input = lambda: sys.stdin.readline().rstrip()

q = []
n = int(input())

for i in range(n):
  for x in list(map(int, input().split())):
    if len(q) > n: heapq.heappop(q)
    heapq.heappush(q, x)

if len(q) > 1: heapq.heappop(q)
print(q[0])