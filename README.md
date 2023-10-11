# Enami
## Documentación de procesos
### Introducción
Este repositorio contiene los distintos procesos asociados al proyecto "Pruebas de Nuevas Tecnologías Convertidor Teniente" para Enami desarrollado por Ntt Data....

### 1 Extraccion y guardado de data recolectada a travez de camaras termograficas

Este proceso consiste en extraer los datos de las camaras termograficas y guardarlas en la nube de google

Existen 2 procesos de extraccion de datos:

Descripcion de los procesos [Detalle](https://github.com/KevinValenciaM/Enami/blob/main/Extraer%20data%20termografica/README.md)

1. Extraccion de datos de camara hikvision
Codigo: [Hikvision](https://github.com/KevinValenciaM/Enami/blob/main/Extraer%20data%20termografica/hikvi_2_gcp_remove.py)
   
2. Extraccion de datos de camara Optris
Codigo: [Optris](https://github.com/KevinValenciaM/Enami/blob/main/Extraer%20data%20termografica/obtiene_termal_value_gcp_2.py)

### 2 Modelo de desgaste frontal y modelo de desgaste de toberas

### 3 Modelo de sugerencia operacional

Este proceso consiste en generar sugerencias en el control del proceso del Convertidor teniente de Enami a traves de datos de operacion recopilados.

-creacion de dataset con datos entregados por enami [Creación del set de datos](https://github.com/KevinValenciaM/Enami/blob/main/Modelo_de_sugerencia_operacional/README.md)  
-variables, limpieza y relleno de datos faltantes  
-estudio de correlacion  
-analisis de temporalidad  
-cruce de datos termograficos  

### 4 Modelo de prediccion de temperatura interna
