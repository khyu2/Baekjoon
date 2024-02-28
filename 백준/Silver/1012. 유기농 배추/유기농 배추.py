import sys
from collections import deque
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, n, m):
    q = deque()
    q.append((x, y))
    vis[x][y] = True

    while len(q):
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if not vis[nx][ny] and a[nx][ny]:
                q.append((nx, ny))
                vis[nx][ny] = True

tc = int(input().rstrip())

for _ in range(tc):
    a = [[0 for __ in range(51)] for j in range(51)]
    vis = [[False for __ in range(51)] for j in range(51)]

    m, n, k = map(int, input().rstrip().split())
    for i in range(k):
        x, y = map(int, input().rstrip().split())
        a[y][x] = 1

    cnt = 0
    for i in range(n):
        for j in range(m):
            if not vis[i][j] and a[i][j]:
                bfs(i, j, n, m)
                cnt += 1

    print(cnt)
