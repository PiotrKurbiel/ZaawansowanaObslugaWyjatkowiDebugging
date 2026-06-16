import asyncio


# Definiujemy własny błąd dla lepszego kontekstu
class BladWalidacji(Exception):
    pass


def uruchom_wielokrotne_zadania():
    print("1. [Start] Uruchamiam kilka operacji na raz...")

    # Tworzymy paczkę (grupę) zawierającą 3 różne błędy
    paczka_bledow = ExceptionGroup(
        "Krytyczna awaria formularza",
        [
            BladWalidacji("Niepoprawny adres e-mail (zadanie 1)"),
            TypeError("Oczekiwano liczby, otrzymano tekst (zadanie 2)"),
            BladWalidacji("Hasło jest zbyt krótkie (zadanie 3)")
        ]
    )

    # Rzucamy całą grupę naraz
    raise paczka_bledow


# ==========================================
# OBSŁUGA GRUPY WYJĄTKÓW
# ==========================================
try:
    uruchom_wielokrotne_zadania()

except* BladWalidacji as eg:
    # Ten blok odfiltruje i złapie OBA błędy typu BladWalidacji!
    print("\n2. [Obsługa BladWalidacji] Wykryto problemy z danymi:")
    for e in eg.exceptions:
        print(f"   -> {e}")

except* TypeError as eg:
    # Program przechodzi tutaj i wyciąga z paczki błędy typu TypeError.
    print("\n3. [Obsługa TypeError] Wykryto błąd programistyczny w typach danych:")
    for e in eg.exceptions:
        print(f"   -> {e}")

print("\n4. [Koniec] Wszystkie błędy z paczki zostały obsłużone. Program działa dalej!")