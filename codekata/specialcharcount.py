s =input()
k = 0
for i in range(len(s)):
  if s[i] in "!@#$%^&*_(){}[]:;,./?":
    k += 1
print (k)
