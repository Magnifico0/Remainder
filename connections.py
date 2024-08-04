#study_notes.py
#from ui_stacked_widget import Ui_MainWindow as W 
from stacked_widget_text_browser import Ui_MainWindow as W



#show_dictionary_page ve show_program_page i bu kısıma yaz 

#like this one you can divide your program into pieces 

class Connections:
    def __init__(self, main_window: W):
        self.main_window = main_window


    def show_dictionary_page(self):
        self.main_window.stackedWidget.setCurrentWidget(self.main_window.dictionary_page)

    def show_program_page(self):
        self.main_window.stackedWidget.setCurrentWidget(self.main_window.program_page)

    def show_study_notes(self):
        self.main_window.stackedWidget.setCurrentWidget(self.main_window.study_notes_page)

    def show_add_study_notes_page(self): 
        self.main_window.stackedWidget.setCurrentWidget(self.main_window.add_study_notes_page)

    def show_home_page(self):
        self.main_window.stackedWidget.setCurrentWidget(self.main_window.home_page)

    def show_dictionary_display_page(self):
        self.main_window.stackedWidget.setCurrentWidget(self.main_window.dictionary_display_page)    
