import random

ch = 0
sp = []
even = []
for i in range(10):
    sp.append(random.randint(0,9))
    
print(sp)

even=list(sp)
even=[i for i in sp if  i%2 == 0]

for i in range (0,len(even)):
                ch = ch*10 + even[i]

print('парні числа',ch)
