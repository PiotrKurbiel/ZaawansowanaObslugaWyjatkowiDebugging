#Zadanie1
#Postanowiłeś że w teleinformatyce nie ma pieniędzy, i przebranżowiłeś sie na budżetówke
#Pracujesz w ZUSie, i chcesz rozliczyć pewną firme z ich płac. Zakładasz że każdy w firmie pracuje na pełen etat i ma umowę o pracę
#Napisz własny wyjątek Najnizszakrajowa, i wyrzuc go w metodzie ZUS, w momencie w ktorym płaca danej osoby jest niższa od najniższej_krajowej
#Wyrzucony wyjątek powinien przyjmować za wiadomość imię, i płace danej osoby


class NajnizszakrajowaError(Exception):
    #--kod--

def ZUS(dane):
    najnizsza_krajowa = 4806
    #--kod--


firma = {
    "Kowalski": 3000,
    "Nowak": 5000,
    "Działowy": 4000,
    "Lewandowski": 5000000
}

ZUS(firma)