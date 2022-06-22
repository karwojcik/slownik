slownik = {}

while(True):
    print("1-Dodaj definicję")
    print("2-Znajdź definicję")
    print("3-Usuń definicję")
    print("4-Zakończ")


    wybor = input("Twój wybór: ")

    if (wybor == "1"):
        slowo = input("Podaj slowo: ")
        definicja = input ("Podaj definicję: ")
        slownik[slowo] = definicja
        print("Dodano do słownika")
    elif (wybor == "2"):
        
        slowo = input("Podaj slowo: ")
        if slowo in slownik:
            print(definicja)
        else:
            print("Nie znaleziono słowa")
    elif (wybor == "3"):
        
        slowo = input("Podaj slowo: ")
        if slowo in slownik:
            del definicja
            print("Usunięto pomyślnie")
        else:
            print("Nie znaleziono słowa")
    elif (wybor == "4"):
        print("Zakończono")
        break
    else:
        print("Wybór z poza zakresu")
        

