import os
import shutil

from_dir = "C:/Users/Rafael dos Anjos/Downloads"

to_dir = "C:/Projetos/Projeto 102/Arquivos_Documentos"

list_of_files = os.listdir(from_dir)

#print(list_of_files)


for file_name in list_of_files:
    name, estensao = os.path.splitext()

    if estensao == '':
        continue
    if estensao in ['.txt','.doc','.docx','.pdf']:
        path1 = from_dir + '/' + file_name
        path2 = to_dir + '/' + "Arquivos_Imagen"
        path3 = to_dir + '/' + "Arquivos_Imagen" + "/" + file_name
        if os.path.exists(path2):
            print("Movendo" + file_name + ".....")

            shutil.move(path1, path3)
        else:
          os.makedirs(path2)
          print( " Movendo " + file_name + "...")
          shutil.move(path1, path3)
