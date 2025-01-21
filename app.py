from conversor import Conversor
from servicos import Servicos
import customtkinter
from tkinter import filedialog
from tkinter import Tk
import os
import threading # Utilizado para poder gerar varios processamentos ao mesmo tempo sem que o app trave.

class Interface:
    def __init__(self):
        customtkinter.set_appearance_mode("Dark")  
        customtkinter.set_default_color_theme("dark-blue")  

        self.janela = customtkinter.CTk()
        self.janela.title("Conversor")
        self.janela.geometry("800x500")
        self.janela.resizable(False, False)  # Travar tamanho da janela

        # Frame Esquerdo (Menu Lateral)
        menu_lateral = customtkinter.CTkFrame(self.janela, width=200, corner_radius=0)
        menu_lateral.grid(row=0, column=0, sticky="ns")

        # Botões do Menu Lateral
        titulo_menu = customtkinter.CTkLabel(menu_lateral, text="Conversor", font=("Arial", 18))
        titulo_menu.pack(pady=20, padx=10)

        botoes_lateral = ["Conversor Imagem", "Conversor Videos"]

        for i in botoes_lateral:
            botao_home = customtkinter.CTkButton(menu_lateral, text=i, command=lambda opcao=i: self.clique_botao(opcao))
            botao_home.pack(pady=10, padx=10)

        # Configuração de redimensionamento
        self.janela.grid_columnconfigure(1, weight=1)
        self.janela.grid_rowconfigure(0, weight=1)

        self.arquivos_selecionados = []  

        self.janela.mainloop()

        self.opcao_produto = None

    def clique_botao(self, opcao):
        self.opcao_produto = None
        if opcao == "Conversor Imagem":
            self.opcao_produto = 1
        if opcao == "Conversor Videos":
            self.opcao_produto = 2
        self.gera_frame_principal()
    
    # Frame Principal (Conteúdo)
    def gera_frame_principal(self):
        if hasattr(self, 'frame_atual') and self.frame_atual is not None:
            self.frame_atual.destruir()
            
        frame_principal = customtkinter.CTkFrame(self.janela, fg_color="transparent")
        frame_principal.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)

        if self.opcao_produto == 1:
            frame_conversor = Servicos(frame_principal)
            frame_conversor.gerar_frame_conversor(self.atualizar_formato_de, self.atualizar_formato_para, self.selecionar_arquivos, self.converter_arquivos, self.opcao_produto)

            self.menu_suspenso_de = frame_conversor.menu_suspenso_de
            self.menu_suspenso_para = frame_conversor.menu_suspenso_para
            self.lista_arquivos = frame_conversor.lista_arquivos
            self.frame_atual = frame_conversor

        elif self.opcao_produto == 2:
            frame_conversor = Servicos(frame_principal)
            frame_conversor.gerar_frame_conversor_videos(self.atualizar_formato_de, self.atualizar_formato_para, self.selecionar_arquivos, self.converter_arquivos, self.opcao_produto)

            self.menu_suspenso_de = frame_conversor.menu_suspenso_de
            self.menu_suspenso_para = frame_conversor.menu_suspenso_para
            self.lista_arquivos = frame_conversor.lista_arquivos
            self.frame_atual = frame_conversor
            
        else:
            self.frame_atual = None

    def selecionar_arquivos(self):
        root = Tk()
        root.withdraw()  
        print(self.menu_suspenso_de.get())

        arquivos = filedialog.askopenfilenames(title=f"Selecione arquivos ({self.menu_suspenso_de.get()})",
        filetypes=[(f"Arquivos {self.menu_suspenso_de.get()}", f"*.{self.menu_suspenso_de.get().lower()}")])

        if arquivos:
            formato_selecionado = self.menu_suspenso_de.get().lower()

            arquivos_filtrados = [arquivo for arquivo in arquivos if arquivo.lower().endswith(f".{formato_selecionado}")]
            arquivos_incorretos = [arquivo for arquivo in arquivos if not arquivo.lower().endswith(f".{formato_selecionado}")]

            if arquivos_incorretos: 
                self.lista_arquivos.delete("1.0", "end")
                self.lista_arquivos.insert("end", "Erro: Um ou mais arquivos têm um formato incompatível!\n\n")
                self.lista_arquivos.insert("end", f"Os seguintes arquivos não são compatíveis com o formato {formato_selecionado.upper()}:\n\n")
                for arquivo in arquivos_incorretos:
                    self.lista_arquivos.insert("end", arquivo + "\n")
                self.arquivos_selecionados = []
                root.destroy()
                return

            # Se todos os arquivos forem compatíveis, salva e exibe na lista
            self.arquivos_selecionados = arquivos_filtrados
            self.lista_arquivos.delete("1.0", "end")
            for arquivo in self.arquivos_selecionados:
                self.lista_arquivos.insert("end", arquivo + "\n")

        root.destroy() 

    def atualizar_formato_de(self, escolha):
        self.menu_suspenso_de.set(escolha)
        self.arquivos_selecionados = []
        self.lista_arquivos.delete("1.0", "end")
        print(f"Formato de entrada atualizado para: {self.menu_suspenso_de.get()}")

    def atualizar_formato_para(self, escolha):
        self.menu_suspenso_para.set(escolha)
        print(f"Formato de saída atualizado para: {self.menu_suspenso_para.get()}")

    # Método que será chamado em uma thread separada
    def processar_arquivo(self, index, arquivo, tipo, lista_arquivos, menu_suspenso_para):
        caminho_arquivo = os.path.splitext(arquivo)[0] + f".{menu_suspenso_para.get().lower()}"
        nome_arquivo = os.path.basename(caminho_arquivo)

        try:
            arquivo_converter = Conversor(arquivo, tipo)
            converter = arquivo_converter.Converter(caminho_arquivo, menu_suspenso_para.get().lower())
            if converter == 'success':
                lista_arquivos.insert("end", f"Arquivo {nome_arquivo} - Conversão feita com sucesso!" + "\n")
                print(f"Arquivo {nome_arquivo} - Conversão feita com sucesso!")
        except Exception as e:
            print(f"Erro ao tentar acessar o Conversor: {e}")
            lista_arquivos.insert("end", f"Arquivo {nome_arquivo} - Erro ao tentar acessar o Conversor: {e}" + "\n")

    def converter_arquivos(self, opcao):
        tipo = 'imagem'
        if opcao == 2:
            tipo = 'video'

        if not self.arquivos_selecionados:
            self.lista_arquivos.delete("1.0", "end")
            print("Nenhum arquivo selecionado para conversão.")
            self.lista_arquivos.insert("end", "Nenhum arquivo selecionado para conversão." + "\n")
            return

        self.lista_arquivos.insert("end", f"=================================================================" + "\n")
    
        if len(self.arquivos_selecionados) > 1:
            self.lista_arquivos.insert("end", f"Convertendo {len(self.arquivos_selecionados)} arquivos..." + "\n")
            print(f"Convertendo {len(self.arquivos_selecionados)} arquivos...")
        else:
            self.lista_arquivos.insert("end", f"Convertendo {len(self.arquivos_selecionados)} arquivo..." + "\n")
            print(f"Convertendo {len(self.arquivos_selecionados)} arquivo...")

        for index, arquivo in enumerate(self.arquivos_selecionados):
            thread = threading.Thread(
                target=self.processar_arquivo, 
                args=(index, arquivo, tipo, self.lista_arquivos, self.menu_suspenso_para)
            )

            thread.start()

            if index == len(self.arquivos_selecionados) - 1:
                        self.arquivos_selecionados[:] = []


app = Interface()
