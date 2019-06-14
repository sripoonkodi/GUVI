u=input()
v=0
for i in range(0,len(u)):
  if(u[i].isalpha()):
    v=v+1
    break
for i in range(0,len(u)):
  if(u[i].isdigit()):
    v=v+1
    break
if(v==2):
  print("Yes")
else:
  print("No")
