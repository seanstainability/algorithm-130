# https://www.acmicpc.net/problem/6588
from sys import stdin
N=1000000
check=[False, False] + [True] * N
for i in range(2,int(N**0.5)+1):
  if check[i]==True:
    for j in range(i*2,N+1,i):
      check[j]=False
while True:
  num = int(stdin.readline().strip())
  if num==0: break
  for i in range(3,num):
    if check[i]==True:
      if check[num-i]==True:
        print("%d = %d + %d"%(num,i,num-i))
        break
  else:
    print("Goldbach's conjecture is wrong.")