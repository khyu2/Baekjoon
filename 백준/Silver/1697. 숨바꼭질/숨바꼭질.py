import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().rstrip().split())
q = deque()
a = [-1] * 100001

q.append(n)
a[n] = 0

while q:
    cur = q.popleft()
    for i in (cur - 1, cur + 1, cur * 2):
        if 0 <= i <= 100000 and a[i] == -1:
            a[i] = a[cur] + 1
            q.append(i)
            if i == k:
                break

print(a[k])