F=int(input())
LK=list(map(str,input().split()))
S=sorted(LK,key=len)
for i in range(len(S)-1):
    if len(S[i])==len(S[i+1]) and S[i]>S[i+1]:
        S[i],S[i+1]=S[i+1],S[i]
print(*S)
