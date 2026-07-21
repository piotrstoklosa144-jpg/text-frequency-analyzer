def licznik_znakow(nazwa_pliku):
    try:
        with open(nazwa_pliku, 'r', encoding='UTF-8') as plik:
            tekst = plik.read().lower()
        
        alfabet = 'abcdefghijklmnopqrstuvwxyz'
        licznik = {litera: 0 for litera in alfabet}
        wszystkie_znaki = 0

        for znak in tekst:
            if znak.isalpha() and znak in alfabet:
                licznik[znak] += 1
                wszystkie_znaki += 1

        print(f"Zestawienie częstotliwości występowania liter w pliku '{nazwa_pliku}':")
        for znak in alfabet:
            liczba = licznik[znak]
            procent = (liczba / wszystkie_znaki) * 100 if wszystkie_znaki > 0 else 0
            print(f"{znak}: {liczba} ({procent:.2f}%)")
    
    except FileNotFoundError:
        print(f"Plik '{nazwa_pliku}' nie istnieje. Sprawdź ścieżkę i spróbuj ponownie.")
    except Exception as e:
        print(f"Wystąpił problem podczas analizy pliku: {e}")

nazwa_pliku = r"C:\Users\rosik\Desktop\python\plik.txt" #tu mozna wprowadzic sciezke ze swojego dysku
licznik_znakow(nazwa_pliku)
