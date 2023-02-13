import pickle

class Vehiculo():
    def __init__(self,color,modelo,marca):
        self.color = color
        self.modelo = modelo
        self.marca = marca
    def impr(self):
        return f'Marca: {self.marca}\nModelo: {self.modelo}\nColor: {self.color}'
        
moto = Vehiculo('Negro','Hornet','Honda')
print(moto.impr())

f = open('fichero_vehiculos.bin','rb')
moto = pickle.load(f)
f.close()
print(type(moto))
    
    