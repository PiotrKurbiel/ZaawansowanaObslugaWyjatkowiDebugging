# # Tworzymy własny błąd poprzez dziedziczenie po klasie Exception
# class ProduktNiedostepnyError(Exception):
#     """Wyjątek rzucany, gdy klient próbuje kupić produkt, którego nie ma w magazynie."""
#     pass
#
#
# magazyn = {"buty": 0, "koszulka": 5}
#
# def kup_produkt(nazwa):
#     if magazyn.get(nazwa, 0) == 0:
#         # Rzucamy nasz własny błąd z czytelnym komunikatem
#         raise ProduktNiedostepnyError(f"Niestety, produkt '{nazwa}' został wyprzedany!")
#     print(f"Sukces! Kupiono {nazwa}.")
#
# try:
#     kup_produkt("buty")
# except ProduktNiedostepnyError as e:
#     # Łapiemy dokładnie nasz błąd, ignorując inne typy wyjątków
#     print(f"[KONTROLA BŁĘDU]: {e}")


class BladAutoryzacjiError(Exception):
    def __init__(self, komunikat, uzytkownik_id, adres_ip):
        super().__init__(komunikat)
        self.uzytkownik_id = uzytkownik_id
        self.adres_ip = adres_ip

user_id = "hacker_2137"
ip = "192.67.1.99"

try:
    raise BladAutoryzacjiError("Odmowa dostępu!", user_id, ip)
except BladAutoryzacjiError as e:
    print(f"Podejrzany użytkownik: {e.uzytkownik_id}")
    print(f"Adres IP sprawcy: {e.adres_ip}")