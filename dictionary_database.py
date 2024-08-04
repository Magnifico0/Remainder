from stacked_widget_text_browser import Ui_MainWindow as W
from PySide6.QtSql import QSqlDatabase , QSqlQuery
from PySide6.QtCore import QDateTime ,Qt

class DictionaryDatabase:
    def __init__(self, window:W):
        self.window = window
        self.i = 0


#this is kindda working but there is no loop to have all words 
#also i need to take the others and 
        #i have to make a logic to having words like 8 days ago 3 days ago like this 
        """
        boş array oluştur ve o günden 8 gün öncesi ve diğer günlerin indexlerini kayit al aldiğin kaydi daha sonra indexleri üzerinden while gibi kullanabilirsin 
        bu bağlanti kismini da display edersin 
        """
    def get_word_from_database(self): #for words 
            
            note = []
            query = QSqlQuery()
            query_string = f"select word from sozluk" 
            query.prepare(query_string)
            query.exec()
            if query.exec():
                while query.next():
                    value  =query.value(0)
                    note.append(value)
            else:
                print("get_konu_adi_value_from_database ERROR", query.lastError().text())
            return note
    def get_mean_from_database(self): #for mean 
            
            note = []
            query = QSqlQuery()
            query_string = f"select mean from sozluk" 
            query.prepare(query_string)
            query.exec()
            if query.exec():
                while query.next():
                    value  =query.value(0)
                    note.append(value)
            else:
                print("get_konu_adi_value_from_database ERROR", query.lastError().text())
            return note
    def get_sentence_from_database(self): #for mean 
            
            note = []
            query = QSqlQuery()
            query_string = f"select sentence from sozluk" 
            query.prepare(query_string)
            query.exec()
            if query.exec():
                while query.next():
                    value  =query.value(0)
                    note.append(value)
            else:
                print("get_konu_adi_value_from_database ERROR", query.lastError().text())
            return note  
    def get_equivalent_from_database(self): #for mean 
            
            note = []
            query = QSqlQuery()
            query_string = f"select equivalent from sozluk" 
            query.prepare(query_string)
            query.exec()
            if query.exec():
                while query.next():
                    value  =query.value(0)
                    note.append(value)
            else:
                print("get_konu_adi_value_from_database ERROR", query.lastError().text())
            return note  

    def display_words_in_text_browser(self):
        self.word = self.get_word_from_database()  # Word list
        mean = self.get_mean_from_database()
        sentence = self.get_sentence_from_database()
        equivalent = self.get_equivalent_from_database()

        # Debugging: Print the lengths of all lists and the current index
        print(f"Index: {self.i}")
        print(f"Words: {len(self.word)}, Meanings: {len(mean)}, Sentences: {len(sentence)}, Equivalents: {len(equivalent)}")

        if self.i < 0 or self.i >= len(self.word):
            print("Index out of range. No more words to display.")
            return

        self.window.dictionary_word_text_browser.clear()
        self.window.dictionary_word_text_browser.append(self.word[self.i])

        if self.i < len(mean):
            self.window.dictionary_mean_text_browser.clear()
            self.window.dictionary_mean_text_browser.append(mean[self.i])

        if self.i < len(sentence):
            self.window.dcitionary_sentence_text_browser.clear()
            self.window.dcitionary_sentence_text_browser.append(sentence[self.i])

        if self.i < len(equivalent):
            self.window.dictionary_equivalent_text_browser.clear()
            self.window.dictionary_equivalent_text_browser.append(equivalent[self.i])

    
    """
    def display_words_in_text_browser(self): 
        self.word = self.get_word_from_database() #list object
        self.window.dictionary_word_text_browser.clear() #for word
        print(len(self.word))

        self.window.dictionary_word_text_browser.append(self.word[self.i])
         
        
        mean = self.get_mean_from_database()
        self.window.dictionary_mean_text_browser.clear() #for mean
        self.window.dictionary_mean_text_browser.append(mean[self.i])
        
        sentence = self.get_sentence_from_database()
        self.window.dcitionary_sentence_text_browser.clear() #i wrote wrong dictionary in qdesigner
        self.window.dcitionary_sentence_text_browser.append(sentence[self.i])
        
        equivalent = self.get_equivalent_from_database()
        self.window.dictionary_equivalent_text_browser.clear()
        self.window.dictionary_equivalent_text_browser.append(equivalent[self.i])

  
        
    
    def next_word(self):
         self.i+=1
         self.display_words_in_text_browser()
         

    def previous_word(self):
         self.i-=1
         self.display_words_in_text_browser()
    """
    def next_word(self):
        if self.i < len(self.word) - 1:
            self.i += 1
            self.display_words_in_text_browser()

    def previous_word(self):
        if self.i > 0:
            self.i -= 1
            self.display_words_in_text_browser()
  

    def set_label_words_label(self):
         word_number = len(self.word)
         word_number= str(word_number)

         current_word_index = self.i
         current_word_index+=1
         current_word_index = str(current_word_index)
         self.window.words_counter_current.setText(current_word_index)
         self.window.words_counter_label_all.setText(word_number)

#create some logic to implement one day ago, two day ago so on... 
#not sure how to do it but you can create new functions for all and another arrays when triggered when you clicked it or maybe could be some
#shortcut for it, needed to some research or smth 