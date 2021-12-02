class arquivo:

    def __init__(self,valido =0,invalido=0):
        self.valido = valido
        self.invalido = invalido


    def criacao(self):
        #arquivo = open('leitor.txt', 'a+')
        arquivo.write('200.135.80.9\n')
        arquivo.write('192.168.1.1\n')
        arquivo.write('8.35.67.74\n')
        arquivo.write('257.32.4.5\n')
        arquivo.write('85.345.1.2\n')
        arquivo.write('1.2.3.4\n')
        arquivo.write('9.8.234.5\n')
        arquivo.write('192.168.0.256\n')

    def leitura(self):
        arquivo = open('leitor.txt','r')
        print(arquivo.read(), end='')
        arquivo.close()

    def validoinvalido(self):
        self.valido = ['200.135.80.9','192.168.1.1','8.35.67.74','1.2.3.4']
        self.invalido = ['257.32.4.5','85.345.1.2 ','9.8.234.5','192.168.0.256']
        alfa = []
        beta = []
        if self.valido != self.invalido :
            alfa.append(self.valido)
            print('[Endereços válidos]\n',alfa)
        else:
            pass
        if self.invalido != self.valido:
            beta.append(self.invalido)
            print('[Endereços invalidos]\n',beta)


a = arquivo()
#a.criacao()
a.leitura()
a.validoinvalido()