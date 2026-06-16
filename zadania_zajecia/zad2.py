#Zadanie 2
#Poniżej jest przykładowy program który sprawdza jak bardzo losowe są wartości funkcji random.randint
#Do programu zostały dodane 3 breakpointy (pdb.set_trace()) W momencie którym odpalisz program, wejdziesz do Pdb (Python Debugger)
#Pobaw się pythonowym debugerem, możesz skorzystać z przykładowych poleceń poniżej.
#Spróbuj naprawić program (nie jest to ciężkie, po prostu zobacz jak działa debugger)

#break - dodajemy breakpointy w miejscu w którym chcemy - dodaj breakpoint do programu w linijce 43: break zad3.py:57. Samym breakiem możesz go potem wyświetlić
#Możesz go wyłączyć (disable) włączyć (enable), podajac po komendzie jego numer porządkowy. (Tutaj będzie 1)
#list - Wyświetla w którym momencie kodu jest breakpoint. Spróbuj go użyć pare razy
#whatis a - Typ zmiennej a
#print(a) - Wyswietla wartosc zmiennej a
#args - możemy zobaczyć z jakimi argumentami została wywowała funkcja estimate_pi_cesaro
#next - Przechodzi do następnej linijki po danym breakpoincie. Ta komenda NIE przechodzi do następnego breakpointu.Pozwala ona nam na
#śledzenie wykonywania sie programu.
#step - Możesz ,,wejść" do metody. Wypróbuj na set_trace()
#Continue - Kontynuuje działanie programu do następnego breakpointa/błędu. Można też nim wychodzić ze wcześniejszego stepa.
#Oprócz nextem, możemy przechodzić po kodzie up i down, oraz jumpem.
#quit - wychodzi z programu
#help - pokazuje wszystkie dostępne komendy
#Dużą większość komend można wywołać wpisują tylko pierwszą literę






import math
import random
import pdb

def estimate_pi_cesaro(iterations, max_value=10000000):
    coprimes = 0

    for _ in range(iterations):
        a = random.randint(1, max_value)
        b = random.randint(1, max_value)


        if math.gcd(a, b) == 1:
            coprimes += 1

    probability = coprimes / iterations

    pdb.set_trace()

    if probability == 0:
        return 0
    probability = 0

    pdb.set_trace()

    pi_estimate = math.sqrt(6 / probability)



    return probability, pi_estimate


iterations = 1_000_000
prob, pi_est = estimate_pi_cesaro(iterations)


print(f"Liczba prób: {iterations}")
print(f"Odsetek par względnie pierwszych (P): {prob:.6f}")
print(f"Oszacowana liczba Pi: {pi_est:.6f}")
print(f"Prawdziwe Pi (math.pi): {math.pi:.6f}")