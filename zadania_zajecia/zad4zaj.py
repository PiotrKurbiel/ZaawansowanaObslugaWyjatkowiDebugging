#Zadanie 4
#Pracujesz w firmie teleinformatycznej, która posiada program który wylicza moc odbieraną w zależnośći od odległości
#Zauważyłeś że czasami program ,,wychodzi" dla danych wartości r.
#Dostałeś zadanie aby w takim przypadku zapisać do pliku zad4.txt wiadomosć dla której wartości r to sie stało
#Popraw też samo otwieranie plików, tak aby był automatycznie został zamykany




import math
import sys
import random


file = open("zad4.txt", "w")

    for r in range(1,100):
        try:
            Pt = 10;
            f = 1000000
            c = 300000000
            dlugosc = f/c
            a = random.randint(1,10)
            Pr = Pt * (dlugosc/4*math.pi*r)**2
            print("Pr = " + str(Pr))
            if(a == 7):                                                             #Patrz 7 z zadania drugiego!
                sys.exit("System interrupted in iteration nr: " + str(r))
        #--kod--























































if not file.closed:
    raise Exception("Może byś mnie zamknął co?")
