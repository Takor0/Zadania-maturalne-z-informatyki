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

DLUGOSC = 200  # pierwsze
DLUGOSC2 = 300 # liczby


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

for tab in tablica:
    for i in tab:
        temp = i[::-1]
        if prime(int(temp)):
            odpowiedzi.append(i)


for i in odpowiedzi:
    print(i)



