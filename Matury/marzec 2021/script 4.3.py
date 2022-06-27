plik = open("galerie.txt", "r")
zmienna = []
tablica = []
j = 0

odpowiedz = open("wynik4_3.txt", "w")

while j < 50:
    zmienna.append(plik.readline())
    tablica.append(zmienna[j].split())
    j += 1
j = 0

najmniej = 10000
najwiecej = 0
miasto_naj = ""
miasto_mni = ""
temp = 0
ilosc_miast = 0
tab = tablica[0]
ilosc_lokali = 0
lokale = []

for tab in tablica:
    for i in range(2, 140 ,1):
        if tab[i] != '0':
            ilosc_miast += 1
    ilosc_lokali = ilosc_miast//2
    for i in range(2, ilosc_miast+2, 2):
        temp = int(tab[i]) * int(tab[i+1])
        lokale.append(temp)
    lokale = list(dict.fromkeys(lokale))
    if len(lokale) > najwiecej:
        najwiecej = len(lokale)
        miasto_naj = tab[1]
    if len(lokale) < najmniej:
        najmniej = len(lokale)
        miasto_mni = tab[1]
    lokale = []
    ilosc_miast = 0

odpowiedz.write(miasto_naj+ " "+str(najwiecej) + "\n")
odpowiedz.write(miasto_mni+ " " + str(najmniej))











