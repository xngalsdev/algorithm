N = input()
org = int(N)
num = org
cnt = 0

while True:
    a = num // 10
    b = num % 10
    c = (a + b) % 10
    num = (b * 10) + c
    cnt += 1
    if org == num:
        break
print(cnt)
