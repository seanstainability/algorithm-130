# https://www.acmicpc.net/problem/1158
n,k=map(int,input().split())
target=[i for i in range(1,n+1)]
result=[]
seqNo=k-1
while target:
  if seqNo>=len(target):
    seqNo=seqNo%len(target)
  else:
    result.append(str(target.pop(seqNo)))
    seqNo+=k-1
print("<",", ".join(result),">",sep="")
  
