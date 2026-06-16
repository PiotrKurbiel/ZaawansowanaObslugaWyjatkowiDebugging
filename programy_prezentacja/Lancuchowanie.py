# ==========================================
# Jawne łańcuchowanie:
# ==========================================

class BladAplikacji(Exception):
    """Nasz własny błąd logiczny."""
    pass

def pobierz_profil_uzytkownika():
    try:
        # Udajemy, że serwer nie odpowiada (błąd niskopoziomowy)
        raise ConnectionRefusedError("Serwer odrzucił połączenie.")
    except ConnectionRefusedError as oryginalny_blad:
        raise BladAplikacji("Nie udało się załadować profilu.") from oryginalny_blad

pobierz_profil_uzytkownika()

# ==========================================
# Niejawne łańcuchowanie:
# ==========================================

def oblicz_rabat():
    try:
        wynik = 100 / 0  # 1. Pierwszy błąd: ZeroDivisionError
    except ZeroDivisionError:
        # 2. Drugi błąd: pomyłka w kodzie - brak zmiennej: NameError
        print(cena_domyslna)

oblicz_rabat()

# ==========================================
# Ukrywanie łańcuchowania
# ==========================================

def zaloguj_do_panelu():
    try:
        # próbujesz odczytać pliki, ale nie masz uprawnień systemowych
        raise PermissionError("Brak uprawnień systemowych do pliku config.db")
    except PermissionError:
        raise RuntimeWarning("Logowanie nieudane. Spróbuj ponownie.") from None

zaloguj_do_panelu()