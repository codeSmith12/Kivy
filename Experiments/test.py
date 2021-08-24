from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.properties import (
    NumericProperty, ReferenceListProperty, ObjectProperty
)

class TestScreen(GridLayout):
    # layout = ObjectProperty(None) # self. is implied
    def __init__(self, **kwargs):
        super(TestScreen, self).__init__(**kwargs)
        self.scrollView = ScrollView(size_hint=(1, None), size=(Window.width, Window.height))
        self.layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
        self.layout.bind(minimum_height = self.layout.setter('height'))
        self.scrollView.add_widget(self.layout)

    def newItemWidget(self):
        print("Adding new item.")
        newItem = NewItem()
        self.layout.add_widget(newItem)
        print(newItem)

class NewItem(GridLayout):
    def __init__(self, **kwargs):
        super(NewItem, self).__init__(**kwargs)
        self.cols = 2
        self.name = ""
        self.btn = Button(text="Hello")
        self.cost = 0
        self.who = []


class TestApp(App):
    def build(self):
        return TestScreen()

if __name__ == '__main__':
    TestApp().run()
