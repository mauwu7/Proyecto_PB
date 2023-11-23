import Validaciones as val


def opciones(opc):
    if opc == 1:
        marca = val.valida_marca()
        tipo = val.valida_tipo()
        response = val.requests.get("http://makeup-api.herokuapp.com/api/v1/products.json?brand={}&product_type={}".format(marca,tipo))
        datos = val.cln_api(response.json())
        if len(datos) == 0:
            print("No hay informacion disponible para el maquillaje {} de la marca {}".format(tipo,marca)) 
            #ctrl = opc   #Parametro para la funcion 
            return val.no_datos(opc) #Se llama la funcion no_datos para el caso en el que no se tiene datos disponibles para la consulta, con la variable ctrl para determinar en que opcion entrara
        else:
            precios = []  # Se almacenan los datos extraidos de la API
            for i in range(len(datos)):
                precios.append(float(datos[i].get("price")))

            promedio = [val.mean(precios)] #Calcula el  promedio de los precios, que se define en principio como una lista para agregar otros posteriormente
            
            print("A continuacion se muestran los precios para la marca dada ")
            print(precios)
            n = val.save_o_del()
            if n == 1:
                with open("Precios","w") as doc:
                    doc.write("Marca: "+marca+"\n")
                    for i in range(len(precios)):
                        doc.write("Precio: "+str(precios[i])+"\n")
                    doc.write("|-------------------------|"+"\n")
                    doc.write("Promedio: "+ str(promedio[0])+"\n")
                    doc.write("|-------------------------|"+"\n")

                with open("Precios_bruto","w") as doc:
                    doc.write("Marca: "+marca+"\n")
                    for i in range(len(precios)):
                        doc.write(str(precios[i])+"\n")


            else:
                print("Se va a descartar la informacion y finalizará la ejecucio del programa")
                return None
            
            print("Promedio de precios: ",val.mean(precios))
            print("Moda de precios: ", val.mode(precios))
            print("Mediana de los precios", val.median(precios))
                  
            prom_total = val.n_consulta(tipo,promedio) #Se pasa el parametro del tipo de maquillaje elegido previamente dado que ahora solo se quiere conocer la marca, y la lista promedio
            return prom_total
        
    if opc == 2:
        etiqueta = val.valida_etiqueta()
        response = val.requests.get("https://makeup-api.herokuapp.com/api/v1/products.json?product_tags={}".format(etiqueta))
        datos = val.cln_api(response.json())

        precios = []
        
        for i in range(len(datos)):
            precios.append(float(datos[i].get("price")))
        print("A continuacion se presentan los precios de los productos con la etiqueta{}".format(etiqueta))
        print(precios)
        n = val.save_o_del()
        if n == 1:
            with open("Precios","w") as doc:
                doc.write("Etiqueta: "+etiqueta+"\n")
                for i in range(len(precios)):
                    doc.write("Precio: " + str(precios[i])+"\n")
        else:
            print("Se va a descartar la informacion y finalizara el programa")
            return None
        
        print("Promedio de precios: ",val.mean(precios))
        print("Moda de precios: ", val.mode(precios))
        print("Mediana de los precios", val.median(precios))
        
        return precios #Se regresan los precios que se obtuvieron del API