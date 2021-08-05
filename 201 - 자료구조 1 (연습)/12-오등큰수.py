# https://www.acmicpc.net/problem/17299
from sys import stdin
from collections import deque, Counter
N=int(input())
A=list(map(int,stdin.readline().strip().split()))
B=Counter(A)
oh_big=[-1]*N
stack=deque()
for i in range(N):
  while stack and (B[A[stack[-1]]]<B[A[i]]):
    oh_big[stack.pop()]=A[i]
  stack.append(i)
print(*oh_big)
