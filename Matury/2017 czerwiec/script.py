import math

def prime(x):
    if x == 0:
        return True
    if x == 1:
        return False
    for i in range(2,x+1):
        if x != i:
            if x%i == 0:
                return True
        else: return False





file = open('punkty.txt','r')
tablica = []
for i in range(0,1000):
    tablica.append(file.readline())
for i in range(0,1000):
    tablica[i] = tablica[i].split()

pierwsze = 0

for i in tablica:
    if prime(int(i[0])) == False and prime(int(i[1])) == False:
        pierwsze += 1

#print(pierwsze) # zadanie 1
podobne = 0
cyfry = []
cyfry2 = []
for i in range(1000):
    cyfry = []
    cyfry2 = []
    cyfry = list(tablica[i][0])
    cyfry2 = list(tablica[i][1])
    cyfry = list(dict.fromkeys(cyfry))
    cyfry2 = list(dict.fromkeys(cyfry2))
    cyfry.sort()
    cyfry2.sort()
    if cyfry == cyfry2:
        podobne += 1

najwieksza = 0
temp = 0

punkt1x = 0
punkt1y = 0
punkt2x = 0
punkt2y = 0

#print(podobne) # zadanie 2
for i in tablica:
    xa = float(i[0])
    ya = float(i[1])
    for j in range(1000):
        xb = float(tablica[j][0])
        yb = float(tablica[j][1])
        temp = math.sqrt(((xb-xa)*(xb-xa)) + ((yb-ya)*(yb-ya)))
        if temp > najwieksza:
            najwieksza = temp
            punkt1x = xa
            punkt1y = ya
            punkt2x = xb
            punkt2y = yb
#print(math.ceil(najwieksza)) # zadanie 3
#print(str(punkt1x)+ ' '+ str(punkt1y)) # zadanie3.punkty1
#print(str(punkt2x)+ ' '+ str(punkt2y)) # zadanie3.punkty2

wewnatrz = 0
nabokach = 0
nazewnatrz = 0

for i in tablica:
    if int(i[0]) < 5000:
        if int(i[1]) < 5000:
            wewnatrz += 1
    if int(i[0]) == 5000 and int(i[1]) <= 5000:
        nabokach += 1
    if int(i[1]) == 5000 and int(i[0]) <= 5000:
        nabokach += 1
    if int(i[0]) > 5000 or int(i[1]) > 5000:
        nazewnatrz +=1

print(wewnatrz) # punkty wewnatrz
print(nabokach) # punkty na bokach
print(nazewnatrz) # punkty na zewnatrz












