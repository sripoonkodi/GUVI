A,B=map(int,input().split())
for i in range(1,100001):
  if (i%A==0 and i%B==0):
    print (i)
    break
