# https://www.acmicpc.net/problem/1874
import sys
n=int(input())
stack=[]
operator=[]
pointer=0
result=True
for i in range(n):
  target_num=int(sys.stdin.readline().strip())
  while pointer<target_num:
    pointer+=1
    stack.append(pointer)
    operator.append('+')
  if stack[-1]==target_num:
    stack.pop()
    operator.append('-')
  else:
    result=False
if not result:
  print('NO')
else:
  for j in operator:
    print(j)


