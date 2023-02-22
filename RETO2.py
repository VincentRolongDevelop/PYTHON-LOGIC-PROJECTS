distancia, velocidad_Maxima, tiempo = input().split()

distancia = float(distancia)
velocidad_Maxima = float(velocidad_Maxima)
tiempo = float(tiempo)

velocidad_Vehiculo = (distancia / 1000)/(tiempo/3600)

if(distancia<0 or velocidad_Maxima<0 or tiempo<0):
    print("ERROR")
elif(velocidad_Vehiculo<=velocidad_Maxima):
    print("OK")
elif(velocidad_Vehiculo>velocidad_Maxima and velocidad_Vehiculo<(velocidad_Maxima+velocidad_Maxima*0.2)):
    print("MULTA")
else:
    print("CURSO SENSIBILIZACION")
