import math
def checkPronic (x) :
    i = 0
    while ( i <= (int)(math.sqrt(x)) ) :
        if ( x == i * (i + 1)) :
            return True
        i = i + 1
    return False
n = int(input())
if checkPronic(n):
    print('YES')
else:
    print('NO')