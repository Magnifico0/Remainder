from PySide6.QtWidgets import QGraphicsTextItem 
from PySide6.QtWidgets import QGraphicsScene
from PySide6.QtWidgets import QTextBrowser
from PySide6.QtCore import QDateTime ,Qt
from dictionary_database import DictionaryDatabase
 
from stacked_widget_text_browser import Ui_MainWindow as W

#duplicate connection error --> to fix it use close.database function or do not give a shit 
#from ui_stacked_widget import Ui_MainWindow as W

from PySide6.QtSql import QSqlDatabase , QSqlQuery
#home.py dosyası içerisindeki sql le alakalı bütün kısımları bi alana toplayıp yukarıdan aşağıya buraya geçir onlar karışık durursa geçiremeyebilirsin 
class DatabaseConnections():
    def __init__(self, window:W):
        self.window = window

        self.dictionary = DictionaryDatabase(self)

    
    #TextBrowser codes
    def display_notes_in_text_browser(self,selected_konu):
        notes = self.get_notes_from_database(selected_konu)
        self.window.textBrowser.clear()

        for note_text in notes:
            self.window.textBrowser.append(note_text)

#saving notes into database        
    def adding_into_db(self): 
        self.connect_to_db() 
        self.add_to_database()
        self.update_combo_box() #in the first opening home.py set combo box working, after you saved any note this updates database which taken info and setting again whenever you 
        #clicked save button, so in first opening set_combo_box working after you clicked save note button this logic working and updating combo boxes
        self.window.lineEdit.clear()
        self.window.lineEdit_2.clear()
        self.window.lineEdit_3.clear()
        self.window.textEdit.clear()

    def connect_to_db(self): #buradaki logic içerisine eğer açılmış db varsa bir şey yapmaması eğer yoksa açması , eğer açamazsa ise error vermesini gir 
        
            
        database = QSqlDatabase.addDatabase("QSQLITE")
        database.setDatabaseName("deneme_database_yeni.db")
        if not database.open():
            print("Veritabanına bağlanılamadı.")

    def add_to_database(self):
        ders = self.window.lineEdit.text()
        subject = self.window.lineEdit_2.text()
        konu_adi = self.window.lineEdit_3.text()
        note = self.window.textEdit.toPlainText()
        query = QSqlQuery()
        query.prepare("INSERT INTO study_notes (ders, subject, konu_adi, note) VALUES (:ders, :subject, :konu_adi, :note)")
        query.bindValue(":ders", ders)
        query.bindValue(":subject", subject)
        query.bindValue(":konu_adi", konu_adi)
        query.bindValue(":note", note)

        if query.exec():
            print("Veri başarıyla eklendi add_to_database.")  
        else:
            print("Veri eklenirken bir hata oluştu:", query.lastError().text())

    def add_to_dictionary_database(self):
        current_datetime = QDateTime.currentDateTime().toString('yyyy-MM-dd')
        word = self.window.dictionary_add_word_line_edit.text()
        mean = self.window.dictionary_add_mean_line_edit.text()
        equivalent = self.window.dictionary_add_equivalent_line_edit.text()
        sentence = self.window.dictionary_add_sentence_text_edit.toPlainText()
        query = QSqlQuery()
        query.clear()
        query.prepare("INSERT INTO sozluk (date_ , word, mean, equivalent,sentence) VALUES (:current_datetime, :word, :mean, :equivalent, :sentence)")
        query.bindValue(":current_datetime", current_datetime)
        query.bindValue(":word",word)
        query.bindValue(":mean", mean)
        query.bindValue(":equivalent",equivalent)
        query.bindValue(":sentence", sentence)
       
        if query.exec():
            print("Veri başarıyla eklendi. add_to_dictionary_database")
        else:
            print("Veri eklenirken bir hata oluştu:", query.lastError().text())
    def adding_into_dictionary_database(self):
        self.connect_to_db()
        self.add_to_dictionary_database()
        self.window.dictionary_add_word_line_edit.clear()
        self.window.dictionary_add_mean_line_edit.clear()
        self.window.dictionary_add_equivalent_line_edit.clear()
        self.window.dictionary_add_sentence_text_edit.clear()
    
    def get_ders_value_from_database(self):
        ders=[]
        query = QSqlQuery()
        query_string = "select distinct ders from study_notes"
        query.prepare(query_string)
        query.exec()
        if query.exec():
            while query.next():
                value = query.value(0)
                ders.append(value)
        else:
            print("Veritabanı sorgusu başarısız:", query.lastError().text())

        return ders
    
    def get_subject_value_from_database(self,ders):
        subject = []
        query = QSqlQuery()
        query_string  = f"select distinct subject from study_notes where ders  = '{ders}' " #will be like this and you have to change it 
        query.prepare(query_string)
        query.exec()
        if query.exec():
            while query.next():
                value = query.value(0)
                subject.append(value)
        else:
            print("get_subject_value_from_database  ERROR", query.lastError().text())
        return subject
    
    def get_konu_adi_value_from_database(self,subject):
        konu_adi = []
        query  =QSqlQuery()
        query_string = f"select distinct konu_adi from study_notes where konu_adi  = '{konu_adi}'"
        query.prepare(query_string)
        query.exec()
        if query.exec():
            while query.next():
                value  =query.value(0)
                konu_adi.append(value)
        else:
            print("get_konu_adi_value_from_database ERROR", query.lastError().text())
        return konu_adi
        
    def get_notes_from_database(self,not_adi):
        note = []
        query = QSqlQuery()
        query_string = f"select note from study_notes where konu_adi = '{not_adi}' "
        query.prepare(query_string)
        query.exec()
        if query.exec():
            while query.next():
                value  =query.value(0)
                note.append(value)
        else:
            print("get_konu_adi_value_from_database ERROR", query.lastError().text())
        return note
    
    

    
    def set_combo_boxes(self):  #it has red button for me causae get values part will change 
        self.connect_to_db()

       
        #get_values_from_database fonksiyonunu güncelleyerek belki hepsi için ayrı ayrı yazarak filtreleme kısmını yapabilirsin 
        ders_values = self.get_ders_value_from_database() #retuning ders
        self.window.lecture_combo_box.addItems(ders_values) 

        def update_subject_values(selected_ders):
            
            konu_value = self.get_subject_value_from_database(selected_ders) # buranın içerisine sql kodu yazılabiliyor 
            self.window.subject_combo_box.clear()
            self.window.subject_combo_box.addItems(konu_value)

        self.window.lecture_combo_box.currentTextChanged.connect(update_subject_values)  #bu kodu yukarı taşırsan hata verir   
            
        def update_konu_values(selected_subject):  # update_konu_values fonksiyonunu tanımladık
            konu_adi_value = self.get_konu_adi_value_from_database(selected_subject)
            self.window.note_name_combo_box.clear()
            self.window.note_name_combo_box.addItems(konu_adi_value)

            selected_konu = self.window.note_name_combo_box.currentText()
            self.display_notes_in_text_browser(selected_konu)
        self.window.subject_combo_box.currentTextChanged.connect(update_konu_values)

        self.window.note_name_combo_box.currentTextChanged.connect(self.display_notes_in_text_browser)
        
    def clear_combo_boxes(self):
        self.connect_to_db()
 

        self.window.lecture_combo_box.clear()
        self.window.subject_combo_box.clear()
        self.window.note_name_combo_box.clear()

    def update_combo_box(self):
        self.clear_combo_boxes()
        self.set_combo_boxes()
    
