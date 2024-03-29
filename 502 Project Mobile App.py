import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class childApp(GridLayout):
    def __init__(self, **kwargs):
        super(childApp,self).__init__()
        self.cols = 2
        self.add_widget(Label(text = 'Student Name '))
        self.s_name = TextInput( )
        self.add_widget(self.s_name)

        # Name

        self.add_widget(Label(text='Student Class '))
        self.s_class = TextInput( )
        self.add_widget(self.s_class)

        # RollNo

        self.add_widget(Label(text='Student Roll number '))
        self.s_roll = TextInput()
        self.add_widget(self.s_roll)

        # Marks

        self.add_widget(Label(text='Student Total Marks '))
        self.s_marks = TextInput( )
        self.add_widget(self.s_marks)

        # Button

        self.press = Button(text = 'Click Me')
        self.press.bind(on_press = self.click_me)
        self.add_widget(self.press)

    # Stored Data in Backend

    def click_me(self, instance):
        print("Name of the Student is "+self.s_name.text)
        print("Class of the Student is "+self.s_class.text)
        print("Class of the Student is " + self.s_roll.text)
        print("Marks of the Student is "+self.s_marks.text)
        print(" ")

class parentApp(App):
    def build(self):
        return childApp()

if __name__ == "__main__":
    parentApp().run()