from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, SwapTransition 
from kivy.properties import ColorProperty

kv = Builder.load_file("GeoAssist.kv")

class LanguageWindow(Screen):
    pass

class ObjectWindow(Screen):
    pass

class CheatSheetWindow(Screen):
    pass

class AboutWindow(Screen):
    pass

class GeoAssist(App):
    def build(self):
        sm = ScreenManager(transition=SwapTransition())
        sm.add_widget(LanguageWindow(name='language'))
        sm.add_widget(ObjectWindow(name='object'))
        sm.add_widget(CheatSheetWindow(name='cheatsheet'))
        sm.add_widget(AboutWindow(name='about'))

        return sm

if __name__ == '__main__':
    GeoAssist().run()