#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Autor:Luisa Fernanda Buriticá Ruíz
# Fecha:22 junio de 2023
# Conctacto:fernanda.buritica@udea.edu.co


'''
Importante

1. Dentro de la carpeta path_in3 debe existir una carpeta llamada DatosMeteo+Nombre_estacion.
2. Recordar tener juntos los archivos AMSC.py y Procesamiento_AMSCP1.py
3. En la seccion 4 "PROCESOS" comentar usando el simbolo "#" las estaciones que no requiera procesar.

Ante alguna duda o error comunicarse al correo de contacto con el asunto "ERROR/ DUDA :AMSC Código de procesamiento archivos CSV".
'''

###############################################################################
# 1. LIBRERIAS
# 1.1 Librerías importadas
# 1.2 Modulos importados
from AMSC import resumen_estacion,resumen_estacion_andes,resumen_estacion_oriente,resumen_estacion_pb,resumen_estacion_sonson
###############################################################################
# 3. INFORMACIÓN DE ENTRADA

#command="sudo rm /media/luisa/Compartido/Luisa/1_Observaciones/DatosMeteoAerocivil/"
#subprocess.run(command, shell=True, check=True)
# 3.1 Direcciones de entrada y salida
path_in3= # Poner la dirección absoluta de la carpeta con los CSVs Ej. r"/media/usuario/AMSC/" 
path_out1= # Poner la dirección absoluta de la carpeta de salida. Ej. r"/media/usuario/AMSC/" 


# 3.2 Carpeta
# 3.3 Vectores
columnas=["Tiempo Sistema","Outside Temperature","Wind Speed","Wind Direction","Outside Humidity",
          "Barometer","Rain Rate","UV","Solar Radiation"]
columnas_xlsx=[
    "Date",
    "Time",
    "Out_Temp",
    "Hi_Temp",
    "Low_Temp",
    "Out_Hum",
    "Dew_Pt",
    "Wind_Speed",
    "Wind_Dir",
    "Wind_Run",
    "Hi_Speed",
    "Hi_Dir",
    "Wind_Chill",
    "Head_Index",
    "THW_Index",
    "THSW_Index",
    "Bar",
    "Rain",
    "Rain_Rate",
    "Solar_Rad",
    "Solar_Energy"
    ]
columnas_CSV=['Timestamp','Outdoor Temperature', 'Wind Speed','Wind Direction','Outdoor Humidity',
              'Barometric Pressure','Rain']
# 3.4 Bases de datos
###############################################################################
# 4. PROCESOS
#-----------------------------------------------------------------------------#

def Procesamiento_Datos_AMSC(Estacion):
    tipo1=["arboletes","caucasia","itm","santafe","turbo","yarumal"]
    if Estacion in tipo1:
        resumen_estacion(Estacion,path_in3,columnas,path_out1)
    if Estacion in ["andes"]:
        resumen_estacion_andes(Estacion,path_in3,columnas_xlsx,path_out1)
    if Estacion in ["oriente"]:
        print("Oriente")
        resumen_estacion_oriente(Estacion,path_in3,columnas,path_out1)
    if Estacion in ["pb"]:
        print("Puerto Berrio")
        resumen_estacion_pb(Estacion,path_in3,columnas_CSV,path_out1)
    if Estacion in ["sonson"]:
        resumen_estacion_sonson(Estacion,path_in3,columnas,path_out1)

Procesamiento_Datos_AMSC("arboletes")
Procesamiento_Datos_AMSC("caucasia")
Procesamiento_Datos_AMSC("itm")
Procesamiento_Datos_AMSC("santafe")
Procesamiento_Datos_AMSC("turbo")
Procesamiento_Datos_AMSC("yarumal")
Procesamiento_Datos_AMSC("andes")
Procesamiento_Datos_AMSC("oriente")
Procesamiento_Datos_AMSC("pb")
Procesamiento_Datos_AMSC("sonson")
###############################################################################
