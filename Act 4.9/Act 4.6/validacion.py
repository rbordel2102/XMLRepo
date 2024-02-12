import json
from jsonschema import validate

# Definir el esquema
schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
    "modulosDAM": {
    "type": "object",
    "minLength":1,
    "properties": {
    "moduloProfesional": {
    "type": "array",
    "minLength":1,
    "items": {
        "type": "object",
        "properties": {
        "nombre": {
        "type": "string",
        "minLength":1
        },
        "contenidos": {
        "type": "object",
        "minLength":1,
        "properties": {
        "unidadDidactica": {
        "type": "array",
        "minLength":1,
        "items": {
        "type": "object",
        "properties": {
        "tipo": {
        "type": "string",
        "minLength":1
        },
        "descripcion": {
        "type": "string",
        "minLength":1
        }
        },
    "required": ["tipo", "descripcion"]
    }
    }
    },
    "required": ["unidadDidactica"]
    }
    },
    "required": ["nombre", "contenidos"]
    }
    }
    },
    "required": ["moduloProfesional"]
    }
    },
    "required": ["modulosDAM"]
}

# Archivo JSON a validar
archivo_json = '''
{
    "modulosDAM": {
       "moduloProfesional": [
         {
           "nombre": "Programación",
           "contenidos": {
             "unidadDidactica": [
               {
                 "tipo": "Teoría",
                 "descripcion": "Fundamentos de programación estructurada"
               },
               {
                 "tipo": "Práctica",
                 "descripcion": "Desarrollo de algoritmos en un lenguaje de programación"
               }
             ]
           }
         },
         {
           "nombre": "Bases de Datos",
           "contenidos": {
             "unidadDidactica": [
               {
                 "tipo": "Teoría",
                 "descripcion": "Modelado y diseño de bases de datos"
               },
               {
                 "tipo": "Práctica",
                 "descripcion": "Implementación y gestión de bases de datos"
               }
             ]
           }
         },
         {
           "nombre": "Entornos de Desarrollo",
           "contenidos": {
             "unidadDidactica": [
               {
                 "tipo": "Teoría",
                 "descripcion": "Configuración y uso de entornos de desarrollo integrado"
               },
               {
                 "tipo": "Práctica",
                 "descripcion": "Desarrollo y depuración de aplicaciones"
               }
             ]
           }
         },
         {
           "nombre": "Interfaces de Usuario",
           "contenidos": {
             "unidadDidactica": [
               {
                 "tipo": "Teoría",
                 "descripcion": "Diseño y evaluación de interfaces de usuario"
               },
               {
                 "tipo": "Práctica",
                 "descripcion": "Implementación de interfaces de usuario"
               }
             ]
           }
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