import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window
import re
import math

#set app's size
Window.size = (500, 700)

Builder.load_file('calc.kv')

class MyLayout(Widget):
    #clear barfunction
    def remove(self):
        available = self.ids.calc_input.text
        #remove 1letter on the last text
        available = available[:-1]
        self.ids.calc_input.text = available
        #set the default text box when it"s all deleted
        if available == "":
            self.ids.calc_input.text = '0'

    def clear(self):
        self.ids.calc_input.text = '0'

    def button_press(self, button):
        #create a variable text calculator
        available = self.ids.calc_input.text

        if available == '0':
            self.ids.calc_input.text = ' '
            self.ids.calc_input.text = f'{button}'

        else:
            self.ids.calc_input.text = f'{available}{button}' 
    
    # adding math function

    def math_sign(self, sign):
        available = self.ids.calc_input.text
        self.ids.calc_input.text = f'{available}{sign}'


    def equals(self):
        # available_ess = self.ids.calc_input.text
        available = self.ids.calc_input.text
        #Grouping the operators and the numerators
        num_list = available.replace('+', ' ').replace('-', ' ').replace('/', ' ').replace('x', ' ').split()
        sign_list = available

        num_list2 = [int(num) for num in num_list]
        num_list2 = sorted(num_list2, reverse=True)
        num_list2 = [str(num) for num in num_list2]

        for num in num_list2:
            sign_list = sign_list.replace(num, ' ')

        sign_list = sign_list.split()


         
        #addition
        #modifikasi agar textbox bisa memuat banyak operasi sekaligus dan mengutamakan perkalian dan pembagian
        while("x" or "/" or  "+" or "-" in sign_list):
            if "x" in sign_list:
                #loop list 
                a = str(int(num_list[sign_list.index("x")]) * int(num_list[sign_list.index("x")+1]))
                num_list[sign_list.index("x")].replace(num_list[sign_list.index("x")], a)
                num_list.pop(sign_list.index("x")+1)
                sign_list.pop(sign_list.index("x"))

            elif "/" in sign_list:
                #loop list
                a = str(int(num_list[sign_list.index("/")]) / int(num_list[sign_list.index("/")+1]))
                num_list[sign_list.index("/")].replace(num_list[sign_list.index("/")], a)
                num_list.pop(sign_list.index("/")+1)
                sign_list.pop(sign_list.index("/"))

            elif "+" in sign_list:
                #loop list
                ans = str(int(num_list[sign_list.index("+")]) + int(num_list[sign_list.index("+")]))
                num_list.pop(sign_list.index("+"))
                num_list.pop(sign_list.index("+"))
                num_list.insert(sign_list.index("+"), ans)

                sign_list.pop(sign_list.index("+"))

            elif "-" in sign_list:
                 #loop list
                ans = str(int(num_list[sign_list.index("-")]) - int(num_list[sign_list.index("-")]))
                num_list.pop(sign_list.index("-"))
                num_list.pop(sign_list.index("-"))
                num_list.insert(sign_list.index("-"), ans)

                sign_list.pop(sign_list.index("-"))

        answer = num_list[0]
        self.ids.calc_input.text = answer


            
    def decimal(self):
        available = self.ids.calc_input.text
        if "." in available:
            pass 
        #add decimal to end of text
        available = f'{available}.'
        #display
        self.ids.calc_input.text = available

    def pos_neg(self):
        available = self.ids.calc_input.text

        if "-" in available:
            self.ids.calc_input.text = f'{available.replace("-", "")}'
        else:
            self.ids.calc_input.text = f'-{available}'

#main system generator
class calcApp(App):
    def build(self):
        return MyLayout()
    
if __name__ == '__main__':
    calcApp().run()

