from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class SplitItScreen(GridLayout):

    def __init__(self, **kwargs):
        super(SplitItScreen, self).__init__(**kwargs)
        self.cols = 3
        self.row_force_default=True
        self.row_default_height=40

        

        self.add_widget(Label(text='Items'))# Add the label
        self.newItemName = TextInput(multiline=False)
        self.add_widget(self.newItemName)
        self.newItemBtn = Button(text="+", width=5) # add the input value
        self.add_widget(self.newItemBtn)
        self.add_widget(Label(text='Add item'))


class SplititApp(App):
    def build(self):
        return SplitItScreen()


if __name__ == '__main__':
    SplititApp().run()
