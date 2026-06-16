from contextlib import contextmanager

@contextmanager
def szybki_menadzer_pliku(nazwa):
    print(f"1. [Inicjalizacja] Otwieram połączenie z: {nazwa}")
    try:
        # yield przekazuje zasób do zmiennej po słowie 'as' i zawiesza funkcję
        yield f"AKTYWNE_POŁĄCZENIE_Z_{nazwa}"
    finally:
        # Kod w sekcji finally wykona się absolutnie zawsze, nawet po crashu programu!
        print(f"3. [Sprzątanie] Zamykam bezpiecznie połączenie z: {nazwa}")

# Użycie:
with szybki_menadzer_pliku("Serwer_SMTP") as serwer:
    print(f"2. [Logika] Korzystam z zasobu: {serwer}")
    # Nawet jeśli tutaj dopiszemy błąd (np. raise ValueError), krok 3 i tak się wykona!


    