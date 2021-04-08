from kivy.app import App
from kivy.lang import Builder
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics.context_instructions import PopMatrix, PushMatrix
from kivy.graphics import Rotate
from kivy.uix.behaviors import ButtonBehavior

h = .05
w = h * 1.6

class IconButton(ButtonBehavior, Image):

    def __init__(self, angle=0, **kwargs):
        super(IconButton, self).__init__(**kwargs)

        self.rotate = Rotate(angle = angle)

        self.canvas.before.add(PushMatrix())
        self.canvas.before.add(self.rotate)
        self.canvas.after.add(PopMatrix())

        self.bind(pos=self.update_canvas)
        self.bind(size=self.update_canvas)

    def update_canvas(self, *args):
        self.rotate.origin = self.center         

    def on_press(event):
        event.source = event.img_dn
        print 'pressed'.format(event.id)

    def on_release(event):
        event.source = event.img_up
        print " released'.format(event.id)


class TestApp(App):

    def build(self):
        layout = FloatLayout()
        btn = IconButton(angle=-20, id='b1', size_hint=(h,w), pos_hint = {'center_x': .25, 'center_y': .9})
        btn.img_up = 'loudspeaker_red_32.png'
        btn.img_dn = 'loudspeaker_green_32.png'
        btn.source = btn.img_up

        layout.add_widget(btn)

        im = Image(id='i1', size_hint=(h,w), pos_hint = {'center_x': .25, 'center_y': .9})
        im.source = 'loudspeaker_blue_32.png'

        layout.add_widget(im)

        return layout

class MainApp(App):
    def build(self):
        layout = Builder.load_string("src")
        return layout


if __name__ == '__main__':
    TestApp().run()