#Zadanie 6
#Idziesz z kolegą przez pole (pole że pole) i znaleźliście węża.
#Mówi że normalnie nie przepuszcza GRUP ludzi, ale dla was może zrobić WYJĄTEK
#Przepuści was, jeżeli powiecie jego imię
#Na ogół nie rozmawiacie z wężami, ale ten konkretny wydaje się spoko ziomkiem, dlatego robicie dla niego WYJĄTEK, i próbujecie odgadnąć jego imie
#Po namyśle jednak stwierdzacie czy nie było by go łatwiej pare razy wprowadzić w BŁĄD....

#Zrób dwie grupy wyjątków tak, żeby poniższe instrukcje except* wypisały słowo python


grupa1 = ...

grupa2 = ...

try:
    raise ExceptionGroup("Główny Korzeń", [grupa1, grupa2])
except* ValueError as e:
    if len(e.exceptions) == 1 and len(e.exceptions[0].exceptions) == 1:
        print("p", end="")

except* TypeError as e:
    if e.exceptions[0].exceptions[0].args[0] == "wąż":
        print("y", end="")

except* KeyError as e:
    if len(e.exceptions) == 2:
        print("t", end="")

except* IndexError as e:
    if len(e.exceptions) == 1 and len(e.exceptions[0].exceptions) == 2:
        print("h", end="")

except* ZeroDivisionError:
    print("o", end="")

except* AttributeError:
    print("n", end="\n")