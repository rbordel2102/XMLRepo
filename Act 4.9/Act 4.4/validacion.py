import json
from jsonschema import validate

# Definir el esquema
schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
    "Gestoria": {
    "type": "object",
    "properties": {
    "Sede": {
    "type": "object",
    "properties": {
        "@codigo": { "type": "string" },
        "NombreEmpleado": { "type": "string" },
        "FechaAlta": { "type": "string", "format": "date" },
    "Cliente": {
    "type": "array",
    "items": {
    "type": "object",
    "properties": {
        "@codigo": { "type": "string" },
        "Descripcion": { "type": "string" },
        "NumViviendas": { "type": "string" },
        "vivienda": {
        "type": "object",
    "properties": {
        "@id": { "type": "string" },
        "CosteVivienda": { "type": "string" },
        "Resumen": { "type": "string" },
        "PlazoAlta": { "type": "string", "format": "date" }
    },
    "required": ["@id", "CosteVivienda", "Resumen", "PlazoAlta"]
    }
    },
    "required": ["@codigo", "Descripcion", "NumViviendas", "vivienda"]
    }
    }
    },
    "required": ["@codigo", "NombreEmpleado", "FechaAlta", "Cliente"]
    }
    },
    "required": ["Sede"]
    }
    },
    "required": ["Gestoria"]
}

# Archivo JSON a validar
archivo_json = '''
{
    "Gestoria": {
       "Sede": {
         "@codigo": "M8958438",
         "NombreEmpleado": "Empleado1",
         "FechaAlta": "2024-01-22",
         "Cliente": [
           {
             "@codigo": "ABC-123",
             "Descripcion": "Solvente",
             "NumViviendas": "2",
             "vivienda": {
               "@id": "001",
               "CosteVivienda": "200000",
               "Resumen": "Vivienda 1: Chalet, Vivienda 2: Chalet",
               "PlazoAlta": "2024-06-22"
             }
           },
           {
             "@codigo": "DEF-456",
             "Descripcion": "Insolvente",
             "NumViviendas": "1",
             "vivienda": {
               "@id": "002",
               "CosteVivienda": "50000",
               "Resumen": "Vivienda 1: Piso",
               "PlazoAlta": "2023-02-21"
             }
           }
         ]
       }
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