import math
x,y = map(int,input().split())
g=0
for i in range(x,0,-1):
    if x%i==0 and y%i==0:
        if g<i:
            g=i
print((x*y)//g)