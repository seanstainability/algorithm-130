# https://www.acmicpc.net/problem/2609
A,B=map(int,input().split())
a,b=A,B
while b!=0:
  a=a%b
  a,b=b,a
print(a)
print(A*B//a)
# def gcd(a,b):
# 	if b==0: return a
# 	else: return gcd(b, a%b)
# print(gcd(A,B))
