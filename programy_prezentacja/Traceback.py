import traceback

def Error1():
    raise TypeError("Error1")

def Error2():
    Error1()
    raise ArithmeticError("Error2")

try:
    x = 5.66
    y = "pięćkropkasześćsześć"
    x + y
except TypeError as e:
    print("Wiadomość dla danego błędu: ", e)
    traceback.print_exc()
    pass
print("Halo halo tu Londyn")

try:
    Error2()
except TypeError as e:
    tb = e.__traceback__

    lista = traceback.extract_tb(tb)

    print(lista)


def funkcja1():
    print("funkcja1")
    traceback.print_stack()

def funkcja2():
    funkcja1()

funkcja2()





















