
import cv2
import requests
import numpy as np
from hikvisionapi import Client
import datetime
import time

import os
from os import remove
from google.cloud import storage

#Establecer conexion con proyecto en gcp mediante archivo llave(.json)
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'credential_firebase.json'
storage_client = storage.Client()

#funcion para subir archivos a GCP
def upload_to_bucket(blob_name, file_path, bucket_name):
    '''
    Upload file to a bucket
    : blob_name  (str) - object name
    : file_path (str)
    : bucket_name (str)
    '''
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(blob_name)
    blob.upload_from_filename(file_path, timeout=150) # timeout=60 para aumentar el tiempo permitido de subida
    return blob

#Conexion con camara Hikvision y subir archivo a bucket en gcp

try:
    cam = Client('http://192.168.29.179', 'admin', 'researchlabs1')

    while True:
        hora_actual = datetime.datetime.now()
        hora_actual = hora_actual.strftime('%Y%m%d%H%M%S')
        texto = hora_actual + ".avi"
        video1 = cv2.VideoWriter(texto, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 1, (1280, 720))
        cont = 0
        while cont < 1500:
            try:
                vid = cam.Streaming.channels[202].picture(method='get', type='opaque_data')

                bytes = b''
                with open('screen.jpg', 'wb') as f:
                    for chunk in vid.iter_content(chunk_size=368):
                        bytes += chunk
                        a = bytes.find(b'\xff\xd8')
                        b = bytes.find(b'\xff\xd9')
                        if a != -1 and b != -1:
                            jpg = bytes[a:b + 2]
                            bytes = bytes[b + 2:]
                            i = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8), cv2.IMREAD_COLOR)
                            video1.write(i)
                cont += 1
            except Exception as e:
                print(f"Error: {e}")
                time.sleep(60) #espera de 1 min
                # se agrega un tiempo de espera
                pass
        cv2.destroyAllWindows()
        video1.release()
        upload_to_bucket('videos/'+ texto, texto, 'enami-datos') #subir archivo a gcp
        print("archivo", texto, "en bucket")
        remove(texto) #remover archivo despues de subir a gcp
        print("archivo", texto, "eliminado")
    #cv2.destroyAllWindows()
    #video1.release()
    
except KeyboardInterrupt:
    # Manejar la interrupción del usuario (Ctrl+C) si es necesario.
    cv2.destroyAllWindows()
    video1.release()
except Exception as e:
    print(f"Error general: {e}")
