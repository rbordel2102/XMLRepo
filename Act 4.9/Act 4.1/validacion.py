import json
from jsonschema import validate

# Definir el esquema
schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
    "libreria": {
    "type": "object",
    "properties": {
    "libro": {
    "type": "array",
    "items": {
    "type": "object",
    "properties": {
        "codigoLibro": { "type": "string" },
        "autor": { "type": "string" },
        "titulo": { "type": "string" },
        "editorial": { "type": "string" },
        "edicion": { "type": "string" },
        "fechaPublicacion": { "type": "string" },
        "ISBN": { "type": "string" },
        "NumeroPaginas": { "type": "string" }
               },
    "required": ["codigoLibro", "autor", "titulo", "editorial", "edicion", "fechaPublicacion", "ISBN", "NumeroPaginas"]
    }
    }
    },
    "required": ["libro"]
    }
    },
    "required": ["libreria"]
}

# Archivo JSON a validar
archivo_json = '''
{
    "libreria": {
       "libro": [
         {
           "codigoLibro": "1",
           "autor": "John Ronald Tolkien Reuel",
           "titulo": "El Señor de los Anillos: La Comunidad del Anillo",
           "editorial": "MINOTAURO",
           "edicion": "1",
           "fechaPublicacion": "18/09/2012",
           "ISBN": "9788445000663",
           "NumeroPaginas": "806"
         },
         {
           "codigoLibro": "2",
           "autor": "Stephen King",
           "titulo": "HOLLY",
           "editorial": "PLAZA Y JANES EDITORES",
           "edicion": "4",
           "fechaPublicacion": "21/09/2023",
           "ISBN": "9788401031113",
           "NumeroPaginas": "476"
         },
         {
           "codigoLibro": "10",
           "autor": "James Clear",
           "titulo": "HABITOS ATOMICOS",
           "editorial": "PLANETA",
           "edicion": "5",
           "fechaPublicacion": "08/09/2020",
           "ISBN": "9788418118036",
           "NumeroPaginas": "654"
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