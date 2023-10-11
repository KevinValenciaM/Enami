# Enami
## Documentación de procesos
### Introducción
Este repositorio contiene los distintos procesos asociados al pryecto "Pruebas de Nuevas Tecnologías Convertidor Teniente" para Enami desarrollado por Ntt Data....

### 1 Extraccion y guardados de data recolectada a travez de camaras termograficas
Existen 2 procesos de extraccion de datos:

Cada proceso extrae la informacion termografica de las camaras y las sube a un bucket de Google Cloud Platform.
Es necesario tener un archivo llave json del proyecto en gcp para subir los archivos:
Archivo llave: "archivo.json"

1. Extraccion a travez de camara hikvision
Codigo: #Heading 1 link [Hikvision](https://github.com/KevinValenciaM/Enami/blob/main/Extraer%20data%20termografica/hikvi_2_gcp_remove.py)
   
2. Extraccion a travez de camara Optris
Codigo: #Heading 1 link [Optris](https://github.com/KevinValenciaM/Enami/blob/main/Extraer%20data%20termografica/obtiene_termal_value_gcp_2.py)


