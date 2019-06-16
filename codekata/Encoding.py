J=input()
K=''
for i in J:
  if i=='X':
    K+=("A")
  elif i=='x':
    K+=("a")
  elif i=='Y':
    K+=("B")
  elif i=='y':
    K+=("b")
  elif i=='Z':
    K+=("C")
  elif i=='z':
    K+=("c")
  else:
    K+=chr(ord(i)+3)
print(K)
