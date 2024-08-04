from PySide6.QtWidgets import QApplication
from ui_stacked_widget import Ui_MainWindow
from home import MainWindow
import sys

app = QApplication(sys.argv)
app.setStyle("fusion")

window_ = MainWindow()
#window.show()
window_.showMaximized()

app.exec()  