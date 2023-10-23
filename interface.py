from tkinter import *
from tkinter import filedialog, messagebox
from pasta import Pasta

COR_FUNDO = "#303030"
COR_BOTAO = "#b0b0b0"
COR_LETRA = "#f1f1f1"

class App(Tk):
    def __init__(self):
        super().__init__()
        self.title("Organizador de arquivos")
        self.minsize(500, 300)
        self.maxsize(500, 300)
        self.configure(bg=COR_FUNDO, pady=40, padx=10)
        self.__configurar_interface()

    def __configurar_interface(self):
        self.escolher_dir_inicial = Button(text="Pasta Origem", bg=COR_BOTAO,command=self.escolher_diretorio_inicial)
        self.escolher_dir_inicial.grid(column=0, row=0, pady=10)

        self.diretorio_inicial = Entry(self, width=50)
        self.diretorio_inicial.grid(column=1, row=0, pady=10, )

        self.escolher_dir_final = Button(text="Pasta Destino", bg=COR_BOTAO, command=self.escolher_diretorio_final)
        self.escolher_dir_final.grid(column=0, row=1, padx=20)

        self.diretorio_final = Entry(self, width=50)
        self.diretorio_final.grid(column=1, row=1, pady=20, )

        self.mover = Button(text="Mover / Organizar", command=self.mover_pasta, bg=COR_BOTAO)
        self.mover.grid(column=1, row=2)

    def escolher_diretorio_inicial(self):
        diretorio = filedialog.askdirectory(title="Escolha o diretorio")
        self.diretorio_inicial.insert(0, diretorio)

    def escolher_diretorio_final(self):
        diretorio = filedialog.askdirectory(title="Escolha o diretorio")
        self.diretorio_final.insert(0, diretorio)

    def mover_pasta(self):
        dir_inicial = self.diretorio_inicial.get()
        dir_final = self.diretorio_final.get()
        #print(dir_final)
        
        if dir_inicial != "" and dir_final != "": #verifica se os diretorios não estão vazios
            pasta = Pasta(dir_inicial, dir_final)
            checar_terminou = pasta.mover_pasta()
            
            if checar_terminou:
                messagebox.showinfo(title="Arquivos Movidos", message=f"Todos os arquivos foram Movidos\npara o diretorio {dir_final}")
            else:
                messagebox.showerror(title="Aviso", message="Houve algum erro no processo de transferencia\nverificar diretorio destino")
                
aplicativo = App()

aplicativo.mainloop()
