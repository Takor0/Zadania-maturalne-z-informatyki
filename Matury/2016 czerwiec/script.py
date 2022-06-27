file = open('liczby.txt', 'r')

wynik1 = open('wynik_6_1','w')
wynik2 = open('wynik_6_2','w')
wynik3 = open('wynik_6_3','w')
wynik4 = open('wynik_6_4','w')
wynik5 = open('wynik_6_5','w')

tablica = []
for i in range(0,999):
    tablica.append(file.readline())
tablica = [s.rstrip() for s in tablica]
osemkowy = 0
for i in tablica:
    if i[-1] == '8':
        osemkowy += 1
print(osemkowy) # zadanie 1
wynik1.write(str(osemkowy))

czworkowy = 0
wystepuje = 0

temp = []
for i in tablica:
    liczba = i[0:-1]
    if i[-1] == '4':
        temp.append(liczba)
for i in tablica:
    liczba = i[0:-1]
    if i[-1] == '4':
        for z in liczba:
            if z == '0':
                temp.remove(liczba)
                break
print(len(temp)) # zadanie 2
wynik2.write(str(temp))
parzyste = 0
for i in tablica:
    liczba = i[0:-1]
    if i[-1] == '2':
        if liczba[-1] == '0':
            parzyste += 1
print(str(parzyste)) # zadanie 3
wynik3.write(str(parzyste))
suma = 0
for i in tablica:
    liczba = i[0:-1]
    if i[-1] == '8':
        liczba = '0o' + liczba
        suma += int(liczba, 8)
print(str(suma)) # zadanie 4
wynik4.write(str(suma))
najwieksza = 0
najmniejsza = int(tablica[0][0:-1],int(tablica[0][-1]))
kod_najwieksza = 0
kod_najmniejsza = 0

temp = 0

for i in tablica:
    liczba = i[0:-1]
    liczba = int(liczba, int(i[-1]))
    if liczba > najwieksza:
        kod_najwieksza = i[-1]
        najwieksza = liczba
    if liczba < najmniejsza:
        kod_najmniejsza = i[-1]
        najmniejsza = liczba
        temp = i




print(str(kod_najwieksza) + ' ' +str(najwieksza)) # zadanie 5.1
print(str(kod_najmniejsza) + ' ' + str(najmniejsza)) # zadanie 5.2
wynik5.write(str(najmniejsza))
wynik5.write('\n' + str(najwieksza))






