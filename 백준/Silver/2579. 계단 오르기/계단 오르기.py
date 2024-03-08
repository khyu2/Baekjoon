n = int(input())
a = [int(input()) for _ in range(n)]
d = [0] * (n + 1)
a = [0] + a

if n == 1:
	print(a[1])
	exit(0)
 
d[1] = a[1]
d[2] = a[2] + a[1]
# d[3] = a[3] + max(a[1], a[2])
 
for i in range(3, n + 1):
	d[i] = max(d[i-2], d[i-3] + a[i-1]) + a[i]
 
print(d[n])