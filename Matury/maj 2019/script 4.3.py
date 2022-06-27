def nwd(a,b):
    while a!=b:
        if a > b:
            a = a - b
        if a < b:
            b = b - a
    return a


def glowna():

    plik = open('liczby.txt')
    twe = plik.readlines()
    twe = [int(i.strip()) for i in twe]
    twe = list(map(int,twe))
    plik.close()

    N=len(twe)
    dzielmax=0
    dlmax=0
    pierwszamax=0
    for j in range(N-1):
        dl=1
        pierwsza=twe[j]
        localnwd=twe[j]
        for i in range(j+1,N):
            n=nwd(localnwd,twe[i])
            if n>1:
                localnwd=n
                dl+=1
            if n==1 or i==N-1:
                if dlmax<dl:
                    dzielmax=localnwd
                    dlmax=dl
                    pierwszamax=pierwsza
                break
    print(pierwszamax,dlmax,dzielmax)

    

glowna()