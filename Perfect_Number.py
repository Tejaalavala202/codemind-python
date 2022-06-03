n=int(input())
v=0
for i in range(1,n,1):
    if n%i==0:
        v+=i
if v==n:
    print('True')
else:
    print('False')