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
        #addition
        answer = 0
            
        if "+" in available:
            num_list = available.split("+")
        
            for i in range(0, len(num_list)-1):
                if "%" in num_list[i]:
                    n = num_list[i].replace("%", " ")
                    num_list[i] = float(n) * 1/100 
            #loop list
            for element in num_list:
                answer = answer + float(element)

            if answer % 1 == 0:
                self.ids.calc_input.text = str(int(answer))
            else:
                self.ids.calc_input.text = str(answer)

        elif "-" in available:
            num_list = available.split("-")

            for i in range(0, len(num_list)-1):
                if "%" in num_list[i]:
                    n = num_list[i].replace("%", " ")
                    num_list[i] = float(n) * 1/100
            
            #loop list
            answer = float(num_list[0]) - float(num_list[1])

            if answer % 1 == 0:
                self.ids.calc_input.text = str(int(answer))
            else:
                self.ids.calc_input.text = str(answer)

        elif "x" in available:
            num_list = available.split("x")
            #loop list

            for i in range(0, len(num_list)-1):
                if "%" in num_list[i]:
                    n = num_list[i].replace("%", " ")
                    num_list[i] = float(n) * 1/100

            answer = 1.0
            for element in num_list:   
                answer = answer * float(element)
            
            if answer % 1 == 0:
                self.ids.calc_input.text = str(int(answer))
            else:
                self.ids.calc_input.text = str(answer)

        elif "/" in available:
            num_list = available.split("/")

            for i in range(0, len(num_list)-1):
                if "%" in num_list[i]:
                    n = num_list[i].replace("%", " ")
                    num_list[i] = float(n) * 1/100

            #loop list
            answer = float(num_list[0])**2
            for element in num_list:
                answer = answer / float(element)
            #display the answer into the text box
            
            if answer % 1 == 0:
                self.ids.calc_input.text = str(int(answer))
            else:
                self.ids.calc_input.text = str(answer)

    def decimal(self):
        available = self.ids.calc_input.text
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

    def percentage(self):
        available = self.ids.calc_input.text

        available = f'{available}%'

        self.ids.calc_input.text = available
#main system generator
class calcApp(App):
    def build(self):
        return MyLayout()
    
if __name__ == '__main__':
    calcApp().run()

