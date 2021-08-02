# https://www.acmicpc.net/problem/9093
import sys
cmd_cnt=int(input())
result=''
for cnt in range(cmd_cnt):
  sentence=sys.stdin.readline().split()
  for idx in range(len(sentence)):
    word=sentence[idx]
    result+=word[::-1]+' '
  print(result)
  result=''
