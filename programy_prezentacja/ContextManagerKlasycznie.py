class MojMenadzerZasobow:
    def __init__(self, nazwa_zasobu):
        self.nazwa = nazwa_zasobu

    def __enter__(self):
        print(f"KROK 1 (__enter__): Rezerwuję zasób '{self.nazwa}' (np. otwieram plik/bazę)")
        return self  # To, co tu zwrócimy, trafi do zmiennej po słowie 'as'

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"KROK 3 (__exit__): Uruchamiam akcję porządkową dla '{self.nazwa}' (zamykam zasób)")

        # Sprawdzamy, czy w bloku "with" wystąpił błąd
        if exc_type:
            print(f"   [INFO] Wychwyciłem błąd typu: {exc_type.__name__} o treści: '{exc_val}'")
            print("   [INFO] Decyduję o wpuszczeniu błędu dalej (return False)")
            return False  # False = program się wywali; True = błąd zostanie "połknięty"




# Wszystko działa
print("--- SCENARIUSZ A (Sukces) ---")
with MojMenadzerZasobow("Plik_A.txt") as zasob:
    print("KROK 2: Wykonuję bezpieczne operacje wewnątrz bloku 'with'...")

print("\n--- SCENARIUSZ B (Awaria) ---")
# z błędem
try:
    with MojMenadzerZasobow("Baza_Danych_B") as zasob:
        print("KROK 2: Próbuję wykonać operację, która zaraz wybuchnie...")
        wynik = 1 / 0
except ZeroDivisionError:
    print("KROK 4: Główny program przechwycił błąd przepuszczony przez __exit__.")



