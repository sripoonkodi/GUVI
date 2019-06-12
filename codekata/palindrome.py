
n=int(input())
r=0
t=n
while(t!=0):
  d=t%10
  t=t/10
  r=r*10+d
if n==r:
  print("no")
else:
  print("yes")
