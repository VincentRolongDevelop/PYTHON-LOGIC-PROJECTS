numeroDeRegistros = int(input())
lista = []
SI_esta_disponible = []
No_Esta_Disponible = []


for i in range(numeroDeRegistros):
    altura, bielas, sillin, manilar, valor = input().split()
    altura = int(altura)
    bielas = int(bielas)
    sillin = int(sillin)
    manilar = int(manilar)
    valor = int(valor)
    lista.append([altura, bielas, sillin, manilar, valor])

for i in range(len(lista)):
    if (lista[i][0] >= 240 and lista[i][0] <= 300) and (lista[i][1] >= 160 and lista[i][1] <= 180) \
        and (lista[i][2] >= 240 and lista[i][2] <= 275) and (lista[i][3] >= 0 and lista[i][3] <= 50):
        SI_esta_disponible.append(lista[i][4])
    else:
        No_Esta_Disponible.append(lista[i][4])

if len(lista) == len(No_Esta_Disponible):
    print("NO DISPONIBLE")
else:
    print(sum(SI_esta_disponible))