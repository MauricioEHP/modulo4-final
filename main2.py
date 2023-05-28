#Evaluacion realizada por Mauricio Henríquez.


from vehiculo import *      #Se realiza la importacion de todas las clases del script vehiculo.py


#A continuación se crean objetos en 4 clases del script vehiculo.
particular = Particular("Ford", "Fiesta", 4, 180, 500, 5) 
carga = Carga("Daft Trucks", "G 38", 10, 120, 1000, 20000) 
bicicleta = Bicicleta("Shimano", "MT Ranger", 2, "Carrera") 
motocicleta = Motocicletas("BMW", "F800s",2,"Deportiva","2T","Doble Viga", 21) 

#A continuación se imprimen en consola los 4 objetos creados anteriormente. 
print(particular)
print(carga)
print(bicicleta)
print(motocicleta)

print("")       #Impresion de linea en blanco.

#A continuación se valida si el objeto creado para la clase Motocicleta es instancia para las otras Clases
# y se imprime por consola.
print("Motocicleta es instancia con relación a Vehículo: ",isinstance(motocicleta,Vehiculo))
print("Motocicleta es instancia con relación a Automovil: ",isinstance(motocicleta,Automovil))
print("Motocicleta es instancia con relación a Particular: ",isinstance(motocicleta,Particular))
print("Motocicleta es instancia con relación a Carga: ",isinstance(motocicleta,Carga))
print("Motocicleta es instancia con relación a Bicicleta: ",isinstance(motocicleta,Bicicleta))
print("Motocicleta es instancia con relación a Motocicleta: ",isinstance(motocicleta,Motocicletas))