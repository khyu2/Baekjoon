import sys
import heapq
input = sys.stdin.readline

n = int(input().rstrip())
q = []
heapq.heapify(q)

for i in range(n):
    x = int(input().rstrip())
    if x:
        heapq.heappush(q, x)
    else:
        print(heapq.heappop(q) if len(q) else 0)
