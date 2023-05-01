from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        title_bar = BoxLayout(size_hint_max_y='30dp')
        title_bar.add_widget(Button(text='Button 1'))
        title_bar.add_widget(Button(text='Button 2'))
        layout.add_widget(title_bar)
        layout.add_widget(TextInput(text='Hello World'))

        return layout


if __name__ == '__main__':
    MyApp().run()
