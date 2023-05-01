from kivy.app import App
from kivy.uix.button import Button
from kivy.core.window import Window

Window.size = (400, 300)


class MyApp(App):
    def build(self):
        return Button(text="Click me!", on_press=lambda e: print("Button clicked"))


if __name__ == '__main__':
    MyApp().run()
