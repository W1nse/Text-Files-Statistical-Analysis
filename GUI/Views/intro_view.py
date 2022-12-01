
import kivy
from kivy.app import App 
from kivy.uix.label import Label 
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button  


class IntroView(GridLayout):
    def __init__(self,**kwargs):
        super(IntroView, self).__init__(**kwargs)
        #geometry 
        self.cols = 1
        self.padding = 50
        self.spacing  = 20
        #view buttons
        self.load_text_btn = Button(text="Load Text File")
        self.load_text_btn.height = 20
        self.add_widget(self.load_text_btn)
