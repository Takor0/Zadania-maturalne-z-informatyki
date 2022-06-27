plik = open("galerie.txt","r")
zmienna = []
tablica = []
j=0

odpowiedz = open("wynik4_1.txt", "w")



while j<50:
    zmienna.append(plik.readline())
    tablica.append(zmienna[j].split())
    j += 1
plik.close()
string = ""
temp = ""
old = []
j=0
z=0
ile = 0
czy_break = 0
while j < 50:
    temp = tablica[j][0]
    for i in old:
        if temp == i:
            czy_break = 1
            break
    if czy_break == 1:
        czy_break = 0
        j += 1
        continue
    old.append(temp)
    for i in tablica:
        if(temp==tablica[z][0]):
            ile += 1
        z+=1
    string = temp + " " + str(ile)
    odpowiedz.write(string+" "+"\n")
    ile = 0
    z=0
    j += 1
    print(j)









