from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, SwapTransition 
from kivy.properties import StringProperty
from kivy.core.window import Window
from PIL import ImageGrab
from shutil import copyfile
from languageDetection import langDetection
from objectDetection import objectDetection



kv = Builder.load_file("GeoAssist.kv")
#Window.clearcolor = (0.5, 0.5, 0.5, 1) #Window color
Window.size = (1024, 600)


class LanguageWindow(Screen):
    outputString = StringProperty('Output')
    filePath = StringProperty('')

    def __init__(self, **kwargs):
        super(LanguageWindow, self).__init__(**kwargs)
        Window.bind(on_dropfile=self._on_file_drop)
        Window.bind(on_key_down=self._on_keyboard_down)

    def _on_keyboard_down(self, window, keycode, num, text, modifiers):
        # Paste
        if (keycode == 118 and "ctrl" in modifiers):
            im = ImageGrab.grabclipboard()
            im.save('assets/image.png', 'PNG')
            print("yes")
            im.show()
            self.updateImagePreview()
        return True

    def _on_file_drop(self, window, file_path):
        self.filePath = file_path.decode("utf-8")
        copyfile(self.filePath, "assets/image.png")
        self.updateImagePreview()
    
    def updateImagePreview(self):
        self.ids.imgLang.source = "assets/image.png"
        self.ids.imgLang.reload()

    def languageDetect(self, slavic, nordicBaltic, SEA):
        selectedRegions = []
        if slavic:
            selectedRegions.append('slavic')
        if nordicBaltic:
            selectedRegions.append('nordicBaltic')
        if SEA:
            selectedRegions.append('SEA')
        self.outputString = langDetection(selectedRegions)
    pass

class ObjectWindow(Screen):
    outputString = StringProperty('Output')
    filePath = StringProperty('')

    def __init__(self, **kwargs):
        super(ObjectWindow, self).__init__(**kwargs)
        Window.bind(on_dropfile=self._on_file_drop)
        Window.bind(on_key_down=self._on_keyboard_down)

    def _on_keyboard_down(self, window, keycode, num, text, modifiers):
        if (keycode == 118 and "ctrl" in modifiers):
            print("yes")
        return True

    def _on_file_drop(self, window, file_path):
        self.filePath = file_path.decode("utf-8")
        copyfile(self.filePath, "assets/image.png")
        self.ids.imgObj.source = self.filePath
        self.ids.imgObj.reload()

    def objectDetect(self, bollard):
        if bollard:
            objectDetection()

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