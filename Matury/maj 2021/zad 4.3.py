plik = open("instrukcje.txt","r")
zmienna = []
tablica = []
j=0

DLUGOSC = 2000

pomoc = {
    'A' : 0,
    'B' : 0,
    'C' : 0,
    'D' : 0,
    'E' : 0,
    'F' : 0,
    'G' : 0,
    'H' : 0,
    'I' : 0,
    'J' : 0,
    'K' : 0,
    'L' : 0,
    'M' : 0,
    'N' : 0,
    'O' : 0,
    'P' : 0,
    'R' : 0,
    'S' : 0,
    'T' : 0,
    'V' : 0,
    'U' : 0,
    'W' : 0,
    'X' : 0,
    'Y' : 0,
    'Z' : 0,
    'Q' : 0
}

litera = ''

while j<DLUGOSC:
    zmienna.append(plik.readline())
    tablica.append(zmienna[j].split())
    j += 1

for i in tablica:
    if i[0] == 'DOPISZ':
        pomoc[i[1]] += 1

temp = 0
for i in pomoc:
    if pomoc[i] > temp:
        temp = pomoc[i]
        litera = i
print(litera + " " + str(temp))







