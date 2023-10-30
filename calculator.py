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
        available_ess = self.ids.calc_input.text
        available = self.ids.calc_input.text
        answer = 0
        num_list  = available.split('+', '-', '/', '*')
        sign_list = available.split(num_list)
        
        #addition
        for element in sign_list:
            if "+" in sign_list:
                #loop list
                for element in num_list:
                    answer = answer + int(element)
    
                self.ids.calc_input.text = str(answer)

            elif "-" in available:
                num_list = available.split("-")
                 #loop list
                for element in num_list:
                    answer = answer - int(element)
                self.ids.calc_input.text = str(answer)

            elif "x" in available:
                num_list = available.split("x")
                #loop list
                for element in num_list:   
                    answer = answer * int(element)
                self.ids.calc_input.text = str(answer)

            elif "/" in available:
                num_list = available.split("/")
                #loop list
                for element in num_list:
                    answer = answer / int(element)
                #display the answer into the text box
                self.ids.calc_input.text = str(answer)
            
    def decimal(self):
        available = self.ids.calc_input.text
        if "." in available:
            pass 
        #add decimal to end of text
        available = f'{available}.'
        #display
        self.ids.calc_input.text = available



#main system generator
class calcApp(App):
    def build(self):
        return MyLayout()
    
if __name__ == '__main__':
    calcApp().run()

