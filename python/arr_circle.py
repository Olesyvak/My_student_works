from turtle import*
from random import*
a=['red','yellow','green','blue']
x=randint(5,50)

speed(300)
for n in range(1):
    begin_fill()
    color(a[n%4])
    end_fill()
for i in range(2):
    for x in range(1,201,2):
        up()
        goto(x*2,0)
        down()
        circle(x)
    left(180)
    goto(0,0)
    for n in range(2):
        begin_fill()
        color(a[n%4])
        end_fill()
for n in range(3):
    begin_fill()
    color(a[n%4])
    end_fill()
for i in range(2):
    for x in range(1,201,2):
        up()
        goto(x*-2,0)
        down()
        circle(x)
    left(180)
    goto(0,0)
    for n in range(4):
        begin_fill()
        color(a[n%4])
        end_fill()
