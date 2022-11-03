n=input()
c=0
for i in range(len(n)-1):
    for j in range(i+1,len(n)):
        if int(n[i])==int(n[j]):
            c+=1
if c==0:
    print('Unique Number')
else:
    print('Not Unique Number')