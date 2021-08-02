# https://www.acmicpc.net/problem/9012
cmd_cnt=int(input())
for i in range(cmd_cnt):
  target_list=list(input())
  sum=0
  for j in target_list:
    if j=='(':
      sum+=1
    elif j==')':
      sum-=1
    if sum<0:
      print('NO')
      break
  if sum>0:
    print('NO')
  elif sum==0:
    print('YES')
    