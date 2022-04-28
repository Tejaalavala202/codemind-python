n=int(input())
temp=n
pro=1
sum=0
while(n):
    r=n%10
    sum=sum+r
    pro=pro*r
    n=n//10
if(sum==pro):
    print("Spy Number")
else:
    print("Not Spy Number")