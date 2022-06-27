plik = open("galerie.txt", "r")
zmienna = []
tablica = []
j = 0
odpowiedza = open("wynik4_2a.txt", "w")
odpowiedzb = open("wynik4_2b.txt", "w")
while j < 50:
    zmienna.append(plik.readline())
    tablica.append(zmienna[j].split())
    j += 1
j = 0
temp = 0
ilosc_lokali = 0
najwieksza = 0
najwieksza_str = ""
najmniejsza = 1000000
najmniejsza_str = ""
for i in tablica:
    for j in range(2, 140, 2):
        temp += (int(i[j]) * int(i[j+1]))
    for j in range(2, 140, 2):
        if int(i[j]) != 0:
            ilosc_lokali += 1
    odpowiedza.write(i[1] + " " + str(temp) + " " + str(ilosc_lokali) + "\n")
    ilosc_lokali = 0
    if temp > najwieksza:
        najwieksza_str = i[1] + " " + str(temp)
        najwieksza = temp

    if temp < najmniejsza:
        najmniejsza_str = i[1] + " " + str(temp)
        najmniejsza = temp
    temp = 0
odpowiedzb.write(najwieksza_str+"\n")
odpowiedzb.write(najmniejsza_str+"\n")
