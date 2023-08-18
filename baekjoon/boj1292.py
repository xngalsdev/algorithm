A,B=map(int,input().split())
arr=[0]
for i in range(1,47):
    for j in range(i):
        arr.append(i)
print(sum(arr[A:B+1]))