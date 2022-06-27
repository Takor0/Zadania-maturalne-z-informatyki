def waga(x):
    temp = 0
    j = 1
    while True:
        for i in x:
            temp = temp + int(i)
        x = str(temp)
        j += 1
        temp = 0
        if int(x) < 10:
            return x


plik = open("pierwsze.txt","r")
zmienna = []
tablica = []
j=0
DLUGOSC = 200  # pierwsze
while j<DLUGOSC:
    zmienna.append(plik.readline())
    tablica.append(zmienna[j].split())
    j += 1

licznik = 0

for tab in tablica:
    for i in tab:
        if waga(i) == '1':
            licznik += 1


print(licznik)






