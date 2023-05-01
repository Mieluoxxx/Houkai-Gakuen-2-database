from kivy.app import App
from kivy.graphics import Color, Rectangle
from kivy.uix.widget import Widget


class MyApp(App):
    def build(self):
        w = Widget()
        with w.canvas:
            Color(1, 0, 1, 1)
            Rectangle(pos=[800, 800], size=[100, 100])
        return w


if __name__ == '__main__':
    MyApp().run()
