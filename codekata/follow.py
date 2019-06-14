m=[int(x) for x in input().split()]
n=[int(x) for x in input().split()]
R=0
for i in n:
  if (i==m[1]):
    R=1
if (R==1):
  print("yes")
else:
  print("no")
