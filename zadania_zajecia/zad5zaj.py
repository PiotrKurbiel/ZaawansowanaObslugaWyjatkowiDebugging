#Zadanie 5
#Pracujesz dalej w tej samej firmie teleinformatycznej, ale w troche innym dziale
#Tym razem otrzymujesz program który wylicza transmitancje filtra na podstawie jego wcześniej wyliczonych współczynników a (wzór uproszczony)
#Współczynniki które otrzymujesz, są dokładniejsze niż pozwala na to sprzęt, dlatego są one zaokrąglane do danych wartości, np do 1
#Powoduje to czasami całkowite wyzerowanie mianownika, i wyrzucenie wyjątku związanego z tą operacją
#Aby naprawić ten błąd, musisz dokończyć klasę ReduckjaPrzybliżenia, która pełni funkcje Context Managera, czyli musi mieć __enter i __exit__
#Napisz kod który w przypadku wyrzucenia wyjątku związanego z zerowaniem mianownika, doda do współczynników 0.001,
#oraz poda poprawną transmitancje tylko raz (bool dobreobliczenia = True)


class RedukcjaPrzyblizenia:
    def __init__(self, a1, a2, a3):
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3
        self.dobreobliczenia = False;
        #__enter__

        #__exit__


filtr = RedukcjaPrzyblizenia(3,0.999,1)
while not filtr.dobreobliczenia:
    with filtr as f:
        H = 1/((1- f.a1)*(1 - f.a2)*(1 - f.a3))
        print(H)
