v=int(input())
k=int(input())
a=0
for i in range(1,(v//2)+1,1):
    if(v%i==0):
        a+=i
b=0
for i in range(1,(k//2)+1,1):
    if(k%i==0):
        b+=i
if(a==k and b==v):
    print('Amicable')
else:
    print('Not Amicable')