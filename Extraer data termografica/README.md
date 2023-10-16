### Extraccion y guardado de Data en la nube

Existen 2 procesos de extraccion de datos, uno por camara termografica.  
1: proceso para camara [Hikvision](https://github.com/KevinValenciaM/Enami/blob/main/Extraer%20data%20termografica/hikvi_2_gcp_remove.py)  
2: proceso para camara [Optris](https://github.com/KevinValenciaM/Enami/blob/main/Extraer%20data%20termografica/obtiene_termal_value_gcp_2.py)  
Estos procesos consisten en extraer la informacion termografica de las camaras y subirlas a un bucket de Google Cloud Platform utilizando Python.

## Requeriemientos

Es necesario tener un archivo llave json del proyecto en gcp para subir los archivos: 
Archivo llave: "nombre_llave.json"

Ejecutado en Windows 10 pro
Python 3.7.9

Librerias necesarias:  
Proceso 1 Hikvision:  
cv2  
numpy  
hikvisionapi  
datetime  
time  
os  
google.cloud  

Proceso 2 Optris:  
from ctypes.util import find_library  # Necesaria para buscar libreria utilizada para la conexion con camara optris
numpy  
ctypes  
cv2  
os  
datetime  
google.cloud  

## Uso

Cada proceso se debe ejecutar de forma independiente.
El proceso 1 Hikvision guarda la informacion capturada por la camara en forma de video(.avi), este archivo es subido a la nube y posteriormente es borrado del disco.  
El proceso 2 Optris guarda la informacion capturada por la camara en formato csv, este archivo es subido a la nube y posteriormente es borrado del disco.

El codigo guarda los archivos en un bucket del proyecto data analytics brasil de Ntt

Los datos guardados cada dia por cada camara tienen un peso de alrededor de 12 GB.

Considerar posibles caidas del proceso debido a un tiempo de espera prolongado en alguna etapa de los procesos, esto puede ser causado po una baja velocidad de conexion a  internet. El tiempo de espera para subir un archivo a gcp es de maximo 2 minutos 30 segundos (se puede cambiar).
