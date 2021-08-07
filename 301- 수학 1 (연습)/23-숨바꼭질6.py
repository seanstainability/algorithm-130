# https://www.acmicpc.net/problem/17087
N,S=map(int,input().split())
A=list(map(int,input().split()))
def gcd(a,b):
	if b==0: return a
	else: return gcd(b, a%b)
diff=list(set(abs(A[i]-S) for i in range(N)))
print(diff)
d=min(diff)
for i in range(len(diff)):
  d=gcd(diff[i],d)
print(d)