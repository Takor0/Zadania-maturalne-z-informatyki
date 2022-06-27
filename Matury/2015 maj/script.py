def czy_wiecej(x):
    temp1 = 0
    temp2 = 0
    for i in x:
        if i == '1':
            temp1 += 1
        if i == '0':
            temp2 += 1
    if (temp1 < temp2):
        return True
    else:
        return False


wynik1 = open("wyniki1.txt","w")
wynik2 = open("wyniki2.txt","w")
wynik3 = open("wyniki3.txt","w")



file = open("liczby.txt", "r")

tablica = []
for i in range(0, 1000):
    tablica.append(file.readline())

more_zeros = 0

for i in tablica:
    if czy_wiecej(i):
        more_zeros += 1

tablica = [s.rstrip() for s in tablica]

wynik1.write(str(more_zeros))

more_zeros = 0
more_eight = 0


for i in tablica:
    temp8 = i[-3] + i[-2] + i[-1]
    temp2 = i[-1]
    if temp8 == '000':
        more_eight += 1
    if temp2 == '0':
        more_zeros += 1

wynik2.write(str(more_zeros)+'\n')
wynik2.write(str(more_eight))

temp_dl = 0
krotka = len(tablica[0])


najdl = 0
najkr = 0

dluga = 0


for i in tablica:
    temp_kr = len(i)
    temp_dl = len(i)
    if dluga < temp_dl:
        dluga = temp_dl
    if krotka > temp_kr:
        krotka = temp_kr

temp_dl = 0
temp_kr = 0

najdl = '0'
najkr = '111'


for i in tablica:
    if len(i) == dluga:
        temp_dl = i
        if temp_dl > najdl:
            najdl = temp_dl
    if len(i) == krotka:
        temp_kr = i
        if najkr > temp_kr:
            najkr = temp_kr


odp1 = ''
odp2 = ''

for i in tablica:
    if i==najkr:
        odp1 = str(tablica.index(i)+1)
    if i==najdl:
        odp2 = str(tablica.index(i)+1)







wynik3.write(odp1+'\n')
wynik3.write(odp2)














