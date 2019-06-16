IN=int(input())
AB=list(map(int,input().split()))
BC=[]
for i in AB:
  if(AB.count(i)>1):
    BC.append(i)
  else:
    print(i)
