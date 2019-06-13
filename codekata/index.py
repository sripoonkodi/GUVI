t=int(input())
a =list(map(int,input().split()))
for i in range(t):
  print(a[i],a.index(a[i]))
