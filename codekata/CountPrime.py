MN,NM = map(int,input().split())
c= 0
for i in range(MN,NM+1):
  if i > 1:
    for h in range(2,i):
      if i % h == 0:
        break
    else:
      c+= 1
print(c)
