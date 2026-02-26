a=int(input())
b=list(map(int, input().split()))
cnt=0
for x in b:
    if x>a:
        cnt += 1
       

print(cnt)
