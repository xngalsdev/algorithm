N=int(input())
peak=list(map(int,input().split()))
cnt=0
answer=0
high=0
for a in range (N):
    if peak[a]>high:
        high = peak[a]
        cnt=0
    else:
        cnt+=1
    if answer<cnt:
        answer=cnt
print(answer)