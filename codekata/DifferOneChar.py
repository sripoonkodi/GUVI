MN,NM = map(str,input().split())
c= 0
for i in range(len(MN)):
  if (MN[i]!=NM[i]):
    c+= 1
if c==1:
  print("yes")
else:
  print("no")


