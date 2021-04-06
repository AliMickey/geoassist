from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

class LanguageWindow(Screen):
    pass

class ObjectWindow(Screen):
    pass

class CheetSheetWindow(Screen):
    pass

class AboutWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("GeoCheater.kv")

class GeoCheaterApp(App):
    def build(self):
        return kv

if __name__ == "__main__":
    GeoCheaterApp().run()