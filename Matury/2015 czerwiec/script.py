file = open("kody.txt", "r")
file2 = open("cyfra_kodkreskowy.txt", 'r')


wynik1 = open('kody1.txt','w')
wynik2 = open('kody2.txt','w')
wynik3 = open('kody3.txt','w')

tablica = []
for i in range(0, 500):
    tablica.append(file.readline())
tablica = [s.rstrip() for s in tablica]

kod = []
for i in range(0, 10):
    kod.append(file2.readline())
kod = [s.rstrip() for s in kod]

for i in tablica:
    suma_par = 3 * (int(i[1]) + int(i[3]) + int(i[5]))
    suma_parzysta = int(i[1]) + int(i[3]) + int(i[5])
    suma_niepar = (int(i[0]) + int(i[2]) + int(i[4]))
    suma = suma_par + suma_niepar
    reszta = suma%10
    wynik = 10 - reszta
    kontrol = wynik%10

    kontrol_25 = 0

    napis = '11011010'
    for z in i:
        napis += kod[int(z)][2:16]
    napis += kod[kontrol][2:16]
    napis += '11010110'


    wynik1.write(str(suma_parzysta)+" "+str(suma_niepar)+'\n')
    wynik2.write(str(kontrol)+" ")
    wynik2.write(str(kod[kontrol][2:16])+'\n')
    wynik3.write(str(napis)+'\n')

#print(str(suma_parzysta)+" "+str(suma_niepar))   # zadanie 1
#print(str(kontrol) + ' ' + kod[kontrol][2:16])   # zadanie 2
#print(napis)  # zadanie 3



