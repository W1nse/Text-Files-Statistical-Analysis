
import kivy
from kivy.app import App 
from kivy.uix.label import Label 
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button  
from kivy.core.window import Window 
from kivy.clock import Clock


class IntroView(GridLayout):
    def __init__(self,app,**kwargs):
        super(IntroView, self).__init__(**kwargs)
        self.app =  app 
        #geometry 
        self.cols = 1
        self.rows = 1
        self.padding = 50
        Window.size = (400, 150)
        #view buttons
        self.load_text_btn = Button(text="Load Text File")
        self.load_text_btn.on_press = self.load_btn_func
        self.load_text_btn.height = 20
        self.add_widget(self.load_text_btn)
    
    def load_btn_func(self):
        Clock.schedule_once(self.app.switch_to_load_view,1)

