n = int(input())
x=0
y=1
f=0
l=[0,1]
while 1:
    f=x+y
    x=y
    y=f
    l.append(f)
    if l[len(l)-1]>n:
        break
e=len(l)-1
if (n-l[e-1])<(l[e]-n):
    print(l[e-1])
elif (n-l[e-1])>(l[e]-n):
    print(l[e])
else:
    print(l[e-1],l[e])

