"""

primero poner el  cwebp.exe en windows

uso de script:
ejecutar desde la consola

# cmd> python cwebp_compressor_dir.py folder-name 80

"""

import sys,os
import time
import slug
from subprocess import call
from glob import glob

CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))

##--------start funciones Mia
def NameImgToWebp_Slug(nameImg):
    name = nameImg.split('.')[0]
    name = slug.slug(name)
    return name+'.webp'
##--------end funciones Mia




#folder-name
path_file = sys.argv[1]
#quality of produced .webp images [0-100]
quality = 75

PATH_CWEBP = r"D:\repos\curso_python\Utilidades\convertir Imagen a Webp\cwebp.exe"
PATH_CWEBP =' \"'+PATH_CWEBP+'\" '

if int(quality) < 0 or int(quality) > 100:
    print("image quality out of range[0-100] ;/:/")
    sys.exit(0)


img_list = []
if os.path.isfile(path_file):
    if path_file.endswith(".jpg") or path_file.endswith(".png") or path_file.endswith(".jpeg"):

        img_list.append(path_file)
        #img_list.append(path_file.split('\\')[-1])
        print("Nombre de la imagen a convertir:",path_file.split('\\')[-1])
        print("Path file:",path_file)


# time.sleep(1)

print("-------------------------------------------------------------------------")
print("-----------------Ejecutamos el comando para Convertir---------------------")
print("-------------------------------------------------------------------------")

# print(img_list)   # for debug
for img_name in img_list:

    dirname = os.path.dirname(img_name)
    name_archivo =img_name.split('\\')[-1]

    print("dirname:",dirname)
    print("name_archivo:",name_archivo)

    # path_salida = dirname+ os.sep +(name_archivo.split('.')[0])+'.webp'
    path_salida = dirname+ os.sep +NameImgToWebp_Slug(name_archivo)

    #cmd='cwebp \"'+dirname+ os.sep +name_archivo+'\" -q '+str(quality)+' -o \"'+dirname+ os.sep +(name_archivo.split('.')[0])+'.webp\"'
    cmd=PATH_CWEBP+' \"'+dirname+ os.sep +name_archivo+'\" -q '+str(quality)+' -o \"'+path_salida+'\"'

    print("Comando a Ejcutar:",cmd)
    # running the above command
    call(cmd, shell=True)

# pause =input("enter]")