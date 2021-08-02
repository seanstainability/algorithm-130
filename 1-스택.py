# https://www.acmicpc.net/problem/10828
import sys
cmd_cnt=int(sys.stdin.readline())
stack=[]
for i in range(cmd_cnt):
  cmd=sys.stdin.readline().split()
  cmd_str=cmd[0]
  if cmd_str=='push':
    stack.append(cmd[1])
  elif cmd_str=='pop':
    if not stack:
      print(-1)
    else:
      print(stack.pop())
  elif cmd_str=='size':
    print(len(stack))
  elif cmd_str=='empty':
    if not stack:
      print(1)
    else:
      print(0)
  elif cmd_str=='top':
    if not stack:
      print(-1)
    else:
      print(stack[len(stack)-1])
