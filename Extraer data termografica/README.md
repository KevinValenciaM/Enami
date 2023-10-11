### Extraccion y guardado de Data en la nube

Existen 2 procesos de extraccion de datos, uno por camara termografica.
1: proceso para camara Hikvision
2: proceso para camara Optris
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
from ctypes.util import find_library  ## preguntar a Wilma por "libirimager.dll"
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

Considerar los datos guardados cada dia por cada camara tienen un peso de alrededor de 12 GB.
