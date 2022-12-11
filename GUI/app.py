import kivy
from kivy.app import App 
from kivy.uix.label import Label 
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button  
from kivy.uix.screenmanager import ScreenManager, Screen 
from GUI.Views.main_view import MainView
from GUI.Views.load_view import LoadView
from kivy.core.window import Window 

class MyApp(App):
    def __init__(self, **kwargs):
        super(MyApp, self).__init__(**kwargs)
        self.title = "Stats.txt"
        self.text_file_dir = ""
        Window.size = (800, 600)
    
    def build(self):

        self.screen_manager =ScreenManager()

        #main view
        self.main_view = MainView(self)
        screen0 = Screen(name="main")
        screen0.add_widget(self.main_view)
        self.screen_manager.add_widget(screen0)
        #load view 
        self.load_view = LoadView(self)
        screen1 = Screen(name="load")
        screen1.add_widget(self.load_view)
        self.screen_manager.add_widget(screen1)
        
        


        return self.screen_manager
    
    #screen switching functions
    def switch_to_load_view(self, dt=0):
        self.screen_manager.current = "load"
    
    def switch_to_main_view(self, dt=0):
        self.screen_manager.current = "main"