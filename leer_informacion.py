def leer_informacion(archivo:str, formato:str):
    """Lee el contenido de un archivo previamente creado y muestra su contenido.
    Si el archivo no existe o no se encuentra, se captura una excepción FileNotFoundError y se informa al usuario.
   
    Args:
        archivo: nombre del archivo al cual se intenta acceder\n
        formato: formato del archivo al cual se intenta acceder
    """
    try:
        ruta = "./archivos/"
        nom_archivo = f"{archivo}.{formato}"
        path = ruta + nom_archivo
        
        with open(path, "r") as nuevo_archivo:
            print(f"El archivo {archivo}.{formato} ya existe, ha sido creado previamente")
            contenido = nuevo_archivo.readlines()
            for lineas in contenido:
                print(lineas.strip()) #funcion strip() elimina los espacios en blanco entre lineas.
                
         
    except FileNotFoundError:
        print(f"El archivo al cual intentas acceder no existe o no se encuentra dentro de la ruta especificada")

    except Exception as e:
        print("Error: ", e)
    
def main():
    """Función principal del programa que entrega los parametros necesarios para la posterior ejecución de la función leer_informacion().
    """
    nombre_archivo = "informacion"
    formato = "dat"    
    
    leer_informacion(nombre_archivo, formato)

#Ejecución de la funcion para correr el programa
main()