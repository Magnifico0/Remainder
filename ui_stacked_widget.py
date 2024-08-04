# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'stacked_widget.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGraphicsView, QGridLayout,
    QLCDNumber, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QStatusBar, QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1179, 672)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.home_page = QWidget()
        self.home_page.setObjectName(u"home_page")
        self.gridLayout = QGridLayout(self.home_page)
        self.gridLayout.setObjectName(u"gridLayout")
        self.daily_to_do_list_graphics_view = QGraphicsView(self.home_page)
        self.daily_to_do_list_graphics_view.setObjectName(u"daily_to_do_list_graphics_view")
        sizePolicy.setHeightForWidth(self.daily_to_do_list_graphics_view.sizePolicy().hasHeightForWidth())
        self.daily_to_do_list_graphics_view.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.daily_to_do_list_graphics_view, 1, 1, 3, 2)

        self.dictionary_button = QPushButton(self.home_page)
        self.dictionary_button.setObjectName(u"dictionary_button")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.dictionary_button.sizePolicy().hasHeightForWidth())
        self.dictionary_button.setSizePolicy(sizePolicy1)
        self.dictionary_button.setMinimumSize(QSize(220, 150))

        self.gridLayout.addWidget(self.dictionary_button, 1, 0, 1, 1)

        self.lcd_number_date = QLCDNumber(self.home_page)
        self.lcd_number_date.setObjectName(u"lcd_number_date")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lcd_number_date.sizePolicy().hasHeightForWidth())
        self.lcd_number_date.setSizePolicy(sizePolicy2)
        self.lcd_number_date.setMinimumSize(QSize(450, 90))

        self.gridLayout.addWidget(self.lcd_number_date, 0, 2, 1, 1)

        self.study_notes_button = QPushButton(self.home_page)
        self.study_notes_button.setObjectName(u"study_notes_button")
        sizePolicy1.setHeightForWidth(self.study_notes_button.sizePolicy().hasHeightForWidth())
        self.study_notes_button.setSizePolicy(sizePolicy1)
        self.study_notes_button.setMinimumSize(QSize(0, 150))

        self.gridLayout.addWidget(self.study_notes_button, 2, 0, 1, 1)

        self.program_button = QPushButton(self.home_page)
        self.program_button.setObjectName(u"program_button")
        sizePolicy1.setHeightForWidth(self.program_button.sizePolicy().hasHeightForWidth())
        self.program_button.setSizePolicy(sizePolicy1)
        self.program_button.setMinimumSize(QSize(0, 150))

        self.gridLayout.addWidget(self.program_button, 3, 0, 1, 1)

        self.lcd_number_time = QLCDNumber(self.home_page)
        self.lcd_number_time.setObjectName(u"lcd_number_time")
        sizePolicy2.setHeightForWidth(self.lcd_number_time.sizePolicy().hasHeightForWidth())
        self.lcd_number_time.setSizePolicy(sizePolicy2)
        self.lcd_number_time.setMinimumSize(QSize(260, 90))

        self.gridLayout.addWidget(self.lcd_number_time, 0, 1, 1, 1)

        self.stackedWidget.addWidget(self.home_page)
        self.study_notes_page = QWidget()
        self.study_notes_page.setObjectName(u"study_notes_page")
        sizePolicy3 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.study_notes_page.sizePolicy().hasHeightForWidth())
        self.study_notes_page.setSizePolicy(sizePolicy3)
        self.study_notes_page.setMaximumSize(QSize(16777198, 16777209))
        self.study_notes_page.setStyleSheet(u"")
        self.gridLayout_3 = QGridLayout(self.study_notes_page)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.note_name_combo_box = QComboBox(self.study_notes_page)
        self.note_name_combo_box.setObjectName(u"note_name_combo_box")
        sizePolicy2.setHeightForWidth(self.note_name_combo_box.sizePolicy().hasHeightForWidth())
        self.note_name_combo_box.setSizePolicy(sizePolicy2)
        self.note_name_combo_box.setMinimumSize(QSize(180, 50))

        self.gridLayout_3.addWidget(self.note_name_combo_box, 0, 4, 1, 1)

        self.add_note_button = QPushButton(self.study_notes_page)
        self.add_note_button.setObjectName(u"add_note_button")
        sizePolicy2.setHeightForWidth(self.add_note_button.sizePolicy().hasHeightForWidth())
        self.add_note_button.setSizePolicy(sizePolicy2)
        self.add_note_button.setMinimumSize(QSize(180, 50))

        self.gridLayout_3.addWidget(self.add_note_button, 0, 0, 1, 1)

        self.subject_combo_box = QComboBox(self.study_notes_page)
        self.subject_combo_box.setObjectName(u"subject_combo_box")
        sizePolicy2.setHeightForWidth(self.subject_combo_box.sizePolicy().hasHeightForWidth())
        self.subject_combo_box.setSizePolicy(sizePolicy2)
        self.subject_combo_box.setMinimumSize(QSize(180, 50))

        self.gridLayout_3.addWidget(self.subject_combo_box, 0, 3, 1, 1)

        self.flash_cards_button = QPushButton(self.study_notes_page)
        self.flash_cards_button.setObjectName(u"flash_cards_button")
        sizePolicy2.setHeightForWidth(self.flash_cards_button.sizePolicy().hasHeightForWidth())
        self.flash_cards_button.setSizePolicy(sizePolicy2)
        self.flash_cards_button.setMinimumSize(QSize(180, 50))

        self.gridLayout_3.addWidget(self.flash_cards_button, 0, 5, 1, 1)

        self.study_notes_graphics_view = QGraphicsView(self.study_notes_page)
        self.study_notes_graphics_view.setObjectName(u"study_notes_graphics_view")

        self.gridLayout_3.addWidget(self.study_notes_graphics_view, 1, 0, 1, 7)

        self.lecture_combo_box = QComboBox(self.study_notes_page)
        self.lecture_combo_box.setObjectName(u"lecture_combo_box")
        sizePolicy2.setHeightForWidth(self.lecture_combo_box.sizePolicy().hasHeightForWidth())
        self.lecture_combo_box.setSizePolicy(sizePolicy2)
        self.lecture_combo_box.setMinimumSize(QSize(180, 50))

        self.gridLayout_3.addWidget(self.lecture_combo_box, 0, 1, 1, 1)

        self.questions_button = QPushButton(self.study_notes_page)
        self.questions_button.setObjectName(u"questions_button")
        sizePolicy2.setHeightForWidth(self.questions_button.sizePolicy().hasHeightForWidth())
        self.questions_button.setSizePolicy(sizePolicy2)
        self.questions_button.setMinimumSize(QSize(180, 50))

        self.gridLayout_3.addWidget(self.questions_button, 0, 6, 1, 1)

        self.stackedWidget.addWidget(self.study_notes_page)
        self.add_study_notes_page = QWidget()
        self.add_study_notes_page.setObjectName(u"add_study_notes_page")
        self.gridLayout_4 = QGridLayout(self.add_study_notes_page)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.add_notes_flash_cards_button_2 = QPushButton(self.add_study_notes_page)
        self.add_notes_flash_cards_button_2.setObjectName(u"add_notes_flash_cards_button_2")
        sizePolicy2.setHeightForWidth(self.add_notes_flash_cards_button_2.sizePolicy().hasHeightForWidth())
        self.add_notes_flash_cards_button_2.setSizePolicy(sizePolicy2)
        self.add_notes_flash_cards_button_2.setMinimumSize(QSize(180, 50))

        self.gridLayout_4.addWidget(self.add_notes_flash_cards_button_2, 0, 3, 1, 1)

        self.add_notes_question_button = QPushButton(self.add_study_notes_page)
        self.add_notes_question_button.setObjectName(u"add_notes_question_button")
        sizePolicy2.setHeightForWidth(self.add_notes_question_button.sizePolicy().hasHeightForWidth())
        self.add_notes_question_button.setSizePolicy(sizePolicy2)
        self.add_notes_question_button.setMinimumSize(QSize(180, 50))

        self.gridLayout_4.addWidget(self.add_notes_question_button, 0, 4, 1, 1)

        self.label = QLabel(self.add_study_notes_page)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(14)
        self.label.setFont(font)

        self.gridLayout_4.addWidget(self.label, 1, 0, 1, 1)

        self.lineEdit = QLineEdit(self.add_study_notes_page)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy4)
        self.lineEdit.setMinimumSize(QSize(240, 30))

        self.gridLayout_4.addWidget(self.lineEdit, 1, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(835, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer, 1, 2, 1, 3)

        self.label_2 = QLabel(self.add_study_notes_page)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.gridLayout_4.addWidget(self.label_2, 2, 0, 1, 1)

        self.lineEdit_2 = QLineEdit(self.add_study_notes_page)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        sizePolicy4.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy4)
        self.lineEdit_2.setMinimumSize(QSize(240, 30))

        self.gridLayout_4.addWidget(self.lineEdit_2, 2, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(835, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_2, 2, 2, 1, 3)

        self.label_3 = QLabel(self.add_study_notes_page)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.gridLayout_4.addWidget(self.label_3, 3, 0, 1, 1)

        self.lineEdit_3 = QLineEdit(self.add_study_notes_page)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        sizePolicy4.setHeightForWidth(self.lineEdit_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_3.setSizePolicy(sizePolicy4)
        self.lineEdit_3.setMinimumSize(QSize(240, 30))

        self.gridLayout_4.addWidget(self.lineEdit_3, 3, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(835, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_3, 3, 2, 1, 3)

        self.textEdit = QTextEdit(self.add_study_notes_page)
        self.textEdit.setObjectName(u"textEdit")
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)

        self.gridLayout_4.addWidget(self.textEdit, 4, 0, 1, 5)

        self.add_note_button_2 = QPushButton(self.add_study_notes_page)
        self.add_note_button_2.setObjectName(u"add_note_button_2")
        sizePolicy2.setHeightForWidth(self.add_note_button_2.sizePolicy().hasHeightForWidth())
        self.add_note_button_2.setSizePolicy(sizePolicy2)
        self.add_note_button_2.setMinimumSize(QSize(180, 50))

        self.gridLayout_4.addWidget(self.add_note_button_2, 5, 0, 1, 5)

        self.add_notes_notes_button = QPushButton(self.add_study_notes_page)
        self.add_notes_notes_button.setObjectName(u"add_notes_notes_button")
        sizePolicy2.setHeightForWidth(self.add_notes_notes_button.sizePolicy().hasHeightForWidth())
        self.add_notes_notes_button.setSizePolicy(sizePolicy2)
        self.add_notes_notes_button.setMinimumSize(QSize(180, 50))

        self.gridLayout_4.addWidget(self.add_notes_notes_button, 0, 0, 1, 3)

        self.stackedWidget.addWidget(self.add_study_notes_page)
        self.dictionary_page = QWidget()
        self.dictionary_page.setObjectName(u"dictionary_page")
        self.gridLayout_5 = QGridLayout(self.dictionary_page)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_4 = QLabel(self.dictionary_page)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_5.addWidget(self.label_4, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.dictionary_page)
        self.program_page = QWidget()
        self.program_page.setObjectName(u"program_page")
        self.gridLayout_6 = QGridLayout(self.program_page)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_5 = QLabel(self.program_page)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_6.addWidget(self.label_5, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.program_page)

        self.gridLayout_2.addWidget(self.stackedWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1179, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.dictionary_button.setText(QCoreApplication.translate("MainWindow", u"Dictionary", None))
        self.study_notes_button.setText(QCoreApplication.translate("MainWindow", u"Study Notes", None))
        self.program_button.setText(QCoreApplication.translate("MainWindow", u"Programs", None))
        self.add_note_button.setText(QCoreApplication.translate("MainWindow", u"Not Ekle", None))
        self.flash_cards_button.setText(QCoreApplication.translate("MainWindow", u"Flash Cards ", None))
        self.questions_button.setText(QCoreApplication.translate("MainWindow", u"Questions", None))
        self.add_notes_flash_cards_button_2.setText(QCoreApplication.translate("MainWindow", u"Flash Cards", None))
        self.add_notes_question_button.setText(QCoreApplication.translate("MainWindow", u"Questions", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Ders :", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Konu :", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Not :", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.add_note_button_2.setText(QCoreApplication.translate("MainWindow", u"Not Ekle ", None))
        self.add_notes_notes_button.setText(QCoreApplication.translate("MainWindow", u"Notes", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Dictionary Page", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Program Page", None))
    # retranslateUi

