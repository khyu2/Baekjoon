import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n, m = map(int, input().split())

a = set([input() for i in range(n)])
b = set([input() for i in range(m)])

c = list(a & b)
print(len(c))

for i in sorted(c):
	print(i, end ="")
