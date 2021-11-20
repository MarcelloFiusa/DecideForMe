import random


class DecidaPorMim:
    def __init__(self):
        self.respostas = [
            'Com certeza, Você deve fazer isso! ;)',
            'Não sei, você quem sabe :/',
            'Não faz isso! Melhor não D:',
            'Acho que Tá na hora certo, mete bronca!! :D'
        ]

    def Iniciar(self):
        input('Faça sua pergunta: ')
        print(random.choice(self.respostas))
        

decision = DecidaPorMim()
decision.Iniciar()