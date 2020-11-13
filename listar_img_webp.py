"""

primero poner el  cwebp.exe en windows

uso de script:
ejecutar desde la consola

# cmd> python cwebp_compressor_dir.py folder-name 80

"""

import sys,os
import time
from subprocess import call
from glob import glob



plantilla ="""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="description" content="">
    <meta name="author" content="Mark Otto, Jacob Thornton, and Bootstrap contributors">
    <meta name="generator" content="Jekyll v3.8.5">
    <title>$TITLE$ | Starter Template · Bootstrap</title>

    <link rel="icon" type="image/png" href="https://www.nginx.com/wp-content/themes/nginx-new/assets/img/nginx-favicon.png">

    <meta name="title" content="Título de la WEB">
    <meta name="description" content="Descripción de la WEB">
    <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/css/bootstrap.min.css" rel="stylesheet" type="text/css"/>


    <style>

    </style>
</head>
<body>

<h1>Listado de Archivos Web</h1>

{{%LISTADO%}}


<script src="https://code.jquery.com/jquery-3.3.1.min.js"
        integrity="sha256-FgpCb/KJQlLNfOu91ta32o/NMZxltwRo8QtmkMRdAu8="
        crossorigin="anonymous"></script>

</body>
</html>
"""
#folder-name
path = r"D:\repos\web_cursos_geral\2020"
#quality of produced .webp images [0-100]



print("-------------------------------------------------------------------------")
print("-----------------Filtramos solo las imagenes [jps,png]---------------------")
print("-------------------------------------------------------------------------")

img_list = []

for dirpath, dirnames, filenames in os.walk(path,topdown=True):
    print('\nruta       :', dirpath)
    for img_name in filenames:
        # se pueden utilizar más tipos de imágenes (bmp, tiff, gif)
        # if img_name.endswith(".jpg") or img_name.endswith(".png") or img_name.endswith(".jpeg"):
        if img_name.endswith(".webp"):

            img_list.append(img_name)








#
# for img_name in glob(path+'/*'):
#     # se pueden utilizar más tipos de imágenes (bmp, tiff, gif)
#     if img_name.endswith(".jpg") or img_name.endswith(".png") or img_name.endswith(".jpeg"):
#         # extraer el nombre de las imágenes (image_name. [jpg | png]) de la ruta completa
#         print("Nombre de la imagen a convertir:",img_name.split('\\')[-1])
#         img_list.append(img_name.split('\\')[-1])


print("-------------------------------------------------------------------------")
print("-----------------Ejecutamos el comando para Convertir---------------------")
print("-------------------------------------------------------------------------")

# print(img_list)   # for debug

salida_html=''
for img_name in img_list:

    str ="https://cesar23.github.io/web_cursos_geral/2020/{}".format(img_name)
    str= '<a href="{}">{}</a> <br>'.format(str,str)
    print(str )
    salida_html+=str
    # running the above command
    # call(cmd, shell=False)
    # print(cmd)    # for debug

plantilla=plantilla.replace('{{%LISTADO%}}',salida_html)
with open('index.html', "w",encoding='utf-8') as file:
    file.write(plantilla)


# salida = input("Pulsar [enter para salir]")