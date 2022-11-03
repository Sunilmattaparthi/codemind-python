n = int(input())
s=0
for i in range(1,n):
    if n%i==0:
        s+=i
n1=s
s=0
for i in range(1,n1):
    if n1%i==0:
        s+=i
if s==n:
    print('Amicable')
else:
    print('Not Amicable')