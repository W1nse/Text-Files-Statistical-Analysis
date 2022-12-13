import os
os.environ['KIVY_IMAGE'] = 'pil'
import kivy
from kivy.app import App 
from kivy.uix.screenmanager import ScreenManager, Screen 
from GUI.Views.main_view import MainView
from GUI.Views.load_view import LoadView
from kivy.core.window import Window 
from src.analyzer import Analyzer

class MyApp(App):
    def __init__(self, **kwargs):
        super(MyApp, self).__init__(**kwargs)
        self.title = "Stats.txt"
        self.text_file_dir = ""
        Window.size = (700, 750)
        self.analyzer = Analyzer()
        self.disable_main_view_ops = True
    
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
        if os.path.isfile(self.text_file_dir):
            self.main_view.current_file_label.text = self.text_file_dir
            self.main_view.graph_pmf_btn.disabled = self.disable_main_view_ops
            self.main_view.graph_cdf_btn.disabled = self.disable_main_view_ops
            self.main_view.graph_char_prop_btn.disabled = self.disable_main_view_ops
            self.main_view.top_n_btn.disabled = self.disable_main_view_ops
            if self.disable_main_view_ops==False:
                self.main_view.mean_label.text = str(round(self.analyzer.mean(),4))
                variance = self.analyzer.variance()
                self.main_view.variance_label.text = str(round(variance,4))
                if variance!=0:
                    self.main_view.skewness_label.text = str(round(self.analyzer.skewness(),4))
                    self.main_view.kurtosis_label.text = str(round(self.analyzer.kurtosis(),4))
                else:
                    self.main_view.skewness_label.text = "Undefined"
                    self.main_view.kurtosis_label.text = "Undefined"