n=int(input())
t=0
arr=list(map(int,input().split()))
for i in arr:
    if i%2!=0:
        t=t+1
if t<=2:
    print("YES")
else:
    print("NO")