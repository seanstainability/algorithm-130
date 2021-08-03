# https://www.acmicpc.net/problem/10866
from sys import stdin
cmd_cnt=int(input())
deque=[]
for i in range(cmd_cnt):
  cmd=stdin.readline().split()
  if cmd[0]=="push_front":
    deque.insert(0,cmd[1])
  elif cmd[0]=="push_back":
    deque.append(cmd[1])
  elif cmd[0]=="pop_front":
    if not deque:
      print(-1)
    else:
      print(deque.pop(0))
  elif cmd[0]=="pop_back":
    if not deque:
      print(-1)
    else:
      print(deque.pop())    
  elif cmd[0]=="size":
    print(len(deque))
  elif cmd[0]=="empty":
    if not deque:
      print(1)
    else:
      print(0)
  elif cmd[0]=="front":
    if not deque:
      print(-1)
    else:
      print(deque[0])
  elif cmd[0]=="back":
    if not deque:
      print(-1)
    else:
      print(deque[-1])
