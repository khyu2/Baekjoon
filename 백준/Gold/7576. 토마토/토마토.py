import sys
from collections import deque
input = sys.stdin.readline

dx = [1,-1,0,0]
dy = [0,0,1,-1]

m, n = map(int, input().rstrip().split())
a = [[0 for _ in range(m)] for _ in range(n)]
vis = [[0 for _ in range(m)] for _ in range(n)]
q = deque()

for i in range(n):
    for j, x in enumerate(map(int, input().rstrip().split())):
        a[i][j] = x
        if x == 1:
            q.append((i, j))

def ripeCheck(): # 익지 않은 토마토가 있는지 확인
    for i in range(n):
        for j in range(m):
            if a[i][j] == 0 and not vis[i][j]:
                return False
    return True

def bfs():
    ret = 0

    while q:
        cur = q.popleft()

        for i in range(4):
            nx = cur[0] + dx[i]
            ny = cur[1] + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if a[nx][ny] == 0 and not vis[nx][ny]:
                vis[nx][ny] = vis[cur[0]][cur[1]] + 1
                ret = max(ret, vis[nx][ny])
                q.append((nx, ny))

    return ret if ripeCheck() else -1

print(bfs())