def cykl_zycia_wyjatku(licznik, mianownik):
    try:
        print(f"KROK 1: Próbuję podzielić {licznik} przez {mianownik}")
        wynik = licznik / mianownik

    except ZeroDivisionError:
        print("KROK 2 [BŁĄD]: Omijanie katastrofy... Nie dzielimy przez zero!")

    else:
        print(f"KROK 2 [SUKCES]: Wynik to {wynik}. Świetna robota!")

    finally:
        print("KROK 3 [KONIEC]: Zwalniam procesor i kończę procedurę.")

cykl_zycia_wyjatku(10, 2)
cykl_zycia_wyjatku(10, 0)


# Return w Finally

def przypadek_A_nadpisanie():
    try:
        return "Wynik z bloku TRY"
    finally:
        # To bezczelnie nadpisze poprzedni return
        return "Wynik z bloku FINALLY"


def przypadek_B_znikajacy_blad():
    try:
        # wywołujemy błąd
        wynik = 1 / 0
    finally:
        # Ten return 'połknie' błąd i udaje, że wszystko jest super
        return "Wszystko działa idealnie!"

print("--- PRZYPADEK A (Walka instrukcji return) ---")
print(f"Funkcja zwróciła: {przypadek_A_nadpisanie()}")

print("\n--- PRZYPADEK B (Znikający błąd) ---")
print(f"Funkcja zwróciła: {przypadek_B_znikajacy_blad()}")