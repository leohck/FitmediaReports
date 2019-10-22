import os


class FileManager:

    __slots__ = ["caminho"]

    def __init__(self, caminho):
        self.caminho = caminho

    # Verificar a existencia de determinado arquivo
    def verificar_arquivo(self, nome_arquivo):
        arquivo = os.path.join(self.caminho, nome_arquivo)
        if not os.path.exists(self.caminho):
            os.makedirs(self.caminho)
        if not os.path.exists(arquivo):
            novo_arquivo = open(arquivo, 'w')
            novo_arquivo.close()
        return arquivo

    # Excluir arquivos não mais necessários
    def excluir_arquivo(self, nome_arquivo):
        arquivo = os.path.join(self.caminho, nome_arquivo)
        if os.path.exists(arquivo):
            os.remove(arquivo)
