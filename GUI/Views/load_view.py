import kivy
from kivy.uix.gridlayout import GridLayout 
from kivy.uix.button import Button 
from kivy.uix.filechooser import FileChooserListView 
from kivy.uix.label import Label 
from kivy.clock import Clock

class LoadView(GridLayout):
    def __init__(self, app, **kwargs):
        super(LoadView, self).__init__(**kwargs)
        self.app = app 
        self.cols = 1

        self.file_chooser = FileChooserListView()
        self.add_widget(self.file_chooser)