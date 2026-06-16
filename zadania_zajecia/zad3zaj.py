#Zadanie3
#Napisałeś bardzo intrygująćy program, który działa jak działa, i oddajesz go do użytkownikowi, który wprowadza dany input.
#Użytkownik wpisuje w input wszystkie cyfry (0-9), jak i swoje imię
#W takim przypadku, błędy które wyskakują, nie są skutkiem złego działania programu, a błędnego inputu, o którym informuje klasa InvalidInput
#Zabezpiecz program tak, aby łapane były wszystkie błędy dla inputów które wpisał użytkownik, i poinformuj go, że są one skutkiem jego błędu.
#W przypadku poprawnego rozwiązania, powinna wyskoczyć wiadomość "The above exception was the direct cause of the following exception:"

class InvalidInput(Exception):
    def __init__(self, msg="Błąd wyskoczył tylko i wyłącznie przez CIEBIE. Wpisałeś ZŁY input i popsułeś CAŁY program. Teraz ktoś to musi naprawiać. Brawo Ty"):
        self.msg = msg
        super().__init__(self.msg)

print("Wprowadz offset")

try:
    offset = input()
    cyferki = [0,1,2,3,4,5,6,8,9]
    if int(offset)==1:
        raise AssertionError("Szanujmy sie nie będziemy dzielić przez 1. Jesteś za bardzo asertywny, dostajesz assertion errora")
    index = int(10/int(offset))
    for x in range(0,10-index):
        print(cyferki[x+index])
    #--kod--





