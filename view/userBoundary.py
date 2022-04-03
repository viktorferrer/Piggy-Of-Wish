from unittest import result
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from matplotlib.pyplot import text

kivy.require('1.11.1')
__version__ = "0.1"

class telaInicial(Screen):
    pass

class cadUser(Screen):
    pass

class listarUser(Screen):
    pass

class gerenciarTela(ScreenManager):
    def telaInicial(self):
        self.current - "TelaInicial"
    
    def telaCadUser(self):
        self.current = "CadastrarUser"
    
    def telaListarUser(self):
        self.current = "ListarUser"
    

class crud(App):
    def build(self):
        self.root = gerenciarTela()
        return self.root

if __name__ == '__main__':
    crud().run()



    # def cadastrar(self):
    #     result = ""
    #     try:
    #         tela = self.get_screen("CadastrarUser")
    #         nome = tela.ids.inputNome,text