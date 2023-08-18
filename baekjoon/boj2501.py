N, K = map(int, input().split())
l = []
for a in range(1, N+1):
    if N % a == 0:
        l.append(a)

if len(l) < K:
    print(0)
else:
    print(l[K-1])
