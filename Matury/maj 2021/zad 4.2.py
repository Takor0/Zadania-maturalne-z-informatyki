plik = open("instrukcje.txt","r")
zmienna = []
tablica = []
j=0

DLUGOSC = 2000


while j<DLUGOSC:
    zmienna.append(plik.readline())
    tablica.append(zmienna[j].split())
    j += 1

operacja = ""
ciag = 0
temp = 0
i = 0
while i<DLUGOSC:
    if i+1 == DLUGOSC:
        break
    if tablica[i][0] == tablica[i+1][0]:
        temp += 1
        if temp > ciag:
            ciag = temp
            operacja = tablica[i][0]
    else:
        temp = 1
    i += 1

print(operacja + " " + str(ciag))

