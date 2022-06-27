def suma(x):
    liczydlo = 0
    for i in x:
        liczydlo += int(i)

    return liczydlo

def numer(x):
    liczba = 0
    return ord(x) - 55




def main():
    file = open("identyfikator.txt","r")
    tablica = []
    for i in range(200):
        tablica.append(file.readline())
    tablica = [s.rstrip() for s in tablica]
    najwieksza = 0
    temp = 0
    for i in tablica:
        temp = suma(i[3:9])
        if temp>najwieksza:
            najwieksza = temp

    for i in tablica:
        if suma(i[3:9]) == najwieksza:
            print(i)

    # chr(67) ord("a")



    #KOK201272
    print('---------------------------------------------------------')


    for i in tablica:
        temp = i[2] + i[1] + i[0]
        if i[0:3] == temp:
            print(i)
        temp2 = i[8]+ i[7]+ i[6]+ i[5]+ i[4]+ i[3]
        if i[3:9] == temp2:
            print(i)

    #  7, 3, 1, 7, 3, 1, 7, 3

    print('-----------------------------------')

    for i in tablica:
        sumaa = 7 * numer(i[0]) + 3 * numer(i[1]) + numer(i[2]) + int(i[4]) * 7 + int(i[5]) * 3 + int(i[6]) + int(i[7]) * 7 + int(i[8]) * 3
        if (sumaa%10) != int(i[3]):
            print(i)






main()
