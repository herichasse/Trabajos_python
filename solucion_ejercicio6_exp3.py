import json
import csv

def leer_json(ruta_archivo):
    #Lee un archivo JSON y devuelve los datos.
    with open(ruta_archivo, 'r') as archivo:
        datos = json.load(archivo)
    return datos

def escribir_csv(datos, ruta_archivo):
    #Escribe los datos en un archivo CSV.
    with open(ruta_archivo, 'w', newline='') as archivo:
        escritor_csv = csv.writer(archivo)
        # Escribir encabezados
        escritor_csv.writerow(['nombre', 'calificacion'])
        # Escribir datos
        for estudiante in datos:
            escritor_csv.writerow([estudiante['nombre'], estudiante['calificacion']])

def main():
    ruta_json = 'C:\\Users\\hert6\\OneDrive\\Documentos\\DUOC\\Fundamentos de programacion\\python\\estudiantes.json'
    ruta_csv = 'C:\\Users\\hert6\\OneDrive\\Documentos\\DUOC\\Fundamentos de programacion\\python\\estudiantes.csv'
    
    # Leer datos del archivo JSON
    datos_estudiantes = leer_json(ruta_json)
    
    # Escribir datos en el archivo CSV
    escribir_csv(datos_estudiantes, ruta_csv)
    
    print(f"Datos escritos en {ruta_csv}")

if __name__ == "__main__":
    main()