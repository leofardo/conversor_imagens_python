import customtkinter
class Servicos:
    def __init__(self, frame):
        self.frame = frame

    def gerar_frame_conversor(self, atualizar_formato_de, atualizar_formato_para, selecionar_arquivos, converter_arquivos, opcao_produto):
        # Frame principal
        frame_conversor = self.frame

        # Título principal
        titulo_principal = customtkinter.CTkLabel(frame_conversor, text="Conversor de Imagem", font=("Arial", 24))
        titulo_principal.pack(pady=20)

        # Frame para opções (menus suspensos e botão)
        frame_conversor_opcoes = customtkinter.CTkFrame(master=frame_conversor, fg_color="transparent")
        frame_conversor_opcoes.pack(pady=20, padx=20)

        # Opções para os menus suspensos
        opcoes = ["JPG", "PNG", "GIF", "BMP"]

        # Largura padrão para todos os elementos
        elemento_width = 130
        elemento_height = 40

        # Menu Suspenso "De"
        self.menu_suspenso_de = customtkinter.CTkOptionMenu(
            master=frame_conversor_opcoes,
            values=opcoes,
            command=atualizar_formato_de,
            width=elemento_width,
            height=elemento_height,
            corner_radius=8,
            variable=customtkinter.StringVar(value="JPG")
        )
        self.menu_suspenso_de.grid(row=0, column=0, padx=10, pady=5)

        # Texto "para"
        texto_para = customtkinter.CTkLabel(frame_conversor_opcoes, text="para", font=("Arial", 16), width=10)
        texto_para.grid(row=0, column=1, padx=10, pady=5)

        # Menu Suspenso "Para"
        self.menu_suspenso_para = customtkinter.CTkOptionMenu(
            master=frame_conversor_opcoes,
            values=opcoes,
            command=atualizar_formato_para,
            width=elemento_width,
            height=elemento_height,
            corner_radius=8,
            variable=customtkinter.StringVar(value="PNG")
        )
        self.menu_suspenso_para.grid(row=0, column=2, padx=10, pady=5)

        # Botão para selecionar arquivos
        self.botao_selecionar = customtkinter.CTkButton(
            frame_conversor_opcoes,
            text="Selecionar Arquivos",
            command=selecionar_arquivos,
            width=elemento_width,
            height=elemento_height
        )
        self.botao_selecionar.grid(row=0, column=3, padx=10, pady=5)

        # Lista de arquivos selecionados
        self.lista_arquivos = customtkinter.CTkTextbox(frame_conversor, width=elemento_width*3.72, height=200)
        self.lista_arquivos.pack(pady=10)

        # Botão para converter arquivos
        botao_converter = customtkinter.CTkButton(
            frame_conversor, text="Converter Arquivos", command=lambda: converter_arquivos(opcao_produto), width=elemento_width*3.72,
            height=elemento_height
        )
        botao_converter.pack(pady=20)

        return frame_conversor, atualizar_formato_de, atualizar_formato_para, selecionar_arquivos, converter_arquivos, self.menu_suspenso_de, self.menu_suspenso_para, self.lista_arquivos

    def gerar_frame_conversor_videos(self, atualizar_formato_de, atualizar_formato_para, selecionar_arquivos, converter_arquivos, opcao_produto):
         # Frame principal
        frame_conversor = self.frame

        # Título principal
        titulo_principal = customtkinter.CTkLabel(frame_conversor, text="Conversor de Vídeo", font=("Arial", 24))
        titulo_principal.pack(pady=20)

        # Frame para opções (menus suspensos e botão)
        frame_conversor_opcoes = customtkinter.CTkFrame(master=frame_conversor, fg_color="transparent")
        frame_conversor_opcoes.pack(pady=20, padx=20)

        # Opções para os menus suspensos
        opcoes = ["MP4", "MKV", "AVI", "MOV"]

        # Largura padrão para todos os elementos
        elemento_width = 130
        elemento_height = 40

        # Menu Suspenso "De"
        self.menu_suspenso_de = customtkinter.CTkOptionMenu(
            master=frame_conversor_opcoes,
            values=opcoes,
            command=atualizar_formato_de,
            width=elemento_width,
            height=elemento_height,
            corner_radius=8,
            variable=customtkinter.StringVar(value="MP4")
        )
        self.menu_suspenso_de.grid(row=0, column=0, padx=10, pady=5)

        # Texto "para"
        texto_para = customtkinter.CTkLabel(frame_conversor_opcoes, text="para", font=("Arial", 16), width=10)
        texto_para.grid(row=0, column=1, padx=10, pady=5)

        # Menu Suspenso "Para"
        self.menu_suspenso_para = customtkinter.CTkOptionMenu(
            master=frame_conversor_opcoes,
            values=opcoes,
            command=atualizar_formato_para,
            width=elemento_width,
            height=elemento_height,
            corner_radius=8,
            variable= customtkinter.StringVar(value="MKV")
        )
        self.menu_suspenso_para.grid(row=0, column=2, padx=10, pady=5)

        # Botão para selecionar arquivos
        self.botao_selecionar = customtkinter.CTkButton(
            frame_conversor_opcoes,
            text="Selecionar Arquivos",
            command=selecionar_arquivos,
            width=elemento_width,
            height=elemento_height
        )
        self.botao_selecionar.grid(row=0, column=3, padx=10, pady=5)

        # Lista de arquivos selecionados
        self.lista_arquivos = customtkinter.CTkTextbox(frame_conversor, width=elemento_width*3.72, height=200)
        self.lista_arquivos.pack(pady=10)

        # Botão para converter arquivos
        botao_converter = customtkinter.CTkButton(
            frame_conversor, text="Converter Arquivos", command=lambda: converter_arquivos(opcao_produto), width=elemento_width*3.72,
            height=elemento_height
        )
        botao_converter.pack(pady=20)

        return frame_conversor, atualizar_formato_de, atualizar_formato_para, selecionar_arquivos, converter_arquivos, self.menu_suspenso_de, self.menu_suspenso_para, self.lista_arquivos

    def destruir(self):
            self.frame.destroy()

if __name__ == "__main__":
    print('Inicie o arquivo app.py')