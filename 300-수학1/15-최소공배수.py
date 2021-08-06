# https://www.acmicpc.net/problem/1934
from sys import stdin
T=int(input())
def gcd(x,y):
  while y!=0:
    x=x%y
    x,y=y,x
  return x
def lcm(x, y):
  return x*y//gcd(x,y)
for i in range(T):
  A,B=map(int,stdin.readline().strip().split())
  print(lcm(A,B))