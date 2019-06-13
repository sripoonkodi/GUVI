n=int(input())
r=0
t=n
while(t>0):
  d=t%10
  r+=d**3
  t//=10
  
if n==r:
  print("yes")
else:
  print("no")
