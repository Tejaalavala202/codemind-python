n=int(input())
c=0
a=0
for i in range(1,n+1,1):
    if n%i==0:
        c+=1
if c!=2:
    print('Not Mega Prime')
else:
    while n:
        r=n%10
        n=n//10
        c=0
        for i in range(1,r+1,1):
            if r%i==0:
                c+=1
        if c!=2:
          a+=1
    if a==0:
        print('Mega Prime')
    else:
        print('Not Mega Prime')
