from clase import *

particular = Particular("Ford", "Fiesta", 4, "180", "500", 5)
carga = Carga("Daft Trucks", "G 38", 10, 120, "1000", "20000")
bicicleta = Bicicleta("Shimano", "MT Ranger", 2, "Carrera")
motocicleta = Motocicleta("BMW", "F800s",2,"Deportiva","2T","Doble Viga", 21)

print(particular)
print(carga)
print(bicicleta)
print(motocicleta)

print(isinstance(motocicleta,Vehiculo))
print(isinstance(motocicleta,Automovil))
print(isinstance(motocicleta,Particular))
print(isinstance(motocicleta,Carga))
print(isinstance(motocicleta,Bicicleta))
print(isinstance(motocicleta,Motocicleta))


