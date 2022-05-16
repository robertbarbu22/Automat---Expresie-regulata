f = open("automat.in", "r")
g= open("automat.out", "w")
stari_finale=[]
noduri= int()
tranzitii=[]
linia1=f.readline()
lista_noduri1=[]
noduri=linia1[0]
nr_tranzitii=linia1[2]
nr_tranzitii=int(nr_tranzitii)
for i in range(nr_tranzitii):
    linie=f.readline()
    tranzitii.append([linie[0],linie[2],linie[4]])   #punem tranzitiile intr-o lista
    lista_noduri1.append(linie[0])
linie=f.readline()
stare_initiala=linie[0]  #memoram starea initiala
linie=f.readline()
nr_stari_finale=int(linie[0])
for i in range(2,nr_stari_finale*2+1, 2):
    stari_finale.append(linie[i])   #punem starile finale intr-o lista
tranzitiinod=[]
lista_noduri1=set(lista_noduri1)
lista_noduri=[]
for nod in lista_noduri1:
    lista_noduri.append([nod]) #cream lista cu nodurile pe care le avem
for nod in lista_noduri:
    ct=0
    for tranzitie in tranzitii:
       if tranzitie[0] == nod[0]:
           ct+=1
    nod.append(ct)  #retinem fiecare nod cate tranzitii are

for tranzitie in tranzitii:  #rezolv buclele si atribui litera pe muchii
    if tranzitie[0] == tranzitie[1]:
        for tranzitie2 in tranzitii:
            if tranzitie2[0] == tranzitie[0]:
                if tranzitie2[0] != tranzitie2[1]:
                    tranzitie2[2] = tranzitie[2] + '*' + tranzitie2[2]
        for nod in lista_noduri:
            if nod[0] == tranzitie[0]:
                nod[1] = nod[1] -1
        tranzitii.remove(tranzitie)
        nr_tranzitii -= 1

while nr_tranzitii > 1 :  #elimin noduri pe rand, incepand cu cele cu cele mai putine tranzitii
    for nod in lista_noduri:
        if nod[1] == 1 and nod[0] != stare_initiala:
            for tranzitie in tranzitii:   #caut tranzitia care incepe din nodul cu cele mai putine tranzitii
                if tranzitie[0] == nod[0]:
                    for tranzitie2 in tranzitii:
                        if tranzitie2[1] == nod[0]: # caut nodul care intra in  nodul cu cele mai putine tranzitii
                            litere = tranzitie2[2]
                            litere = litere + tranzitie[2]
                            nod[1] -= 1
                            for nod1 in lista_noduri:
                                if nod1[0] == tranzitie2[0]:
                                    if nod1[0] != stare_initiala:
                                        nod1[1] -= 1
                                    else:
                                        if nod1[1] > 1:
                                            nod1[1] -= 1
                            ok=0
                            for tranzitie3 in tranzitii:
                                if tranzitie3[0] == tranzitie2[0] and tranzitie3[1] != tranzitie2[1]:
                                    tranzitie3[2] = tranzitie3[2] + '+' + litere  #atribui literele de la nodul eliminat altor muchii
                                    ok=1
                                    tranzitii.remove(tranzitie)
                                    tranzitii.remove(tranzitie2)  #elimin tranzitiile din nodul eliminat
                                    nr_tranzitii -= 2
                            if ok == 0:
                                tranzitie2[1] = tranzitie[1]  #daca nodul care avea legatura cu cel eliminat nu mai merge in niciun altul, ii formam alta conexiune
                                tranzitie2[2] = litere
                                nr_tranzitii -= 1
                                tranzitii.remove(tranzitie)

g.write(str(lista_noduri)+'\n')
for tranzitie in tranzitii:
    g.write(str(tranzitie[2])+'\n')
g.write(str(nr_tranzitii))