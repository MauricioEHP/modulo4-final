#Evaluacion realizada por Mauricio Henríquez.


from vehiculo import *      #Se importan todas las clases del script vehiculo

# A continuación se crean distintos objetos.
particular = Particular("Ford", "Fiesta", 4, 180, 500, 5) 
carga = Carga("Daft Trucks", "G 38", 10, 120, 1000, 20000) 
bicicleta = Bicicleta("Shimano", "MT Ranger", 2, "Carrera") 
motocicleta = Motocicletas("BMW", "F800s",2,"Deportiva","2T","Doble Viga", 21) 
# A continuación se imprimen los objetos previamente creados
print(particular)
print(carga)
print(bicicleta)
print(motocicleta)

print("")   #Solo imprime un espacio en blanco.

# Ahora se guardan los objetos creados para que se almacenen en el documento creado por el programa.
particular.guardar_datos_csv()
carga.guardar_datos_csv()
bicicleta.guardar_datos_csv()
motocicleta.guardar_datos_csv()

# Ahora se Imprimen los datos almacenados en el documento csv.
particular.leer_datos_csv()
carga.leer_datos_csv()
bicicleta.leer_datos_csv()
motocicleta.leer_datos_csv()
