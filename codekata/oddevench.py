d=input()
x=""
y=""
for i in range(0,len(d)):
  if (i%2!=0):
    x=x+d[i]
  else:
    y=y+d[i]
print(y,x)
