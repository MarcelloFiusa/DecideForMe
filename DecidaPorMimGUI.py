import random
import PySimpleGUI as sg


class DecidaPorMim:
    def __init__(self):
        self.respostas = [
            'Com certeza, Você deve fazer isso! ;)',
            'Não sei, você quem sabe :/',
            'Não faz isso! Melhor não D:',
            'Acho que Tá na hora certo, mete bronca!! :D'
        ]

    def Iniciar(self):
        #layout
        layout = [
            [sg.Text('Faça sua pergunta: ')],
            [sg.Input()],
            [sg.Output(size=(50,10))],
            [sg.Button('Decida por mim')]
        ]
        #criar janela
        self.janela = sg.Window('Decida por mim!', layout=layout)
        while True:
            #ler os valores
            self.eventos, self.valores = self.janela.Read()
            if self.eventos == 'Decida por mim':
                print(random.choice(self.respostas))


decision = DecidaPorMim()
decision.Iniciar()