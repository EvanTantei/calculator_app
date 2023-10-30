import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window

#set app's size
Window.size = (500, 700)

Builder.load_file('calc.kv')

class MyLayout(Widget):
    def clear(self):
        self.ids.calc_input.text = '0'
    
class calcApp(App):
    def build(self):
        return MyLayout()
    
if __name__ == '__main__':
    calcApp().run()

