import os
from os import chdir, listdir


class Pasta():

    def __init__(self,diretorio_inicial, diretorio_final):
        self.dir_inicial = diretorio_inicial
        self.dir_final = diretorio_final
        self.__novo_diretorio = ""


    def __criar_pastas(self):
        chdir(self.dir_final)
        print(f"diretorio que eu querooo{self.dir_final}")
        nova_pasta = "Pasta_Organizada"
        if not os.path.exists(nova_pasta):
            os.mkdir(nova_pasta)
        diretorio = self.dir_final
        self.__novo_diretorio = f"{diretorio}/{nova_pasta}"
        chdir(self.__novo_diretorio)
        pastas = ["Audio", "Imagens", "Documentos", "Videos", "Outros"]

        for pasta in pastas:
            if not os.path.exists(pasta):
                os.mkdir(pasta)
            else:
                pass

        return self.__novo_diretorio


    def mover_pasta(self):
        self.__criar_pastas()
        arquivos = listdir(self.dir_inicial)
        for arquivo in arquivos:
            # print("entro aqui")

            if arquivo.endswith('.png') or arquivo.endswith('.jpg'):

                self.mover_arquivos(arquivo, "Imagens")

            elif arquivo.endswith('.mp3') or arquivo.endswith('.wave'):

                self.mover_arquivos(arquivo, "Audio")

            elif arquivo.endswith('.mp4') or arquivo.endswith('.mkv'):

                self.mover_arquivos(arquivo, "Videos")

            elif arquivo.endswith('.pdf') or arquivo.endswith('.doc') or arquivo.endswith(".xls") or arquivo.endswith(
                    ".csv") or arquivo.endswith(".docx"):

                self.mover_arquivos(arquivo, "Documentos")

            else:
                self.mover_arquivos(arquivo, "Outros")

        return True
    
    
    def mover_arquivos(self, arquivo, pasta):
        chdir(self.dir_inicial)
        os.system(f"move {arquivo} {self.__novo_diretorio}/{pasta}")




