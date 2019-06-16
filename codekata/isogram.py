b=input()
b=b.lower()
n=""
for J in b:
  if J not in n:
    n=n+J
if (b==n):
  print("Yes")
else:
  print("No")
