#Evaluacion realizada por Mauricio Henríquez.

import csv    #Conexión para trabajo con archivo separado por comas.



class Vehiculo:     #Creación de clase Vehiculo (esta sera la clase padre).
    def __init__(self, marca, modelo, n_ruedas):    #Metodo constructor de las instancias de la clase Vehículo.
        self.marca = marca
        self.modelo = modelo
        self.n_ruedas = n_ruedas

    def guardar_datos_csv(self):        #Metodo para la creación del documento csv 
        try:                #Introducción del codigo que podria generar fallas.
            with open("vehiculos.csv", "a", newline="") as archivo:     #Apertura de archivo csv, al ser llamado con el modo append ("a") si el archivo no existe sera creado por el programa.
                datos = [(self.__class__, self.__dict__)]
                archivo_csv = csv.writer(archivo)
                archivo_csv.writerows(datos)

        except FileNotFoundError:               #Definición de excepción en caso de que el archivo no se encuentre. 
            print("No existe el archivo vehiculos.csv")
        except Exception as e:          #Excepción para fallas no consideradas.
            print("Error no esperado",e)

    def leer_datos_csv(self):           #Metodo para la lectura del archivo csv.
        try:            #introducción de codigo que podria generar fallas.
            with open("vehiculos.csv", "r") as archivo:         #Llamado al archivo csv creado por el metodo guardar_datos_csv.
                    vehiculos = csv.reader(archivo)
                    print(f"Lista de vehiculos {type(self).__name__}")
                    
                    for item in vehiculos:                      #Este tramo de codigo es el que permite la impresión del contenido extraido  
                        vehiculo_tipo = str(self.__class__)     #del documento organizado por tipo de vehiculo.
                        if vehiculo_tipo in item[0]:
                            print(item[1])
                    
        except FileNotFoundError:           #Excepción para los casos en los que no se encuentre el documento.
                print("No existe el archivo vehiculos.csv")
        except Exception as e:              #Excepción para los errores no esperados o no definidos.
                print("Error no esperado:",e)


    def __str__(self):              #Sobrecarga al metodo STR de la clase Vehículo.
        return f'Marca del automóvil: {self.marca} Modelo: {self.modelo} Numero de ruedas: {self.n_ruedas}'

class Automovil(Vehiculo):          #Creación de la clase Automovil que hereda atributos de la clase Vehículo.
    def __init__(self, marca, modelo, n_ruedas, velocidad, cilindraje): #metodo creador de la clase.
        super().__init__(marca, modelo, n_ruedas)       #Atributos heredados desde la clase Vehículo.
        self.velocidad = velocidad
        self.cilindraje = cilindraje

    def __str__(self):          #Sobrecarga del metodo STR perteneciente a la clase Automovil.
        return super().__str__() + f'Velocidad: {self.velocidad} Km/h Cilindraje: {self.cilindraje}cc.'
    
class Particular(Automovil):        #Creacion de la subclase Particular que hereda atributos desde la clase Automovil.
    def __init__(self, marca, modelo, n_ruedas, velocidad, cilindraje, npuestos):   #Metodo constructor de la clase.
        super().__init__(marca, modelo, n_ruedas, velocidad, cilindraje)    #Atributos heredados desde la clase Automovil.
        self.npuestos = npuestos

    def get_npuestos(self):         #Metodo Accesador para la clase Particular.
        return self.npuestos
    
    def set_npuestos(self, npuestos_new):       #Metodo Mutador para la clase Particular.
        self.npuestos = npuestos_new

    def __str__(self):          #Sobre carga del metodo STR para la clase Particular.
        return super().__str__() + f"Puestos: {self.npuestos}"
    
class Carga (Automovil):        #Creacion de subclase Carga que hereda atributos de la clase Automovil.
    def __init__(self, marca, modelo, n_ruedas, velocidad, cilindraje, peso):       #Metodo creador de la clase.
        super().__init__(marca, modelo, n_ruedas, velocidad, cilindraje)            #Atributos Heredados de la clase Automovil.
        self.peso = peso


    def get_peso(self):         #Metodo accesador para la subclase Carga
        return self.peso
    
    def set_npuestos(self, peso_new):       #Metodo Mutador para la subclase Carga.
        self.peso = peso_new

    def __str__(self):      #Sobrecarga del metodo STR de la clase Carga.
        return super().__str__() + f"Carga: {self.peso}"
  
class Bicicleta(Vehiculo):      #Creación de la clase Bicicleta que hereda atributos de la clase Vehiculo.
    def __init__(self, marca, modelo, n_ruedas, tipo):  #Metodo creador de clase Bicicleta.
        super().__init__(marca, modelo, n_ruedas)      #Atributos heredados de la clase Vehiculo.
        self.tipo = tipo

    def __str__(self):      #Sobrecarga del metodo STR de la clase Bicicleta.
        return super().__str__() + f"Tipo: {self.tipo}"
    
class Motocicletas(Bicicleta):  #Creación de subclase Motocicletas que hereda atributos de la clase Bicicleta.
    def __init__(self, marca, modelo, n_ruedas, tipo, nro_radios, cuadro, motor):   #Metodo creador de la clase.
        super().__init__(marca, modelo, n_ruedas, tipo)     #Atributos heredados de la clase Bicicleta.
        self.nro_radios = nro_radios
        self.cuadro = cuadro
        self.motor = motor

    def __str__(self):      #Sobre carga del metodo STR de la clase Motocicletas.
        return super().__str__() + f"Numero de radios: {self.nro_radios} Cuadro: {self.cuadro} Motor: {self.motor}"
    