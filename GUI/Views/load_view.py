import kivy
from kivy.uix.gridlayout import GridLayout 
from kivy.uix.button import Button 
from kivy.uix.filechooser import FileChooserListView 
from kivy.uix.label import Label 
from kivy.clock import Clock

class LoadView(GridLayout):
    def __init__(self, **kwargs):
        super(LoadView).__init__(**kwargs)
        self.file_chooser = FileChooserListView()
        self.add_widget(self.file_chooser)