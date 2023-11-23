import Validaciones as f
import Consultas as c
import sys


if __name__ == '__main__':
    opcion = f.menu()  #Se llama a la funcion menu en Validaciones.py  para conocer las opciones disponibles para consulta de datos
    datos = c.opciones(opcion)  # El dato regresado por la funcion se almacena en la variable datos 
    if datos == None:
        sys.exit()
    else:
        ctrl = f.leer_archivo()
        if ctrl == 1:
            with open("Precios","r") as doc:
                for line in doc:
                    print(line)

    print("Grafica: ")
    f.grafica(datos,opcion)                       #Segundo parametro para la funcion grafica, que determina qué hacer
    archivo = f.registro_excel(datos,opcion)
    datos_leidos = f.leer_excel()
    
    for datos in datos_leidos:
        print(datos)