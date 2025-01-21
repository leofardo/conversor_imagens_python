from PIL import Image
from moviepy.editor import VideoFileClip

class Conversor:
    def __init__(self, caminho_imagem, tipo):
        self.caminho_imagem = caminho_imagem
        self.tipo = tipo

        if self.tipo == 'imagem':
            try:
                self.imagem = Image.open(caminho_imagem)
            except Exception as e:
                self.imagem = None
                print(f"Erro ao carregar a imagem: {e}")
                return 'error_load'

    def Converter(self, caminho_saida, formato):
        print(self.tipo)
        if self.tipo == 'imagem':
            try:
                if formato == 'jpg':
                    formato = 'JPEG'
                if self.imagem.mode != "RGB":
                    self.imagem = self.imagem.convert("RGB") 

                self.imagem.save(caminho_saida, formato)
                print(f"A imagem foi convertida para {formato} e salva como {caminho_saida}.")
                return 'success'

            except Exception as e:
                print(f"Erro ao converter a imagem: {e}")
                return 'error_convert'
            
        if self.tipo == 'video':
            try:
                clip = VideoFileClip(self.caminho_imagem)
                clip.write_videofile(caminho_saida, codec="libx264")
                print(f"A imagem foi convertido para {formato} e salva como {caminho_saida}.")
                return 'success'
            except Exception as e:
                print(f"Erro ao converter o Vídeo: {e}")
                return 'error_convert'
        else:
            return '?'

if __name__ == "__main__":
    print('Inicie o arquivo app.py')
