# https://www.acmicpc.net/problem/10799
S=input()
prev=''
total=0
stack=[]
for i in S:
  if i=='(':
    stack.append(i)
  else:
    if prev=='(':
      stack.pop()
      total+=len(stack) # 레이저에 의해 잘림
    else:
      stack.pop()
      total+=1 # 쇠막대기 끄트머리
  prev=i
print(total)
