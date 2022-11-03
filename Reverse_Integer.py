n = int(input())
if n>0:
    s=str(n)
    s=s[::-1]
    print(int(s))
else:
    n=(-1)*n
    s=str(n)
    s=s[::-1]
    n=(-1)*int(s)
    print(n)
    