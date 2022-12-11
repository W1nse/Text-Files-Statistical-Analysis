import kivy
from kivy.app import App 
from kivy.uix.label import Label 
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button  
from kivy.clock import Clock
from kivy.properties import ListProperty
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle
from kivy.uix.textinput import TextInput
import matplotlib.pyplot  as plt
import numpy as np 


class CustomLabel(Label):
    def __init__(self, background_color, **kwargs):
        super(CustomLabel, self).__init__(**kwargs)
        self.background_color  = background_color
    def on_size(self, *args):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(self.background_color[0], self.background_color[1], self.background_color[2], self.background_color[3])
            Rectangle(pos=self.pos, size=self.size)

class MainView(GridLayout):
    def __init__(self, app, **kwargs):
        super(MainView, self).__init__(**kwargs)
        self.app = app
        #geometry 
        self.cols = 1
        self.padding = 25
        self.spacing  = 10

        self.add_widget(Label(text="Welcome to Stats.txt!",font_size='40sp'))
        #load section
        self.load_section = GridLayout()
        self.load_section.cols = 3
        self.load_section.rows = 1
        self.load_section.spacing = 10
        self.load_section.padding = 5
        self.current_file_label = Label(text="", size_hint_y = None, height=50)
        self.load_section.add_widget(Label(text=f"Opened File: ", size_hint_y = None, height=50))
        self.load_section.add_widget(self.current_file_label)

        self.load_text_btn = Button(text="Load Text File",size_hint_y = None, height=50)
        self.load_text_btn.on_press = self.load_btn_func
        self.load_section.add_widget(self.load_text_btn)

        self.stats_graphs_section = GridLayout(cols=2, size_hint_y = None, height = 420)
        #stats section
        self.stats_section = GridLayout(cols=2,size_hint_y = None, height = 420)
        self.stats_section.spacing = 10
        self.stats_section.padding = 5
    
        self.mean_label = CustomLabel(text=f"mean", color=(0,0,0,1), font_size='20sp', background_color=(1,1,1,1), size_hint_y=None, height=100)
        self.variance_label = CustomLabel(text=f"variance", color=(0,0,0,1), font_size='20sp', background_color=(1,1,1,1), size_hint_y=None, height=100)
        self.skewness_label = CustomLabel(text=f"skewness value",color=(0,0,0,1), font_size='20sp', background_color=(1,1,1,1), size_hint_y=None, height=100)
        self.kurtosis_label = CustomLabel(text=f"kurtosis value",color=(0,0,0,1), font_size='20sp', background_color=(1,1,1,1), size_hint_y=None, height=100)

        self.stats_section.add_widget(Label(text="Mean: ", font_size='20sp', size_hint_y=None, height=100))
        self.stats_section.add_widget(self.mean_label)
        self.stats_section.add_widget(Label(text="Variance: ", font_size='20sp', size_hint_y=None, height=100))
        self.stats_section.add_widget(self.variance_label)
        self.stats_section.add_widget(Label(text="Skewness: ", font_size='20sp', size_hint_y=None, height=100))
        self.stats_section.add_widget(self.skewness_label)
        self.stats_section.add_widget(Label(text="Kutosis: ", font_size='20sp', size_hint_y=None, height=100))
        self.stats_section.add_widget(self.kurtosis_label)


        #graphs buttons section
        self.graphs_section = GridLayout(cols=1,size_hint_y = None, height = 300)
        self.graphs_section.spacing = 20
        self.graphs_section.padding = 10

        self.graph_pmf_btn = Button(text = "Plot PMF", size_hint_y=None, height=80,background_color=(0,1,0,1), disabled=self.app.disable_main_view_ops)
        self.graph_pmf_btn.on_press = self.graph_pmf
        self.graph_cdf_btn = Button(text = "Plot CDF", size_hint_y=None, height=80,background_color=(0,0,1,1), disabled=(self.app.analyzer.text==""))
        self.graph_cdf_btn.on_press = self.graph_cdf
        self.graph_char_prop_btn = Button(text = "Plot Characters Probabilities", size_hint_y=None, height=80,background_color=(1,0.8,0,1), disabled=self.app.analyzer.text=="")
        self.graph_char_prop_btn.on_press = self.graph_probabilities
        self.graphs_section.add_widget(Label(text="Plots", font_size="30sp"))
        self.graphs_section.add_widget(self.graph_pmf_btn)
        self.graphs_section.add_widget(self.graph_cdf_btn)
        self.graphs_section.add_widget(self.graph_char_prop_btn)


        self.stats_graphs_section.add_widget(self.stats_section)
        self.stats_graphs_section.add_widget(self.graphs_section)
        #showing top n repreated characters section
        self.top_n_section = GridLayout(cols=3, size_hint_y = None, height = 100)
        self.top_n_section.spacing = 10
        self.top_n_section.padding = 5
        self.top_n_textinput = TextInput(text="Type n", size_hint_y = None, height = 50)
        self.top_n_btn = Button(text="Show",size_hint_y = None, height = 50, disabled=(self.app.analyzer.text==""))
        self.top_n_btn.on_press = self.show_top_n_func

        self.top_n_section.add_widget(Label(text="Top reapeated N characters", size_hint_y = None, height = 50))
        self.top_n_section.add_widget(self.top_n_textinput)
        self.top_n_section.add_widget(self.top_n_btn)

        self.add_widget(self.load_section)
        self.add_widget(self.top_n_section)

        self.add_widget(self.stats_graphs_section)

        
    def graph_pmf(self):
        X = [i for i in range(62)]
        Y = [self.app.analyzer.pmf(x) for x in X]
        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.stem(X, Y)
        plt.show()
    
    def graph_cdf(self):
        print(self.app.analyzer.pmf(0))
        X = np.arange(0,62,0.1).tolist()
        Y = [self.app.analyzer.cdf(x) for x in X]
        plt.xlabel("x")
        plt.ylabel("F(x)")
        plt.plot(X, Y)
        plt.show()
    
    def graph_probabilities(self):
        X = [i for i in range(62)]
        Y = [self.app.analyzer.pmf(x) for x in X]
        X = [self.app.analyzer.get_rv_char(x) for x in X]
        plt.xlabel("Character")
        plt.ylabel("Probability")
        plt.stem(X, Y)
        plt.show()
    
    def show_top_repeated_n(self):
        pass


    def show_top_n_func(self):
        print(self.top_n_textinput.text, self.top_n_btn.disabled)


    def load_btn_func(self):
        Clock.schedule_once(self.app.switch_to_load_view,1)