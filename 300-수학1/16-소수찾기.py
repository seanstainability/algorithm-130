# https://www.acmicpc.net/problem/1978
N=int(input())
num_list=list(map(int,input().split()))
cnt=0
for i in num_list:
  is_sosu=True
  if i==1:
    continue
  for j in range(2, i):
    if i%j==0:
      is_sosu=False
      break
  if is_sosu:
    cnt+=1
print(cnt)