# https://www.acmicpc.net/problem/17298
from collections import deque
N=int(input())
A=list(map(int,input().split()))
oh_big=[-1]*N
stack=deque()
for i in range(N):
  while stack and (stack[-1][0]<A[i]):
    tmp,idx=stack.pop()
    oh_big[idx]=A[i]
  stack.append([A[i],i])
print(*oh_big)
