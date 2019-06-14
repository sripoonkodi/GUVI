L,C=map(int,input().split())
A=[]
for x in input().split():
  A.append(int(x))
d=A.count(C)
if(d>0):
  print("yes")
else:
  print("no")
