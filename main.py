from clase import *

n = int(input('Cuantos vehiculos desea insertar: '))

vehiculos = []

while len(vehiculos) < n:
    print(f'Datos del automóvil: {len(vehiculos)+1}')
    marca = input('Inserte la marca del automóvil: ')
    modelo = input ('Inserte el modelo: ')
    numeroRuedas = int(input('Inserte el número de ruedas: '))
    velocidad = int(input('Inserte la velocidad en km/h: '))
    cilindraje = int(input('Inserte el cilindraje en cc: '))

    auto = Automovil(marca,modelo,numeroRuedas,velocidad,cilindraje)
    vehiculos.append(auto)

print('Imprimiendo por pantalla los Vehículos:')

i = 1
for vehiculo in vehiculos:
    print(f'Datos del automovil {i}: {vehiculo}')
    i += 1
