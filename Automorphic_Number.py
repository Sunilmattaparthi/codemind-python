n = input()
n1=str(int(n)*int(n))
ch=""
for i in range(len(n1)-len(n),len(n1)):
    ch=ch+n1[i]
if int(n)==int(ch):
    print('Automorphic Number')
else:
    print('Not an Automorphic Number')