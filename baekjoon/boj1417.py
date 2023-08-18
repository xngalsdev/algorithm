N=int(input())
da=int(input())
na=[]
count=0
for a in range(N-1):
    na.append(int(input()))
na.sort(reverse=True)
if N==1:
    print(0)
else:
    while na[0]>=da:
        da+=1
        na[0]-=1
        count+=1
        na.sort(reverse=True)
    print(count)