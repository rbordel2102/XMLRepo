import json
from jsonschema import validate

# Definir el esquema
schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
    "EdicionesAranda": {
    "type": "object",
    "properties": {
        "InformeRegionalVentas": {
        "type": "object",
        "properties": {
        "@fecha": { "type": "string", "format": "date" },
        "Descripcion": { "type": "string" },
        "Region": {
        "type": "object",
        "properties": {
            "Norte": { "$ref": "#/definitions/trimestre" },
            "Centro": { "$ref": "#/definitions/trimestre" },
            "Sur": { "$ref": "#/definitions/trimestre" }
            },
        "required": ["Norte", "Centro", "Sur"]
        }
        },
        "required": ["@fecha", "Descripcion", "Region"]
        }
         },
         "required": ["InformeRegionalVentas"]
       }
    },
    "definitions": {
    "trimestre": {
    "type": "object",
    "properties": {
    "Trimestres": {
    "type": "object",
    "properties": {
        "Trimestre1": { "$ref": "#/definitions/ventas" },
        "Trimestre2": { "$ref": "#/definitions/ventas" },
        "Trimestre3": { "$ref": "#/definitions/ventas" },
        "Trimestre4": { "$ref": "#/definitions/ventas" }
    },
    "required": ["Trimestre1", "Trimestre2", "Trimestre3", "Trimestre4"]
    }
    }
    },
    "ventas": {
    "type": "object",
    "properties": {
    "librosVendidos": { "type": "string" }
    },
    "required": ["librosVendidos"]
    }
    },
    "required": ["EdicionesAranda"]
}

# Archivo JSON a validar
archivo_json = '''
{
"EdicionesAranda": {
       "InformeRegionalVentas": {
         "@fecha": "30/12/2009",
         "Descripcion": "Informe de ventas para las regiones Norte, Centro y Sur",
         "Region": {
           "Norte": {
             "Trimestres": {
               "Trimestre1": {
                 "librosVendidos": "24000"
               },
               "Trimestre2": {
                 "librosVendidos": "38600"
               },
               "Trimestre3": {
                 "librosVendidos": ""
               },
               "Trimestre4": {
                 "librosVendidos": ""
               }
             }
           },
           "Centro": {
             "Trimestres": {
               "Trimestre1": {
                 "librosVendidos": ""
               },
               "Trimestre2": {
                 "librosVendidos": "16080"
               },
               "Trimestre3": {
                 "librosVendidos": "25000"
               },
               "Trimestre4": {
                 "librosVendidos": "29000"
               }
             }
           },
           "Sur": {
             "Trimestres": {
               "Trimestre1": {
                 "librosVendidos": "27000"
               },
               "Trimestre2": {
                 "librosVendidos": "31400"
               },
               "Trimestre3": {
                 "librosVendidos": "40100"
               },
               "Trimestre4": {
                 "librosVendidos": "30000"
               }
             }
           }
         }
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