import os


class Organizador:

    def __init__(self):
        
        self.path = os.path.join(input('Digite o caminho para organizar:'))

        self.EXTS = {

                    'Arquivos': ['.zip', '.pdf', '.ggb', '.doc', ''], 
                    'Música': ['.mp3', '', ''], 
                    'Executáveis': ['.exe', '', ''], 
                    'Imagens': ['.jpg', '', ''], 
                    'Planilhas': ['.csv', '.xlsm', '.xls'], 
                    'Programação': ['.py', '.json', ''], 
                    '': [], 
                    }


    def mostrar_extensoes(self):

        arquivos = os.listdir(self.path)

        for arquivo in arquivos:

            posicao = arquivo.rfind('.')
            
            nome_extensao = arquivo[posicao:].lower()

            print(nome_extensao)


    def criar_diretorios(self):
        
        arquivos = os.listdir(self.path)

        for nome in self.EXTS.keys():

            if nome not in arquivos:
                
                os.mkdir(nome)


org = Organizador()

org.mostrar_extensoes()