class Vehiculo():
    def __init__(self,marca,modelo,numeroRuedas):
        self.marca = marca
        self.modelo = modelo
        self.numeroRuedas = numeroRuedas
    
    def __str__(self):
        return f'Marca: {self.marca}, Modelo: {self.modelo}, Número de ruedas: {self.numeroRuedas}'

class Automovil(Vehiculo):
    def __init__(self, marca, modelo, numeroRuedas,velocidad,cilindrada):
        super().__init__(marca, modelo, numeroRuedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    def __str__(self):
        return f'{super().__str__()}, Velocidad: {self.velocidad} km/h, Cilindrada: {self.cilindrada} cc.'

class Particular(Automovil):
    def __init__(self, marca, modelo, numeroRuedas, velocidad, cilindrada,puestos):
        super().__init__(marca, modelo, numeroRuedas, velocidad, cilindrada)
        self.puestos = puestos
    def __str__(self):
        return f'{super().__str__()}, Puestos: {self.puestos}'

# auto1 = Particular('Toyota','Hilux','4','190 km/h','1200 cc',4)
# print(auto1)

class Carga(Automovil):
    def __init__(self, marca, modelo, numeroRuedas, velocidad, cilindrada,carga):
        super().__init__(marca, modelo, numeroRuedas, velocidad, cilindrada)
        self.carga = carga
    def __str__(self):
        return f'{super().__str__()}, Carga: {self.carga} kilos'

class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, numeroRuedas, tipo):
        super().__init__(marca, modelo, numeroRuedas)
        self.tipo = tipo
    def __str__(self):
        return f'{super().__str__()}, Tipo: {self.tipo}'

class Motocicleta(Bicicleta):
    def __init__(self, marca, modelo, numeroRuedas, tipo,nroRadios,cuadro,motor):
        super().__init__(marca, modelo, numeroRuedas, tipo)
        self.nroRadios = nroRadios
        self.cuadro = cuadro
        self.motor = motor
    def __str__(self):
        return f'{super().__str__()}, Número de radios: {self.nroRadios}, Cuadro: {self.cuadro}, Motor: {self.motor}'
    

# issubclass(hijo,padre)
