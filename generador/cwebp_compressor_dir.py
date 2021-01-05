"""

primero poner el  cwebp.exe en windows

uso de script:
ejecutar desde la consola

# cmd> python cwebp_compressor_dir.py folder-name 80

"""

import sys
import time
from subprocess import call
from glob import glob

#folder-name
path = sys.argv[1]
#quality of produced .webp images [0-100]
quality = sys.argv[2]

if int(quality) < 0 or int(quality) > 100:
    print("image quality out of range[0-100] ;/:/")
    sys.exit(0)




print("-------------------------------------------------------------------------")
print("-----------------Filtramos solo las imagenes [jps,png]---------------------")
print("-------------------------------------------------------------------------")

img_list = []
for img_name in glob(path+'/*'):
    # se pueden utilizar más tipos de imágenes (bmp, tiff, gif)
    if img_name.endswith(".jpg") or img_name.endswith(".png") or img_name.endswith(".jpeg"):
        # extraer el nombre de las imágenes (image_name. [jpg | png]) de la ruta completa
        print("Nombre de la imagen a convertir:",img_name.split('\\')[-1])
        img_list.append(img_name.split('\\')[-1])

time.sleep(5)
print("-------------------------------------------------------------------------")
print("-----------------Ejecutamos el comando para Convertir---------------------")
print("-------------------------------------------------------------------------")

# print(img_list)   # for debug
for img_name in img_list:

    # aunque las posibilidades son muy menores, pero tenga mucho cuidado al modificar el siguiente código
    cmd='cwebp \"'+path+'/'+img_name+'\" -q '+quality+' -o \"'+path+'/'+(img_name.split('.')[0])+'.webp\"'

    print("Comando a Ejcutar:",cmd)
    # running the above command
    call(cmd, shell=False)
    # print(cmd)    # for debug


salida = input("Pulsar [enter para salir]")