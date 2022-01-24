import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class SpartanGrid(GridLayout):
    def __init__(self,**kwargs):
        super(SpartanGrid, self).__init__()
        self.cols = 2
        self.add_widget(Label(text="Login Name:"))

        self.s_name = TextInput()
        self.add_widget(self.s_name)

        self.add_widget(Label(text="Password:"))

        self.p_name = TextInput()
        self.add_widget(self.p_name)

        self.press = Button(text="Click Here")
        self.press.bind(on_press=self.click_me)
        self.add_widget(self.press)

    def click_me(self,instance):
        print("Username "+self.s_name.text)
        print("Password " + self.p_name.text)

class RugvedDev(App):
    def build(self):
        return SpartanGrid()

if __name__ =="__main__":
    RugvedDev().run()
