
#from ui_stacked_widget import Ui_MainWindow as W 
from stacked_widget_text_browser import Ui_MainWindow as W

from PySide6.QtCore import QTimer, QObject
from datetime import datetime
class TimeConnection(QObject):
    def __init__(self, main_window: W):
        super(TimeConnection, self).__init__(main_window)
        self.main_window = main_window
        timer = QTimer(self)
        timer.timeout.connect(self.update_time)
        timer.start(1)



    def update_time(self): 
        current_datetime = datetime.now() 
        self.main_window.lcd_number_date.setDigitCount(10)
        self.main_window.lcd_number_date.display(current_datetime.strftime("%d-%m-%Y"))
        self.main_window.lcd_number_date.display(current_datetime.strftime("%d-%m-%Y"))
        self.main_window.lcd_number_time.display(current_datetime.strftime("%H:%M"))

  
# time_connections.py

