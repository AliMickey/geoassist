from kivy.config import Config
Config.set('graphics', 'resizable', False)
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, SwapTransition 
from kivy.properties import StringProperty, ObjectProperty
from kivy.core.window import Window
from PIL import ImageGrab, Image
from shutil import copyfile
import sys, os
from languageDetection import langDetection
from objectDetection import objectDetection

#Window.clearcolor = (0.5, 0.5, 0.5, 1) #Window color
Window.size = (1024, 500)

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

kv = Builder.load_file(resource_path("resources/GeoAssist.kv"))


class LanguageWindow(Screen):
    outputString = StringProperty('')
    filePath = StringProperty('')
    imageActive = False

    def __init__(self, **kwargs):
        super(LanguageWindow, self).__init__(**kwargs)
        Window.bind(on_dropfile=self._on_file_drop)
        Window.bind(on_key_down=self._on_keyboard_down)

    def _on_keyboard_down(self, window, keycode, num, text, modifiers):
        # Paste
        if (self.manager.current == "language" and "ctrl" in modifiers and keycode == 118):
            self.im = ImageGrab.grabclipboard()
            if (self.im is not None):
                self.im.save(resource_path("resources/image.png"))
                self.imageActive = True
                self.updateImagePreview()            

    def _on_file_drop(self, window, file_path):
        if (self.manager.current == "language"):
            self.filePath = file_path.decode("utf-8")
            copyfile(self.filePath, resource_path("resources/image.png"))
            self.imageActive == True
            self.updateImagePreview()
    
    def updateImagePreview(self):
        self.ids.imgLang.source = resource_path("resources/image.png")
        self.ids.imgLang.reload()

    def languageDetect(self):
        self.outputString = ""
        self.outputString = langDetection()
        
    pass


class ObjectWindow(Screen):
    outputString = StringProperty('')
    filePath = StringProperty('')
    landmark = ObjectProperty(False)
    imageActive = False

    def __init__(self, **kwargs):
        super(ObjectWindow, self).__init__(**kwargs)
        Window.bind(on_dropfile=self._on_file_drop)
        Window.bind(on_key_down=self._on_keyboard_down)
        Window.bind(on_motion=self._on_mouse_input)

    def _on_keyboard_down(self, window, keycode, num, text, modifiers):
        # Paste
        if (self.manager.current == "object" and "ctrl" in modifiers and keycode == 118):
            self.im = ImageGrab.grabclipboard()
            if (self.im is not None):
                self.im.save(resource_path("resources/image.png"))
                self.imageActive = True 
                self.updateImagePreview()

    def _on_mouse_input(self, hit, type, motionevent):
        degree = 0
        if (self.imageActive == True and self.manager.current == "object"):
            if (motionevent.button == "scrolldown"):
                degree = 2
            elif (motionevent.button == "scrollup"):
                degree = -2
            Image.open(resource_path("resources/image.png")).rotate(degree).save(resource_path("resources/image.png"))
            self.updateImagePreview()

    def _on_file_drop(self, window, file_path):
        if (self.manager.current == "object"):
            self.filePath = file_path.decode("utf-8")
            copyfile(self.filePath, resource_path("resources/image.png"))
            self.imageActive = True
            self.updateImagePreview()

    def updateImagePreview(self):
        self.ids.imgObj.source = resource_path("resources/image.png")
        self.ids.imgObj.reload()

    def objectDetect(self):
        self.outputString = objectDetection(self.landmark.active)

    pass


# class CheatSheetWindow(Screen):
#     pass


class AboutWindow(Screen):
    pass


class GeoAssist(App):
    def build(self):
        sm = ScreenManager(transition=SwapTransition())
        sm.add_widget(LanguageWindow(name='language'))
        sm.add_widget(ObjectWindow(name='object'))
        #sm.add_widget(CheatSheetWindow(name='cheatsheet'))
        sm.add_widget(AboutWindow(name='about'))
       
        return sm

if __name__ == '__main__':
    GeoAssist().run()

#.exe Maker
#pyinstaller --noconfirm --onefile --windowed --icon "D:/Programming/Git/geoguessr-ml/resources/icon.ico" --name "GeoAssist" --add-data "D:/Programming/Git/geoguessr-ml/languageDetection.py;." --add-data "D:/Programming/Git/geoguessr-ml/objectDetection.py;." --add-data "D:/Programming/Git/geoguessr-ml/resources;resources/" --add-data "D:/Programming/Git/geoguessr-ml/libpng16-16.dll;." --add-data "D:/Programming/Git/geoguessr-ml/roots.pem;grpc/_cython/_credentials/"  "D:/Programming/Git/geoguessr-ml/main.py"