import kivy.app
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.metrics import Metrics

print(Metrics.density)

Window.size = (400, 300)


class MyApp(kivy.app.App):
    def build(self):
        layout = FloatLayout()
        btn = Button(text="Click me!", size_hint_max=("400dp", "300dp"))
        layout.add_widget(btn)
        return layout


if __name__ == '__main__':
    MyApp().run()
