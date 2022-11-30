import kivy
from kivy.app import App 
from kivy.uix.label import Label 
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button  
from kivy.uix.screenmanager import ScreenManager, Screen 
from GUI.Views.intro_view import IntroView
from GUI.Views.main_view import MainView

class MyApp(App):
    def __init__(self, **kwargs):
        super(MyApp, self).__init__(**kwargs)
        self.title = "Stats.txt"
    
    def build(self):
        self.screen_manager =ScreenManager()

        #adding intro page to the UI
        self.intro_view = IntroView()
        screen0 = Screen(name="intro")
        screen0.add_widget(self.intro_view)
        self.screen_manager.add_widget(screen0)
        #main view
        self.main_view = MainView()
        screen1 = Screen(name="main")
        screen1.add_widget(self.main_view)
        self.screen_manager.add_widget(screen1)

        return self.screen_manager