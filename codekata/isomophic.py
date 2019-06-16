s, S = map(str,input().split())
count = 0
for i in range(len(s)):
  if s.count(s[i]) == S.count(S[i]):
    count += 1
if count == len(s):
  print ("yes")
else:
  print ("no")
