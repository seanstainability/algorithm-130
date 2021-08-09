# https://www.acmicpc.net/problem/2004
N,M=map(int,input().split())
def count_num(n,num):
  count=0
  while n>=num:
    count+=n//num
    n//=num
  return count
count_five=count_num(N,5)-count_num(M,5)-count_num(N-M,5)
count_two=count_num(N,2)-count_num(M,2)-count_num(N-M,2)
print(min(count_five,count_two))