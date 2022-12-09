import kivy
from kivy.app import App 
from kivy.uix.label import Label 
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button  
from kivy.uix.screenmanager import ScreenManager, Screen 
from GUI.Views.intro_view import IntroView
from GUI.Views.main_view import MainView
from GUI.Views.load_view import LoadView

class MyApp(App):
    def __init__(self, **kwargs):
        super(MyApp, self).__init__(**kwargs)
        self.title = "Stats.txt"
    
    def build(self):
        self.screen_manager =ScreenManager()

        #adding intro page to the UI
        self.intro_view = IntroView(self)
        screen0 = Screen(name="intro")
        screen0.add_widget(self.intro_view)
        self.screen_manager.add_widget(screen0)
        #load view 
        self.load_view = LoadView(self)
        screen1 = Screen(name="load")
        screen1.add_widget(self.load_view)
        self.screen_manager.add_widget(screen1)
        #main view
        self.main_view = MainView()
        screen2 = Screen(name="main")
        screen2.add_widget(self.main_view)
        self.screen_manager.add_widget(screen2)
        


        return self.screen_manager
    
    def switch_to_load_view(self, dt=0):
        self.screen_manager.current = "load"