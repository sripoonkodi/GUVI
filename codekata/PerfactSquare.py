a,b=map(int,input().split())
s=0
for i in range(2,max(a,b)):
  if i**2>=min(a,b) and i**2<=max(a,b):
    s+=1
print(s)
