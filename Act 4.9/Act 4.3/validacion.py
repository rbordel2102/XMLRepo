import json
from jsonschema import validate

# Definir el esquema
schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
    "consesionario": {
    "type": "object",
    "minLength":1,
    "properties": {
    "coche": {
    "type": "array",
    "minLength":1,
    "items": {
    "type": "object",
    "properties": {
        "codigo": { "type": "string", "minLength":1 },
        "marca": { "type": "string" },
        "modelo": { "type": "string" },
        "matricula": { "type": "string" },
        "potencia": { "type": "string" },
        "plazas": { "type": "string" },
        "puertas": { "type": "string" }
    },
    "required": ["codigo"]
    }
    }
    },
    "required": ["coche"]
    }
    },
    "required": ["consesionario"]
}

# Archivo JSON a validar
archivo_json = '''
{
    "consesionario": {
       "coche": [
         {
           "codigo": "ABC123",
           "marca": "Toyota",
           "modelo": "Corolla",
           "matricula": "XYZ789",
           "potencia": "120",
           "plazas": "5",
           "puertas": "4"
         },
         {
           "codigo": "DEF456",
           "marca": "Volswagen",
           "modelo": "Polo",
           "matricula": "6038CZS",
           "potencia": "100",
           "plazas": "5",
           "puertas": "4"
         },
         {
           "codigo": "DEF456",
           "marca": "BMW",
           "modelo": "Serie 3",
           "matricula": "UVW012",
           "potencia": "200",
           "plazas": "4",
           "puertas": "5"
         }
       ]
    }
}  
'''

# Cargar el archivo JSON
datos_json = json.loads(archivo_json)

# Validar contra el esquema
validate(instance=datos_json, schema=schema)

#Este script de Python utiliza la biblioteca jsonschema para cargar el esquema y los datos JSON, 
#y luego realiza la validación. Si el archivo JSON cumple con el esquema, no se producirá ninguna excepción. 
#En caso contrario, se lanzará una excepción indicando la razón de la invalidación.