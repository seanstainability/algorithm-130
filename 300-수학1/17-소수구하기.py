# https://www.acmicpc.net/problem/1978
M,N=map(int,input().split())
for i in range(M,N+1):
  is_sosu=True
  if i==1:
    continue
  for j in range(2,int(i**0.5)+1):
    if i%j==0:
      is_sosu=False
      break
  if is_sosu:
    print(i)