### Extraccion y guardado de Data en la nube

Estos procesos consisten en extraer la informacion termografica de las camaras y subirlas a un bucket de Google Cloud Platform.


## Requeriemientos

Es necesario tener un archivo llave json del proyecto en gcp para subir los archivos: 
Archivo llave: "archivo.json"

Ejecutado en Windows 10 pro
Python 3.7.9

Librerias necesarias:
Hikvision:
import cv2
import requests
import numpy as np
from hikvisionapi import Client
import datetime
import time

import os
from os import remove
from google.cloud import storage

Optris:
from ctypes.util import find_library
import numpy as np
import ctypes as ct
import cv2
import os
import datetime

from os import remove
from google.cloud import storage



## Uso

Instrucciones sobre cómo usar el proyecto.
