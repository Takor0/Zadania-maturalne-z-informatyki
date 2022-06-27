def potega(x):
    if x == 1:
        return True
    z = 3
    while z <= x:
        if z == x:
            return True
        z = z * 3
    return False






def glowna():
    plik = open("liczby.txt","r")
    zmienna = []
    tablica = []
    j=0

    DLUGOSC = 500


    while j<DLUGOSC:
        zmienna.append(plik.readline())
        tablica.append(zmienna[j].split())
        j += 1

    licznik = 0
    for i in tablica:
        if potega(int(i[0])) == True:
            licznik += 1

    print(licznik)

glowna()



