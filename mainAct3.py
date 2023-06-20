from clase import *

import csv
def guardar(nombre_archivo, Automovil):
    archivo = open(nombre_archivo, "w")
    datos = []
    for auto in Automovil:
        datos.append((auto.__class__, auto.__dict__))
    archivo_csv = csv.writer(archivo)
    archivo_csv.writerows(datos)
    archivo.close()

def recuperar(nombre_archivo):
    vehiculos = []
    archivo = open(nombre_archivo, "r")
    archivo_csv = csv.reader(archivo)
    for vehiculo in archivo_csv:
        vehiculos.append(vehiculo)
    archivo.close()
    return vehiculos

particular = Particular("Ford", "Fiesta", "4", "180", "500", "5")
carga = Carga("Daft Trucks", "G 38", "10", "120", "1000", "20000")
bicicleta = Bicicleta("Shimano", "MT Ranger", 2, "Carrera")
motocicleta = Motocicleta("BMW", "F800s",2,"Deportiva","2T","Doble Viga", 21)
# automovil = Automovil("Ford", "Fiesta", "4", "180", "500")
# guardar("ejemplo.csv", particular)
try:
    guardar("ejemplo.csv", [carga,particular,bicicleta,motocicleta])
    automoviles = recuperar("ejemplo.csv")
except Exception as error:
    print('Ha ocurrido un error inesperado')



vehiculosParticulares = []
vehiculosCarga = []
vehiculosBicicleta = []
vehiculosMotocicleta = []

for automovil in automoviles:
    if len(automovil) > 0:
        if 'Carga' in automovil[0]:
            vehiculosCarga.append(automovil[1])
        if 'Particular' in automovil[0]:
            vehiculosParticulares.append(automovil[1])
        if 'Bicicleta' in automovil[0]:
            vehiculosBicicleta.append(automovil[1])
        if 'Motocicleta' in automovil[0]:
            vehiculosMotocicleta.append(automovil[1])

print(vehiculosBicicleta)
print(vehiculosCarga)
print(vehiculosMotocicleta)
print(vehiculosParticulares)
    
