A=list(input().split())
c=0
Q= list(A[0])
W= list(A[1])
for i in range(0,min(len(Q),len(W))):
    if Q[i]!=W[i]: 
      c=c+1
c=c+(len(Q)-len(W))
if c==int(A[2]):
  print("yes")
else:
  print("no")
