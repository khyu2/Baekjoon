import sys
input = sys.stdin.readline

n = int(input().rstrip())
a = list(map(int, input().rstrip().split()))

a.sort()

ans = 0
for i in range(n):
    ans += sum(a[:i + 1])

print(ans)