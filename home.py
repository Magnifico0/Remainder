#home.py 
#diğer sayfalara taşınması gereken 11 logic kısım var yaklaşık 1.5 saatlik bir sürede tamamlanır 

from PySide6.QtWidgets import QMainWindow
from PySide6.QtGui import QAction

#from ui_stacked_widget import Ui_MainWindow
from connections import Connections
from time_connections import TimeConnection
from database_connections import DatabaseConnections
from PySide6.QtSql import QSqlDatabase ,QSqlQuery
from stacked_widget_text_browser import Ui_MainWindow
from dictionary_database import DictionaryDatabase




class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Remainder Application v2.0")
        self.stackedWidget.setCurrentWidget(self.home_page)

        #timer set 
        self.time_connection = TimeConnection(self)
        
        #connections
        self.connections = Connections(self) 
        self.dictionary_button.clicked.connect(self.connections.show_dictionary_page)
        self.program_button.clicked.connect(self.connections.show_program_page)             
        self.study_notes_button.clicked.connect(self.connections.show_study_notes)
        self.add_note_button.clicked.connect(self.connections.show_add_study_notes_page)
        self.add_notes_notes_button.clicked.connect(self.connections.show_study_notes)

        self.dictionary_read_words_button.clicked.connect(self.connections.show_dictionary_display_page)
        

        self.actionpages.triggered.connect(self.connections.show_home_page)
        self.actionDictionary.triggered.connect(self.connections.show_dictionary_page)
        self.actionPrograms.triggered.connect(self.connections.show_program_page)
        self.actionStudy_Notes.triggered.connect(self.connections.show_study_notes)
        
      


        #database connection 
        self.database = DatabaseConnections(self)
        self.add_note_button_2.clicked.connect(self.database.adding_into_db)
        self.database.set_combo_boxes() #burada run edildiği için display kısmı çalışıyor
        self.dictionary_add_word_button.clicked.connect(self.database.adding_into_dictionary_database)

        self.dictionary = DictionaryDatabase(self)
        self.dictionary.display_words_in_text_browser()
        self.dictionary_next_word_button.clicked.connect(self.dictionary.next_word)
        self.dictionary_previous_word_button.clicked.connect(self.dictionary.previous_word)
       
        #to set words counter --> to set like 7/23
        self.dictionary_read_words_button.clicked.connect(self.dictionary.set_label_words_label)
        self.dictionary_previous_word_button.clicked.connect(self.dictionary.set_label_words_label)
        self.dictionary_next_word_button.clicked.connect(self.dictionary.set_label_words_label)


        #like this code you can create another functions to work for this one and will add to list them 
        self.actionOne_Day_Ago.triggered.connect(self.dictionary.previous_word)
        

        

 
       
        
                              
