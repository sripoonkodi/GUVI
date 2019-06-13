a,b=(input().split())
a=int(a)
b=int(b)
for n in range (a,b):
  r=0
  t=n
  while(t>0):
    d=t%10
    r+=d**3
    t//=10
  if n==r:
    print(n,end=" ")
