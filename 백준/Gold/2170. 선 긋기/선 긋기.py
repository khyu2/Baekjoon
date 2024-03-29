import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
a = [[*map(int, input().split())] for _ in range(n)]
a.sort()

line = 0
start = a[0][0]
end = a[0][1]

for i in range(1, n):
  if a[i][0] > end:
    line += end - start
    start = a[i][0]
    end = a[i][1]
  elif a[i][1] > end:
    end = a[i][1]
  # print('line:', line, start, end)
line += end - start

print(line)