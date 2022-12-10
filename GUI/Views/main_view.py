import kivy
from kivy.app import App 
from kivy.uix.label import Label 
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button  


class MainView(GridLayout):
    def __init__(self, app, **kwargs):
        super(MainView, self).__init__(**kwargs)
        #geometry 
        self.cols = 1
        self.padding = 50
        self.spacing  = 20