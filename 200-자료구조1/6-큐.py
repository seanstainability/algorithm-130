# https://www.acmicpc.net/problem/10845
from sys import stdin
cmd_cnt=int(input())
queue=[]
for i in range(cmd_cnt):
  cmd=stdin.readline().split()
  cmd_str=cmd[0]
  if cmd_str=='push':
    queue.append(cmd[1])
  elif cmd_str=='pop':
    if not queue:
      print(-1)
    else:
      print(queue.pop(0))
  elif cmd_str=='size':
    print(len(queue))
  elif cmd_str=='empty':
    if not queue:
      print(1)
    else:
      print(0)
  elif cmd_str=='front':
    if not queue:
      print(-1)
    else:
      print(queue[0])
  elif cmd_str=='back':
    if not queue:
      print(-1)
    else:
      print(queue[-1])
      