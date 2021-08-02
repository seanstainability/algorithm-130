# https://www.acmicpc.net/problem/1874
n=int(input())
stack=[]
operator=[]
pointer=0
result=True
for i in range(n):
  target=int(input())
  while pointer<target:
    pointer+=1
    stack.append(pointer)
    operator.append('+')
  if stack[-1]==target:
    stack.pop()
    operator.append('-')
  else:
    result=False
if not result:
  print('NO')
else:
  for j in operator:
    print(j)


