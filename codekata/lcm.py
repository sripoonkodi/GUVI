import math
L,M=input().split()
L=int(L)
M=int(M)
N=math.gcd(L,M)
print((L*M)//N)
