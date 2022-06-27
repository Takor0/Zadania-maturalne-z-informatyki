def znajdz_silnie(x):

    x = int(x)
    if x == 0:
        return 1
    temp = x
    i = 1
    while i<x:
        temp = temp * i
        i +=1
    return temp

def silnia(x):

    suma = 0
    for i in x:
        suma += znajdz_silnie(i)
    return suma


def glowna():
    plik = open("liczby.txt","r")
    zmienna = []
    tablica = []
    j=0

    DLUGOSC = 500

    wszystkie = []

    while j<DLUGOSC:
        zmienna.append(plik.readline())
        tablica.append(zmienna[j].split())
        j += 1

    liczba = ""

    for tab in tablica:
        for i in tab:
            liczba = silnia(i)
            if liczba == int(i):
                wszystkie.append(i)

    for i in wszystkie:
        print(i)






glowna()