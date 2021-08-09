# https://www.acmicpc.net/problem/1676
N=int(input())
count=0
while N>=5:
  count+=N//5
  N//=5
print(count)
