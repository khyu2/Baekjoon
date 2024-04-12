import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
dist = [*map(int, input().split())]
cost = [*map(int, input().split())]

ans, i = 0, 0
while i < n:
  j = i + 1
  total_dist = dist[i] if i != n - 1 else 0

  while j < n - 1 and cost[i] < cost[j]:
    total_dist += dist[j]
    j += 1
  
  ans += cost[i] * total_dist
  i = j

print(ans)
