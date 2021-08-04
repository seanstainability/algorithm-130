# https://www.acmicpc.net/problem/17413
S=input()
result=''
reversed=''
tag=False
for char in S:
  if tag:
    result=result+char
    if char=='>':
      tag=False
      reversed=''
  else:
    if char=="<":
      tag=True
      result=result+reversed+char
    elif char==' ':
      result=result+reversed+char
      reversed=''
    else:
      reversed=char+reversed
result=result+reversed
print(result)

