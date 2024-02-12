import json
from jsonschema import validate

# Definir el esquema
schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
    "DAM": {
    "type": "object",
    "minLength":1,
    "properties": {
    "alumno": {
    "type": "array",
    "minLength":1,
    "items": {
        "type": "object",
        "properties": {
        "NIF": { "type": "string", "minLength":1 },
        "resultado": { "type": "string", "minLength":1 },
        "observaciones": { "type": "string" },
        "IP": { "type": "string", "minLength":1 },
        "MAC": { "type": "string", "minLength":1 }
        },
    "oneOf": [
    { "required": ["IP"] },
    { "required": ["MAC"] }
    ],
    "required": ["NIF", "resultado"]
    }
    }
    },
    "required": ["alumno"]
    }
    },
    "required": ["DAM"]
}

# Archivo JSON a validar
archivo_json = '''
{
    "DAM": {
       "alumno": [
         {
           "NIF": "12345678A",
           "resultado": "apto",
           "observaciones": "Excelente desempeño en programación Java",
           "IP": "192.168.1.1"
         },
         {
           "NIF": "87654321B",
           "resultado": "No apto",
           "MAC": "00:1A:2B:3C:4D:5F"
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