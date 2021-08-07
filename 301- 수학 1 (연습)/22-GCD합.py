# https://www.acmicpc.net/problem/9613
from itertools import combinations
N=int(input())
def gcd(a,b):
	if b==0: return a
	else: return gcd(b, a%b)
for _ in range(N):
  lists=list(map(int,input().split()))
  lists=lists[1:]
  combi=combinations(lists,2)
  result=0
  for i in combi:
    result+=gcd(i[0],i[1])
  print(result)