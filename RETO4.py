

def repeticiones(lista_1):
    arrreglo = []
    defec = 0

    for z in lista_1:
        if z not in arrreglo:
            arrreglo.append(z)
        else:
            defec += 1

    return defec

numero_Baldosas, sensor = input().split()
numero_Baldosas = int(numero_Baldosas)
sensor = int(sensor)

baldosas = input().split()
defectuosas_1 = 0
defectuosas_final = 0

carrete = [0]*(sensor + 1)

defectuosas_final = repeticiones(baldosas)

if (sensor+1) < numero_Baldosas:
    for i in range(len(baldosas)):
        if i >= sensor:
            j = i
            k = 0

            for k in range(sensor, -1, -1):
                carrete[k] = baldosas[j]
                j -= 1
        
            defectuosas_1 += repeticiones(carrete)

if defectuosas_1 > defectuosas_final:
    defectuosas_1 = defectuosas_final

print(defectuosas_final, defectuosas_1, numero_Baldosas)