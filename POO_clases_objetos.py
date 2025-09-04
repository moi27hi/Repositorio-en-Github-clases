# Clases y objetos.

class celular:

    def __init__(self,marca,modelo, camara): #Aqui escribimos las propiedades que queremos que tenga el objeto.
        self.marca = marca 
        self.modelo = modelo 
        self.camara = camara
# Esta funcion se ejecutara siempre que creemos un objeto.
# Metodo constructor. Construye la clase.
# Self forma de hacer referencia a si mismo/ al mismo objeto.
# Propiedades - atributos de un objeto(color, edad, tipo de cabello, etc. )


    def llamar (self):
         print(f"Estas haciendo una llamada desde un: {self.modelo} ")

         # En los metodos tenemos que escribir siempre self para autoreferenciarnos.
    
    def cortar(self):
        print(f"Cortaste la llamada desde tu {self.modelo} ")

        # Tenemos que pasarles el parametro self.

celular1 = celular("Samsung","S23","48MP")
celular2 = celular("Apple","iPhone 12 Pro Max","96MP")

print(celular1.modelo)
print(f"El celular 2 es de la marca {celular2.marca}")
celular2.llamar()
celular1.cortar()
celular2.cortar()



