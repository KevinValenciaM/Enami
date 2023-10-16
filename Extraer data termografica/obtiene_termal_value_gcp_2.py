#! /usr/bin/env python3
from ctypes.util import find_library
import numpy as np
import ctypes as ct
import cv2
import os
import datetime

from os import remove
from google.cloud import storage

#Establecer conexion con proyecto en gcp mediante archivo llave(.json)
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'credential_firebase.json'
storage_client = storage.Client()

#Funcion para subir archivos a bucket de gcp
def upload_to_bucket(blob_name, file_path, bucket_name):
    '''
    Upload file to a bucket
    : blob_name  (str) - object name
    : file_path (str)
    : bucket_name (str)
    '''
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(blob_name)
    blob.upload_from_filename(file_path, timeout=150) #timeout de aumento de espera de subida
    return blob

#Define EvoIRFrameMetadata structure for additional frame infos
class EvoIRFrameMetadata(ct.Structure):
     _fields_ = [("counter", ct.c_uint),
                 ("counterHW", ct.c_uint),
                 ("timestamp", ct.c_longlong),
                 ("timestampMedia", ct.c_longlong),
                 ("flagState", ct.c_int),
                 ("tempChip", ct.c_float),
                 ("tempFlag", ct.c_float),
                 ("tempBox", ct.c_float),
                 ]

if __name__ == "__main__":
        # load library
        if os.name == 'nt':
                #windows:
                #libir = ct.windll.LoadLibrary("c:\\irDirectSDK\\sdk\\x64\\libirimager.dll")
                #libir = ct.windll.LoadLibrary("c:/Users/pocct/Downloads/libirimager-8.8.5-windows/irDirectSDK/bin/x64/libirimager.dll")   
                libir = ct.windll.LoadLibrary("c:\\Users\\pocct\\Downloads\\libirimager-8.8.5-windows\\irDirectSDK\\sdk\\x64\\libirimager.dll")                
                #print('Estoy aqui')
                #libir = ct.CDLL(r"C:/Users/pocct/Downloads/libirimager-8.8.5-windows/irDirectSDK/x64/libirimager.dll") 
        else:
                #linux:
                libir = ct.cdll.LoadLibrary(ct.util.find_library("irdirectsdk"))

        #path to config xml file
        pathXml = ct.c_char_p(b'../config/generic.xml')

        # init vars
        pathFormat = ct.c_char_p()
        pathLog = ct.c_char_p(b'logfilename')
        #print('a la m')

        palette_width = ct.c_int()
        palette_height = ct.c_int()

        thermal_width = ct.c_int()
        thermal_height = ct.c_int()

        serial = ct.c_ulong()

        # init EvoIRFrameMetadata structure
        metadata = EvoIRFrameMetadata()

        # init lib
        ret = libir.evo_irimager_usb_init(pathXml, pathFormat, pathLog)
        if ret != 0:
                print("error at init")
                exit(ret)

        # get the serial number
        ret = libir.evo_irimager_get_serial(ct.byref(serial))
        print('serial: ' + str(serial.value))

        # get thermal image size
        libir.evo_irimager_get_thermal_image_size(ct.byref(thermal_width), ct.byref(thermal_height))
        print('thermal width: ' + str(thermal_width.value))
        print('thermal height: ' + str(thermal_height.value))

        # init thermal data container
        np_thermal = np.zeros([thermal_width.value * thermal_height.value], dtype=np.uint16)
        npThermalPointer = np_thermal.ctypes.data_as(ct.POINTER(ct.c_ushort))

        # get palette image size, width is different to thermal image width due to stride alignment!!!
        libir.evo_irimager_get_palette_image_size(ct.byref(palette_width), ct.byref(palette_height))
        print('palette width: ' + str(palette_width.value))
        print('palette height: ' + str(palette_height.value))

        # init image container
        np_img = np.zeros([palette_width.value * palette_height.value * 3], dtype=np.uint8)
        npImagePointer = np_img.ctypes.data_as(ct.POINTER(ct.c_ubyte))

        count=0
        # capture and display image till q is pressed
        while chr(cv2.waitKey(1) & 255) != 'q':
                #get thermal and palette image with metadat
                ret = libir.evo_irimager_get_thermal_palette_image_metadata(thermal_width, thermal_height, npThermalPointer, palette_width, palette_height, npImagePointer, ct.byref(metadata))

                if ret != 0:
                        print('error on evo_irimager_get_thermal_palette_image ' + str(ret))
                        continue
                #calculate total mean value
                mean_temp = np_thermal.mean()
                mean_temp = mean_temp / 10. - 100

                
                ##Segrabara cada 10 frames
                if count%480==0:
                    hora_actual = datetime.datetime.now()
                    hora_actual = hora_actual.strftime('%Y%m%d%H%M%S')
                    texto='C:/Users/pocct/Documents/Optris/'+hora_actual+".csv"
                    np.savetxt(texto, np_thermal, delimiter=";")
                    count=0
                    print('mean temp: ' + str(mean_temp))
                    upload_to_bucket('Optris/'+hora_actual+".csv", texto, 'enami-datos') #subir archivo a gcp
                    print("archivo", hora_actual+".csv", "en bucket")
                    remove(texto) #remover archivo despues de subir a gcp
                    print("archivo", hora_actual+".csv", "eliminado")
                count+=1
               
        # clean shutdown
        libir.evo_irimager_terminate()
