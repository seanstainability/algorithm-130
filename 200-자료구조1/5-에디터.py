# https://www.acmicpc.net/problem/1406
from sys import stdin
s=input()
s_list=list(s)
temp_list=[]
cmd_cnt=int(input())
for cmd in range(cmd_cnt):
  cmd=stdin.readline().split()
  cmd_str=cmd[0]
  if cmd_str=='L':
    if s_list:
      temp_list.append(s_list.pop())
    else: continue
  elif cmd_str=='D':
    if temp_list:
      s_list.append(temp_list.pop())
    else: continue
  elif cmd_str=='B':
    if s_list:
      s_list.pop()
    else: continue
  elif cmd_str=='P':
    s_list.append(cmd[1])
print("".join(s_list+list(reversed(temp_list))))