a = raw_input("A:\n")

b = raw_input("B:\n")

x = int (a)

y = int (b)

def is_divisible(x,y):
    if x % y == 0:
        return True
    else:
        return False

if is_divisible(x,y):
    print 'x is divisible by y'
