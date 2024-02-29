import sys
from collections import defaultdict
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n = int(input().rstrip())
m = int(input().rstrip())
a = defaultdict(list)

for i in range(m):
    u, v = map(int, input().rstrip().split())
    a[u].append(v)
    a[v].append(u)

vis = [False] * 101
cnt = 0

def dfs(cur):
    if vis[cur]:
        return
    vis[cur] = True
    global cnt
    cnt += 1

    for nxt in a[cur]:
        if not vis[nxt]:
            dfs(nxt)

dfs(1)

print(cnt - 1)