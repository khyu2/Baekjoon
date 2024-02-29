import sys
input = sys.stdin.readline

n = int(input().rstrip())
a = set()

for _ in range(n):
  s = input().rstrip()
  
  if "add" in s:
    a.add(s[4:])
  elif "remove" in s:
    a.discard(s[7:])
  elif "check" in s:
    print(1 if s[6:] in a else 0)
  elif "toggle" in s:
    if s[7:] in a:
      a.remove(s[7:])
    else:
      a.add(s[7:])
  elif "all" == s:
    a = set([str(i) for i in range(1, 21)])
  else:
    a = set()
