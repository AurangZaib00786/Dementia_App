
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager,Screen



class Signup(Screen):
    pass

class Login(Screen):
    pass

class Main(Screen):
    pass

class Screenmanager(ScreenManager):
    pass

class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'BlueGray'
        return Builder.load_file('screens.kv')

if __name__ == '__main__':
   
    MainApp().run()