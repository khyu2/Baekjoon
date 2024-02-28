import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n = int(input().rstrip())

a = {1:0, 2:1}

def go(x):
    if x in a:
        return a[x]

    if x % 6 == 0:
        a[x] = min(go(x // 3), go(x // 2)) + 1
    elif x % 3 == 0:
        a[x] = min(go(x // 3), go(x - 1)) + 1
    elif x % 2 == 0:
        a[x] = min(go(x // 2), go(x - 1)) + 1
    else:
        a[x] = go(x - 1) + 1
    return a[x]

print(go(n))


