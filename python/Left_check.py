a = int(input())
b = int(input())
if a%b == 0:
    print("%d ділиться на %d" % (a,b))
else:
    print("%d не ділиться на %d" % (a,b))
    print("Залишок: %d" % (a%b))
