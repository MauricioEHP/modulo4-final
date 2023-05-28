#Evaluacion realizada por Mauricio Henríquez.

from vehiculo import *      ##Se importan todas las clases del script vehiculo.py

instancias = []     #Se crea una lista en blanco.

n = int(input("Cuantos Vehículos desea insertar: "))        #Se solicita confirmar la cantidad de vehiculos que seran ingresados a la lista.

for i in range(n):      #Con en ciclo se consultan los datos de los automoviles a ingresar las veces indicadas por el usuario.
    print(f"Datos del automóvil {i+1}")
    marca = input("Inserte la marca del automóvil: ") 
    modelo = input("Inserte la modelo: ") 
    n_ruedas = int(input("Inserte la numero de ruedas: "))
    velocidad = int(input("Inserte la velocidad en Km/h: "))
    cilindraje = int(input("Inserte la cilindraje en cc: "))
    print("")
    auto= Automovil(marca, modelo, n_ruedas, velocidad, cilindraje)
    instancias.append(auto) 
# Acontinuación se imprimen los datos ingresados en la lista.
for index,item in enumerate(instancias):
    print(f"Datos del Automóvil {index + 1} : Marca {item.marca}, Modelo {item.modelo}, {item.n_ruedas} ruedas, {item.velocidad} Km/h, {item.cilindraje}cc")


