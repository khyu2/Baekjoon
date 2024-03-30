stick = [64]

x = int(input())
while sum(stick) > x:
  stick.sort(reverse=True)
  half = stick.pop() >> 1

  stick.append(half)
  if sum(stick) < x:
    stick.append(half)

print(len(stick))
