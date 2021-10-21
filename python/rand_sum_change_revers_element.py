import random

b = []
d = []
e = []
f = []
i = 0

while i <10:
        b.append(random.randint(-10,10))
        i +=1
print(b)
c=sum(b)
print("Сума елементів =",c)

d=[i for i in b if i> 0]
print("Додатні елементи =",d)

e=[i*-1 for i in b]
print("Зміна знаку елементів =",e)

f=list(b)
f.reverse()
print("Зворотній порядок =",f)


