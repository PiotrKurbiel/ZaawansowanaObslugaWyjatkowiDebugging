import pdb
def funkcjadodatnicza(x,y):
    if x == x:
        if y == y:
            y = y + 2*(x-5**2)/64 + 100/128 + (31*x)/32
            return y
x = 6;
y = 4;
y = funkcjadodatnicza(x,y)
pdb.set_trace()
print(y)
raise ArithmeticError()