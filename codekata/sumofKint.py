w,t=(input().split())
w=int(w)
t=int(t)
s=0
arr = [int(x) for x in input().split()]
for i in range (0,t):
  s=s+arr[i]
print(s)
