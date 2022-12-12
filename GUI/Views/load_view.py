from kivy.uix.gridlayout import GridLayout 
from kivy.uix.button import Button 
from kivy.uix.filechooser import FileChooserIconView 
from kivy.clock import Clock


class LoadView(GridLayout):
    def __init__(self, app, **kwargs):
        super(LoadView, self).__init__(**kwargs)
        self.app = app 
        self.cols = 1

        #file chooser
        self.file_chooser = FileChooserIconView()
        self.add_widget(self.file_chooser)

        subgrid0 = GridLayout(cols=2,size_hint_y=None,height=50)

        #load button 
        self.load_btn = Button(text="Load")
        self.load_btn.on_press = self.load_action
        self.load_btn.background_color = (0,0,1,0.5)

        subgrid0.add_widget(self.load_btn)
        #cancel button
        self.cancel_btn = Button(text="Cancel")
        self.cancel_btn.on_press = self.cancel_action
        self.cancel_btn.background_color = (1,0,0,0.5)
        subgrid0.add_widget(self.cancel_btn)

        self.add_widget(subgrid0)
    
    def cancel_action(self):
        Clock.schedule_once(self.app.switch_to_main_view,0.5)
    
    def load_action(self):
        if len(self.file_chooser.selection)!=0:
            if self.file_chooser.selection[0][-4:] == ".txt":
                self.app.text_file_dir = self.file_chooser.selection[0]
                text_file = open(self.app.text_file_dir, mode="r")
                all_text = text_file.read()
                if all_text!="":
                    self.app.disable_main_view_ops = False
                text_file.close()
                self.app.analyzer.set_text(all_text)
                Clock.schedule_once(self.app.switch_to_main_view,0.5)
