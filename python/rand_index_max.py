import random

sp = []
for i in range(11):
    k=random.randint(0,100)
    sp.append(k)

print(sp)

a=max (sp)
print('max elem',a)

a=sp[0]
n=0
for i in range (1,len(sp)):
    if a<sp[i]:
       a=sp[i]
       n=i
print ('index max elem',n)
