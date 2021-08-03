# https://www.acmicpc.net/problem/9012
import sys
cmd_cnt=int(input())
for cnt in range(cmd_cnt):
  target_list=list(sys.stdin.readline().strip())
  sum=0
  for i in target_list:
    if i=='(':
      sum+=1
    elif i==')':
      sum-=1
    if sum<0:
      print('NO')
      break
  if sum>0:
    print('NO')
  elif sum==0:
    print('YES')
    