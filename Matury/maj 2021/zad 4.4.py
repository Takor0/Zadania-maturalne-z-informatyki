def przesun(wyraz, litera):
    wyraz = list(wyraz)
    temp = 0
    for i in wyraz:
        if i == litera:
            temp = ord(i)
            if temp == 90:
                wyraz[wyraz.index(i)] = 'A'
                break
            else:
                wyraz[wyraz.index(i)] = chr(temp+1)
                break




    wyraz = "".join(wyraz)
    return wyraz

plik = open("instrukcje.txt","r")
zmienna = []
tablica = []
j=0

DLUGOSC = 2000


while j<DLUGOSC:
    zmienna.append(plik.readline())
    tablica.append(zmienna[j].split())
    j += 1

napis = ""

for i in tablica:
    if i[0] == "DOPISZ":
        napis += i[1]
    if i[0] == "ZMIEN":
        napis = napis[0:len(napis)-1] + i[1]
    if i[0] == "USUN":
        napis = napis[0:len(napis)-1]
    if i[0] == 'PRZESUN':
        napis = przesun(napis,i[1])

print(napis)

