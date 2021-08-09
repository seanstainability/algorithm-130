# https://www.acmicpc.net/problem/2089
N=int(input())
answer=''
if not N:
    print('0')
    exit()
else:
  while N:
    if N % -2:
        answer='1'+answer
        N=N//-2+1
    else:
        answer='0'+answer
        N=N//-2
print(answer)