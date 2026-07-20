# Text Frequency Analyzer - Licznik liter w pliku

## O projekcie
Prosty skrypt narzędziowy w Pythonie, który sprawdza, jak często poszczególne litery pojawiają się w pliku tekstowym. Kod odrzuca cyfry, spacje i znaki specjalne, skupiając się wyłącznie na podstawowym alfabecie łacińskim od A do Z. Na koniec wylicza procentowy udział każdej litery w całym tekście.

## Technologie
* Język: Python 3
* Biblioteki: Brak (skrypt korzysta wyłącznie z wbudowanych funkcji Pythona)

## Funkcje skryptu
* Ignoruje wielkość liter – przed analizą zamienia cały tekst w pliku na małe litery.
* Odrzuca cyfry, znaki interpunkcyjne oraz znaki specjalne poza zakresem a-z.
* Oblicza udział procentowy każdej litery z dokładnością do dwóch miejsc po przecinku.
* Posiada prostą obsługę błędów – jeśli podasz złą ścieżkę, skrypt wyświetli czytelny komunikat zamiast się zawiesić.

---

## Jak to uruchomić
1. Otwórz plik skryptu i w zmiennej nazwa_pliku podaj ścieżkę do swojego pliku tekstowego na dysku.
2. Uruchom skrypt w terminalu: python main.py
3. Wyniki analizy zobaczysz od razu w konsoli w formie czytelnego zestawienia.
