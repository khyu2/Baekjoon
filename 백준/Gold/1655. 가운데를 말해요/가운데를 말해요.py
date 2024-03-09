import sys
import heapq
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
max_heap = []
min_heap = []

for i in range(n):
  x = int(input())

  if len(max_heap) == 0:
    heapq.heappush(max_heap, -x)
  
  else:
    heapq.heappush(max_heap, -x)
    heapq.heappush(min_heap, -heapq.heappop(max_heap))

    if len(min_heap) > len(max_heap):
      heapq.heappush(max_heap, -heapq.heappop(min_heap))

  print(-max_heap[0])