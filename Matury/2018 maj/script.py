# A B C D E F G H I J K L M N O P Q R S T U V W X Y Z

def odleglosc(litera,array):
    for i in array:
        if ord(i) - ord(litera) >= 10 or ord(i) - ord(litera) <= -10:
            return False
    return True




#file = open('przyklad.txt', 'r')
file = open('sygnaly.txt', 'r')

tablica = []
for i in range(1000):
    tablica.append(file.readline())
tablica = [s.rstrip() for s in tablica]
przeslanie = ''
for i in range(40,1001,40):
    try: przeslanie += tablica[i-1][9]
    except: pass

slowo = []

#print(przeslanie) # zadanie 1
slowa = tablica
for i in range(1000):
    slowa[i] = list(dict.fromkeys(slowa[i]))

#file = open('przyklad.txt', 'r')
file = open('sygnaly.txt', 'r')

tablica = []
for i in range(1000):
    tablica.append(file.readline())
tablica = [s.rstrip() for s in tablica]

najwiecej = 0
temp = 0
for i in slowa:
    temp = len(i)
    if temp > najwiecej:
        najwiecej = temp
j = 0
najdluzszy = ''

for i in slowa:
    if len(i) == najwiecej:
        #print(tablica[j] + ' ' + str(najwiecej)) # zadanie 4.2
        break
    j += 1


flaga = 0

for i in tablica:
    flaga = 0
    for j in i:
        if odleglosc(j,i) == False:
            flaga = 1
    if flaga == 0:
        #print(i) # zadanie 4.3
        pass


