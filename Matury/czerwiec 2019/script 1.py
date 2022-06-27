def prime(x):
    i = 2
    while x > i:
        if x % i == 0:
            return False
        i += 1
    return True


plik = open("pierwsze.txt","r")
plik2 = open("liczby.txt")
zmienna = []
tablica = []
zmienna2 = []
tablica2 = []
j=0

DLUGOSC = 200
DLUGOSC2 = 300


while j<DLUGOSC:
    zmienna.append(plik.readline())
    tablica.append(zmienna[j].split())
    j += 1
j=0
while j<DLUGOSC2:
    zmienna2.append(plik2.readline())
    tablica2.append(zmienna2[j].split())
    j += 1

odpowiedzi = []

for tab in tablica2:
    for i in tab:
        if int(i) >= 100 and int(i) <= 5000:
            if prime(int(i)):
                odpowiedzi.append(i)

for i in odpowiedzi:
    print(i)