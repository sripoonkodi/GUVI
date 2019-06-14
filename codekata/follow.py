m=[int(x) for x in input().split()]
n=[int(x) for x in input().split()]
e=0
for i in n:
  if (i==n[1]):
    e=1
if (e==1):
  print("yes")
else:
  print("no")
