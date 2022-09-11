import random

class chutenumero:
    def __init__(self):
        self.valor_aleatorio = 0
        self.valor_min = 1
        self.valor_max = 100
        self.tentar_dnv = True


    def iniciar(self):
        self.geradorn()
        self.pedirumvalor()
        try:
            while self.tentar_dnv == True:
                if int(self.valordochute) > self.valor_aleatorio:
                    print('Chute um valor mais baixo!')
                    self.pedirumvalor()
                elif int(self.valordochute) < self.valor_aleatorio:
                    print('Chute um valor mais alto!')
                    self.pedirumvalor()
                if int(self.valordochute) == self.valor_aleatorio:
                    self.tentar_dnv = False
                    print('Parabéns você acertou')

        except:
            print('Por Favor digitar apenas números!')
            self.iniciar()

    def pedirumvalor(self):
        self.valordochute = input('Chute um número: ')
    def geradorn(self):
        self.valor_aleatorio = random.randint(self.valor_min,self.valor_max)

chute = chutenumero()
chute.iniciar()
