import os
from kivy.app import App
from kivy.core.window import Window

os.environ['KIVY_IMAGE'] = 'pil'

Window.size = (400, 300)


class MyApp(App):
    pass


if __name__ == '__main__':
    MyApp().run()
