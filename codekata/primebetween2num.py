a,b=(input().split())
a=int(a)
b=int(b)
for n in range(a+1,b):
  if n>1:
    for i in range (2,n):
      if (n%i==0):
        break
    else:
      print(n,end=" ")

  
