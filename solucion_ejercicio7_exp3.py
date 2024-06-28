#ejercisio 7

import json

def leer_datos_json(archivo_json):
    with open(archivo_json, 'r') as file:
        datos = json.load(file)
    return datos

def buscar_persona(datos, nombre, apellido):
    for persona in datos:
        if persona['nombre'] == nombre and persona['apellido'] == apellido:
            return persona
    return None

def mostrar_datos(persona):
    if persona:
        for clave, valor in persona.items():
            print(f"{clave}: {valor}")
    else:
        print("Persona no encontrada")

def main():
    archivo_json = 'C:\\Users\\hert6\\OneDrive\\Documentos\\DUOC\\Fundamentos de programacion\\python\\personas.json'
    nombre_a_buscar = 'Juan'
    apellido_a_buscar = 'Perez'

    datos = leer_datos_json(archivo_json)
    persona = buscar_persona(datos, nombre_a_buscar, apellido_a_buscar)

    mostrar_datos(persona)

if __name__ == '__main__':
    main()