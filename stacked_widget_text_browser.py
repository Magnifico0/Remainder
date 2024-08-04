# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'stacked_widget_text_browser.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGraphicsView, QGridLayout,
    QLCDNumber, QLabel, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QStatusBar, QTextBrowser,
    QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1277, 796)
        self.actionpages = QAction(MainWindow)
        self.actionpages.setObjectName(u"actionpages")
        self.actionDictionary = QAction(MainWindow)
        self.actionDictionary.setObjectName(u"actionDictionary")
        self.actionStudy_Notes = QAction(MainWindow)
        self.actionStudy_Notes.setObjectName(u"actionStudy_Notes")
        self.actionPrograms = QAction(MainWindow)
        self.actionPrograms.setObjectName(u"actionPrograms")
        self.actionTodays_Words = QAction(MainWindow)
        self.actionTodays_Words.setObjectName(u"actionTodays_Words")
        self.actionOne_Day_Ago = QAction(MainWindow)
        self.actionOne_Day_Ago.setObjectName(u"actionOne_Day_Ago")
        self.actionTwo_Days_Ago = QAction(MainWindow)
        self.actionTwo_Days_Ago.setObjectName(u"actionTwo_Days_Ago")
        self.actionFive_Days_Ago = QAction(MainWindow)
        self.actionFive_Days_Ago.setObjectName(u"actionFive_Days_Ago")
        self.actionSeven_Days_Ago = QAction(MainWindow)
        self.actionSeven_Days_Ago.setObjectName(u"actionSeven_Days_Ago")
        self.actionTen_Days_Ago = QAction(MainWindow)
        self.actionTen_Days_Ago.setObjectName(u"actionTen_Days_Ago")
        self.actionThirty_Days_Ago = QAction(MainWindow)
        self.actionThirty_Days_Ago.setObjectName(u"actionThirty_Days_Ago")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
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
        self.dictionary_display_page = QWidget()
        self.dictionary_display_page.setObjectName(u"dictionary_display_page")
        self.gridLayout_7 = QGridLayout(self.dictionary_display_page)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.sentence_label = QLabel(self.dictionary_display_page)
        self.sentence_label.setObjectName(u"sentence_label")
        font = QFont()
        font.setPointSize(20)
        self.sentence_label.setFont(font)

        self.gridLayout_7.addWidget(self.sentence_label, 3, 0, 1, 1)

        self.dictionary_previous_word_button = QPushButton(self.dictionary_display_page)
        self.dictionary_previous_word_button.setObjectName(u"dictionary_previous_word_button")
        sizePolicy2.setHeightForWidth(self.dictionary_previous_word_button.sizePolicy().hasHeightForWidth())
        self.dictionary_previous_word_button.setSizePolicy(sizePolicy2)
        self.dictionary_previous_word_button.setMinimumSize(QSize(0, 70))
        self.dictionary_previous_word_button.setFont(font)

        self.gridLayout_7.addWidget(self.dictionary_previous_word_button, 5, 5, 1, 1)

        self.dcitionary_sentence_text_browser = QTextBrowser(self.dictionary_display_page)
        self.dcitionary_sentence_text_browser.setObjectName(u"dcitionary_sentence_text_browser")
        sizePolicy2.setHeightForWidth(self.dcitionary_sentence_text_browser.sizePolicy().hasHeightForWidth())
        self.dcitionary_sentence_text_browser.setSizePolicy(sizePolicy2)
        self.dcitionary_sentence_text_browser.setMinimumSize(QSize(0, 70))
        self.dcitionary_sentence_text_browser.setMaximumSize(QSize(16777215, 70))

        self.gridLayout_7.addWidget(self.dcitionary_sentence_text_browser, 3, 1, 1, 6)

        self.dictionary_equivalent_text_browser = QTextBrowser(self.dictionary_display_page)
        self.dictionary_equivalent_text_browser.setObjectName(u"dictionary_equivalent_text_browser")
        sizePolicy2.setHeightForWidth(self.dictionary_equivalent_text_browser.sizePolicy().hasHeightForWidth())
        self.dictionary_equivalent_text_browser.setSizePolicy(sizePolicy2)
        self.dictionary_equivalent_text_browser.setMinimumSize(QSize(0, 70))
        self.dictionary_equivalent_text_browser.setMaximumSize(QSize(16777215, 70))

        self.gridLayout_7.addWidget(self.dictionary_equivalent_text_browser, 4, 1, 1, 6)

        self.dictionary_mean_text_browser = QTextBrowser(self.dictionary_display_page)
        self.dictionary_mean_text_browser.setObjectName(u"dictionary_mean_text_browser")
        sizePolicy2.setHeightForWidth(self.dictionary_mean_text_browser.sizePolicy().hasHeightForWidth())
        self.dictionary_mean_text_browser.setSizePolicy(sizePolicy2)
        self.dictionary_mean_text_browser.setMinimumSize(QSize(0, 70))
        self.dictionary_mean_text_browser.setMaximumSize(QSize(16777215, 70))

        self.gridLayout_7.addWidget(self.dictionary_mean_text_browser, 2, 1, 1, 6)

        self.words_counter_label_all = QLabel(self.dictionary_display_page)
        self.words_counter_label_all.setObjectName(u"words_counter_label_all")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.words_counter_label_all.sizePolicy().hasHeightForWidth())
        self.words_counter_label_all.setSizePolicy(sizePolicy3)
        self.words_counter_label_all.setMinimumSize(QSize(20, 70))
        self.words_counter_label_all.setFont(font)

        self.gridLayout_7.addWidget(self.words_counter_label_all, 5, 3, 1, 2)

        self.equivalent_label = QLabel(self.dictionary_display_page)
        self.equivalent_label.setObjectName(u"equivalent_label")
        self.equivalent_label.setFont(font)

        self.gridLayout_7.addWidget(self.equivalent_label, 4, 0, 1, 1)

        self.words_counter_current_2 = QLabel(self.dictionary_display_page)
        self.words_counter_current_2.setObjectName(u"words_counter_current_2")
        sizePolicy3.setHeightForWidth(self.words_counter_current_2.sizePolicy().hasHeightForWidth())
        self.words_counter_current_2.setSizePolicy(sizePolicy3)
        self.words_counter_current_2.setMinimumSize(QSize(30, 70))
        self.words_counter_current_2.setFont(font)

        self.gridLayout_7.addWidget(self.words_counter_current_2, 5, 2, 1, 1)

        self.mean_label = QLabel(self.dictionary_display_page)
        self.mean_label.setObjectName(u"mean_label")
        self.mean_label.setFont(font)

        self.gridLayout_7.addWidget(self.mean_label, 2, 0, 1, 1)

        self.dictionary_todays_words_button = QPushButton(self.dictionary_display_page)
        self.dictionary_todays_words_button.setObjectName(u"dictionary_todays_words_button")
        sizePolicy2.setHeightForWidth(self.dictionary_todays_words_button.sizePolicy().hasHeightForWidth())
        self.dictionary_todays_words_button.setSizePolicy(sizePolicy2)
        self.dictionary_todays_words_button.setMinimumSize(QSize(0, 70))

        self.gridLayout_7.addWidget(self.dictionary_todays_words_button, 0, 1, 1, 5)

        self.dictionary_word_text_browser = QTextBrowser(self.dictionary_display_page)
        self.dictionary_word_text_browser.setObjectName(u"dictionary_word_text_browser")
        sizePolicy2.setHeightForWidth(self.dictionary_word_text_browser.sizePolicy().hasHeightForWidth())
        self.dictionary_word_text_browser.setSizePolicy(sizePolicy2)
        self.dictionary_word_text_browser.setMinimumSize(QSize(0, 70))
        self.dictionary_word_text_browser.setMaximumSize(QSize(16777215, 70))

        self.gridLayout_7.addWidget(self.dictionary_word_text_browser, 1, 1, 1, 6)

        self.dictionary_today_added_words_button = QPushButton(self.dictionary_display_page)
        self.dictionary_today_added_words_button.setObjectName(u"dictionary_today_added_words_button")
        sizePolicy2.setHeightForWidth(self.dictionary_today_added_words_button.sizePolicy().hasHeightForWidth())
        self.dictionary_today_added_words_button.setSizePolicy(sizePolicy2)
        self.dictionary_today_added_words_button.setMinimumSize(QSize(0, 70))

        self.gridLayout_7.addWidget(self.dictionary_today_added_words_button, 0, 6, 1, 1)

        self.word_label = QLabel(self.dictionary_display_page)
        self.word_label.setObjectName(u"word_label")
        self.word_label.setFont(font)

        self.gridLayout_7.addWidget(self.word_label, 1, 0, 1, 1)

        self.words_counter_label = QLabel(self.dictionary_display_page)
        self.words_counter_label.setObjectName(u"words_counter_label")
        self.words_counter_label.setMinimumSize(QSize(0, 70))
        self.words_counter_label.setFont(font)

        self.gridLayout_7.addWidget(self.words_counter_label, 5, 0, 1, 1)

        self.words_counter_current = QLabel(self.dictionary_display_page)
        self.words_counter_current.setObjectName(u"words_counter_current")
        sizePolicy3.setHeightForWidth(self.words_counter_current.sizePolicy().hasHeightForWidth())
        self.words_counter_current.setSizePolicy(sizePolicy3)
        self.words_counter_current.setMinimumSize(QSize(20, 70))
        self.words_counter_current.setFont(font)

        self.gridLayout_7.addWidget(self.words_counter_current, 5, 1, 1, 1)

        self.dictionary_next_word_button = QPushButton(self.dictionary_display_page)
        self.dictionary_next_word_button.setObjectName(u"dictionary_next_word_button")
        sizePolicy2.setHeightForWidth(self.dictionary_next_word_button.sizePolicy().hasHeightForWidth())
        self.dictionary_next_word_button.setSizePolicy(sizePolicy2)
        self.dictionary_next_word_button.setMinimumSize(QSize(0, 70))
        self.dictionary_next_word_button.setFont(font)

        self.gridLayout_7.addWidget(self.dictionary_next_word_button, 5, 6, 1, 1)

        self.stackedWidget.addWidget(self.dictionary_display_page)
        self.study_notes_page = QWidget()
        self.study_notes_page.setObjectName(u"study_notes_page")
        sizePolicy4 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.study_notes_page.sizePolicy().hasHeightForWidth())
        self.study_notes_page.setSizePolicy(sizePolicy4)
        self.study_notes_page.setMaximumSize(QSize(16777198, 16777209))
        self.study_notes_page.setStyleSheet(u"")
        self.gridLayout_2 = QGridLayout(self.study_notes_page)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.add_note_button = QPushButton(self.study_notes_page)
        self.add_note_button.setObjectName(u"add_note_button")
        sizePolicy2.setHeightForWidth(self.add_note_button.sizePolicy().hasHeightForWidth())
        self.add_note_button.setSizePolicy(sizePolicy2)
        self.add_note_button.setMinimumSize(QSize(180, 50))

        self.gridLayout_2.addWidget(self.add_note_button, 0, 0, 1, 1)

        self.flash_cards_button = QPushButton(self.study_notes_page)
        self.flash_cards_button.setObjectName(u"flash_cards_button")
        sizePolicy2.setHeightForWidth(self.flash_cards_button.sizePolicy().hasHeightForWidth())
        self.flash_cards_button.setSizePolicy(sizePolicy2)
        self.flash_cards_button.setMinimumSize(QSize(180, 50))

        self.gridLayout_2.addWidget(self.flash_cards_button, 0, 4, 1, 1)

        self.note_name_combo_box = QComboBox(self.study_notes_page)
        self.note_name_combo_box.setObjectName(u"note_name_combo_box")
        sizePolicy2.setHeightForWidth(self.note_name_combo_box.sizePolicy().hasHeightForWidth())
        self.note_name_combo_box.setSizePolicy(sizePolicy2)
        self.note_name_combo_box.setMinimumSize(QSize(180, 50))

        self.gridLayout_2.addWidget(self.note_name_combo_box, 0, 3, 1, 1)

        self.questions_button = QPushButton(self.study_notes_page)
        self.questions_button.setObjectName(u"questions_button")
        sizePolicy2.setHeightForWidth(self.questions_button.sizePolicy().hasHeightForWidth())
        self.questions_button.setSizePolicy(sizePolicy2)
        self.questions_button.setMinimumSize(QSize(180, 50))

        self.gridLayout_2.addWidget(self.questions_button, 0, 5, 1, 1)

        self.textBrowser = QTextBrowser(self.study_notes_page)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setInputMethodHints(Qt.ImhNone)
        self.textBrowser.setOpenExternalLinks(True)

        self.gridLayout_2.addWidget(self.textBrowser, 1, 0, 1, 6)

        self.subject_combo_box = QComboBox(self.study_notes_page)
        self.subject_combo_box.setObjectName(u"subject_combo_box")
        sizePolicy2.setHeightForWidth(self.subject_combo_box.sizePolicy().hasHeightForWidth())
        self.subject_combo_box.setSizePolicy(sizePolicy2)
        self.subject_combo_box.setMinimumSize(QSize(180, 50))

        self.gridLayout_2.addWidget(self.subject_combo_box, 0, 2, 1, 1)

        self.lecture_combo_box = QComboBox(self.study_notes_page)
        self.lecture_combo_box.setObjectName(u"lecture_combo_box")
        sizePolicy2.setHeightForWidth(self.lecture_combo_box.sizePolicy().hasHeightForWidth())
        self.lecture_combo_box.setSizePolicy(sizePolicy2)
        self.lecture_combo_box.setMinimumSize(QSize(180, 50))

        self.gridLayout_2.addWidget(self.lecture_combo_box, 0, 1, 1, 1)

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
        font1 = QFont()
        font1.setPointSize(14)
        self.label.setFont(font1)

        self.gridLayout_4.addWidget(self.label, 1, 0, 1, 1)

        self.lineEdit = QLineEdit(self.add_study_notes_page)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy5 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy5)
        self.lineEdit.setMinimumSize(QSize(240, 30))

        self.gridLayout_4.addWidget(self.lineEdit, 1, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(835, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer, 1, 2, 1, 3)

        self.label_2 = QLabel(self.add_study_notes_page)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)

        self.gridLayout_4.addWidget(self.label_2, 2, 0, 1, 1)

        self.lineEdit_2 = QLineEdit(self.add_study_notes_page)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        sizePolicy5.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy5)
        self.lineEdit_2.setMinimumSize(QSize(240, 30))

        self.gridLayout_4.addWidget(self.lineEdit_2, 2, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(835, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_2, 2, 2, 1, 3)

        self.label_3 = QLabel(self.add_study_notes_page)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.gridLayout_4.addWidget(self.label_3, 3, 0, 1, 1)

        self.lineEdit_3 = QLineEdit(self.add_study_notes_page)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        sizePolicy5.setHeightForWidth(self.lineEdit_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_3.setSizePolicy(sizePolicy5)
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
        self.verticalSpacer = QSpacerItem(20, 140, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer, 11, 2, 1, 1)

        self.dictionary_add_word_line_edit = QLineEdit(self.dictionary_page)
        self.dictionary_add_word_line_edit.setObjectName(u"dictionary_add_word_line_edit")
        self.dictionary_add_word_line_edit.setMinimumSize(QSize(0, 35))

        self.gridLayout_5.addWidget(self.dictionary_add_word_line_edit, 3, 3, 1, 1)

        self.dictionary_add_sentence_text_edit = QTextEdit(self.dictionary_page)
        self.dictionary_add_sentence_text_edit.setObjectName(u"dictionary_add_sentence_text_edit")
        self.dictionary_add_sentence_text_edit.setMaximumSize(QSize(16777215, 100))
        self.dictionary_add_sentence_text_edit.setTabChangesFocus(False)

        self.gridLayout_5.addWidget(self.dictionary_add_sentence_text_edit, 10, 3, 1, 1)

        self.dictionary_add_word_button = QPushButton(self.dictionary_page)
        self.dictionary_add_word_button.setObjectName(u"dictionary_add_word_button")
        sizePolicy2.setHeightForWidth(self.dictionary_add_word_button.sizePolicy().hasHeightForWidth())
        self.dictionary_add_word_button.setSizePolicy(sizePolicy2)
        self.dictionary_add_word_button.setMinimumSize(QSize(180, 50))

        self.gridLayout_5.addWidget(self.dictionary_add_word_button, 12, 2, 1, 2)

        self.dictionary_add_equivalent_line_edit = QLineEdit(self.dictionary_page)
        self.dictionary_add_equivalent_line_edit.setObjectName(u"dictionary_add_equivalent_line_edit")
        self.dictionary_add_equivalent_line_edit.setMinimumSize(QSize(0, 35))

        self.gridLayout_5.addWidget(self.dictionary_add_equivalent_line_edit, 9, 3, 1, 1)

        self.dictionary_equivalent_label = QLabel(self.dictionary_page)
        self.dictionary_equivalent_label.setObjectName(u"dictionary_equivalent_label")
        self.dictionary_equivalent_label.setFont(font1)

        self.gridLayout_5.addWidget(self.dictionary_equivalent_label, 9, 1, 1, 1)

        self.dictionary_read_words_button = QPushButton(self.dictionary_page)
        self.dictionary_read_words_button.setObjectName(u"dictionary_read_words_button")
        sizePolicy2.setHeightForWidth(self.dictionary_read_words_button.sizePolicy().hasHeightForWidth())
        self.dictionary_read_words_button.setSizePolicy(sizePolicy2)
        self.dictionary_read_words_button.setMinimumSize(QSize(0, 80))

        self.gridLayout_5.addWidget(self.dictionary_read_words_button, 1, 2, 1, 2)

        self.dictionary_sentence_label = QLabel(self.dictionary_page)
        self.dictionary_sentence_label.setObjectName(u"dictionary_sentence_label")
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.dictionary_sentence_label.sizePolicy().hasHeightForWidth())
        self.dictionary_sentence_label.setSizePolicy(sizePolicy6)
        self.dictionary_sentence_label.setFont(font1)

        self.gridLayout_5.addWidget(self.dictionary_sentence_label, 10, 1, 1, 1)

        self.dictionary_word_label = QLabel(self.dictionary_page)
        self.dictionary_word_label.setObjectName(u"dictionary_word_label")
        self.dictionary_word_label.setFont(font1)

        self.gridLayout_5.addWidget(self.dictionary_word_label, 3, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 100, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_5.addItem(self.verticalSpacer_2, 2, 2, 1, 1)

        self.dictionary_mean_label = QLabel(self.dictionary_page)
        self.dictionary_mean_label.setObjectName(u"dictionary_mean_label")
        self.dictionary_mean_label.setFont(font1)

        self.gridLayout_5.addWidget(self.dictionary_mean_label, 4, 1, 1, 1)

        self.dictionary_add_mean_line_edit = QLineEdit(self.dictionary_page)
        self.dictionary_add_mean_line_edit.setObjectName(u"dictionary_add_mean_line_edit")
        self.dictionary_add_mean_line_edit.setMinimumSize(QSize(0, 35))

        self.gridLayout_5.addWidget(self.dictionary_add_mean_line_edit, 4, 3, 1, 1)

        self.stackedWidget.addWidget(self.dictionary_page)
        self.program_page = QWidget()
        self.program_page.setObjectName(u"program_page")
        self.gridLayout_6 = QGridLayout(self.program_page)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_5 = QLabel(self.program_page)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_6.addWidget(self.label_5, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.program_page)

        self.gridLayout_3.addWidget(self.stackedWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1277, 22))
        self.menuAna_Sayfa = QMenu(self.menubar)
        self.menuAna_Sayfa.setObjectName(u"menuAna_Sayfa")
        self.menuWords = QMenu(self.menubar)
        self.menuWords.setObjectName(u"menuWords")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.dictionary_read_words_button, self.dictionary_add_word_line_edit)
        QWidget.setTabOrder(self.dictionary_add_word_line_edit, self.dictionary_add_mean_line_edit)
        QWidget.setTabOrder(self.dictionary_add_mean_line_edit, self.dictionary_add_equivalent_line_edit)
        QWidget.setTabOrder(self.dictionary_add_equivalent_line_edit, self.dictionary_add_sentence_text_edit)
        QWidget.setTabOrder(self.dictionary_add_sentence_text_edit, self.dictionary_add_word_button)
        QWidget.setTabOrder(self.dictionary_add_word_button, self.questions_button)
        QWidget.setTabOrder(self.questions_button, self.textBrowser)
        QWidget.setTabOrder(self.textBrowser, self.subject_combo_box)
        QWidget.setTabOrder(self.subject_combo_box, self.add_note_button)
        QWidget.setTabOrder(self.add_note_button, self.add_notes_flash_cards_button_2)
        QWidget.setTabOrder(self.add_notes_flash_cards_button_2, self.study_notes_button)
        QWidget.setTabOrder(self.study_notes_button, self.lineEdit_3)
        QWidget.setTabOrder(self.lineEdit_3, self.lineEdit)
        QWidget.setTabOrder(self.lineEdit, self.daily_to_do_list_graphics_view)
        QWidget.setTabOrder(self.daily_to_do_list_graphics_view, self.textEdit)
        QWidget.setTabOrder(self.textEdit, self.add_notes_notes_button)
        QWidget.setTabOrder(self.add_notes_notes_button, self.add_notes_question_button)
        QWidget.setTabOrder(self.add_notes_question_button, self.lineEdit_2)
        QWidget.setTabOrder(self.lineEdit_2, self.add_note_button_2)
        QWidget.setTabOrder(self.add_note_button_2, self.program_button)
        QWidget.setTabOrder(self.program_button, self.dictionary_button)
        QWidget.setTabOrder(self.dictionary_button, self.flash_cards_button)
        QWidget.setTabOrder(self.flash_cards_button, self.lecture_combo_box)
        QWidget.setTabOrder(self.lecture_combo_box, self.note_name_combo_box)

        self.menubar.addAction(self.menuAna_Sayfa.menuAction())
        self.menubar.addAction(self.menuWords.menuAction())
        self.menuAna_Sayfa.addAction(self.actionpages)
        self.menuAna_Sayfa.addSeparator()
        self.menuAna_Sayfa.addAction(self.actionDictionary)
        self.menuAna_Sayfa.addSeparator()
        self.menuAna_Sayfa.addAction(self.actionStudy_Notes)
        self.menuAna_Sayfa.addSeparator()
        self.menuAna_Sayfa.addAction(self.actionPrograms)
        self.menuAna_Sayfa.addSeparator()
        self.menuWords.addSeparator()
        self.menuWords.addAction(self.actionTodays_Words)
        self.menuWords.addSeparator()
        self.menuWords.addAction(self.actionOne_Day_Ago)
        self.menuWords.addSeparator()
        self.menuWords.addAction(self.actionTwo_Days_Ago)
        self.menuWords.addSeparator()
        self.menuWords.addAction(self.actionFive_Days_Ago)
        self.menuWords.addSeparator()
        self.menuWords.addAction(self.actionSeven_Days_Ago)
        self.menuWords.addSeparator()
        self.menuWords.addAction(self.actionTen_Days_Ago)
        self.menuWords.addSeparator()
        self.menuWords.addAction(self.actionThirty_Days_Ago)
        self.menuWords.addSeparator()

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionpages.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.actionDictionary.setText(QCoreApplication.translate("MainWindow", u"Dictionary", None))
        self.actionStudy_Notes.setText(QCoreApplication.translate("MainWindow", u"Study Notes", None))
        self.actionPrograms.setText(QCoreApplication.translate("MainWindow", u"Programs", None))
        self.actionTodays_Words.setText(QCoreApplication.translate("MainWindow", u"Todays Words", None))
        self.actionOne_Day_Ago.setText(QCoreApplication.translate("MainWindow", u"One Day Ago", None))
        self.actionTwo_Days_Ago.setText(QCoreApplication.translate("MainWindow", u"Two Days Ago", None))
        self.actionFive_Days_Ago.setText(QCoreApplication.translate("MainWindow", u"Five Days Ago", None))
        self.actionSeven_Days_Ago.setText(QCoreApplication.translate("MainWindow", u"Seven Days Ago", None))
        self.actionTen_Days_Ago.setText(QCoreApplication.translate("MainWindow", u"Ten Days Ago", None))
        self.actionThirty_Days_Ago.setText(QCoreApplication.translate("MainWindow", u"Thirty Days Ago", None))
        self.dictionary_button.setText(QCoreApplication.translate("MainWindow", u"Dictionary", None))
        self.study_notes_button.setText(QCoreApplication.translate("MainWindow", u"Study Notes", None))
        self.program_button.setText(QCoreApplication.translate("MainWindow", u"Programs", None))
        self.sentence_label.setText(QCoreApplication.translate("MainWindow", u"Sentence : ", None))
        self.dictionary_previous_word_button.setText(QCoreApplication.translate("MainWindow", u"Previous Word", None))
        self.words_counter_label_all.setText(QCoreApplication.translate("MainWindow", u"20", None))
        self.equivalent_label.setText(QCoreApplication.translate("MainWindow", u"Equivalent : ", None))
        self.words_counter_current_2.setText(QCoreApplication.translate("MainWindow", u"  /", None))
        self.mean_label.setText(QCoreApplication.translate("MainWindow", u"Mean : ", None))
        self.dictionary_todays_words_button.setText(QCoreApplication.translate("MainWindow", u"Today's Words", None))
        self.dictionary_today_added_words_button.setText(QCoreApplication.translate("MainWindow", u"Today Added Words", None))
        self.word_label.setText(QCoreApplication.translate("MainWindow", u"Word : ", None))
        self.words_counter_label.setText(QCoreApplication.translate("MainWindow", u"Words : ", None))
        self.words_counter_current.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.dictionary_next_word_button.setText(QCoreApplication.translate("MainWindow", u"Next Word", None))
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
        self.dictionary_add_word_button.setText(QCoreApplication.translate("MainWindow", u"Add Word", None))
        self.dictionary_equivalent_label.setText(QCoreApplication.translate("MainWindow", u"Equivalent:", None))
        self.dictionary_read_words_button.setText(QCoreApplication.translate("MainWindow", u"Read Words", None))
        self.dictionary_sentence_label.setText(QCoreApplication.translate("MainWindow", u"Sentence : ", None))
        self.dictionary_word_label.setText(QCoreApplication.translate("MainWindow", u"Word : ", None))
        self.dictionary_mean_label.setText(QCoreApplication.translate("MainWindow", u"Mean :", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Program Page", None))
        self.menuAna_Sayfa.setTitle(QCoreApplication.translate("MainWindow", u"Sayfalar", None))
        self.menuWords.setTitle(QCoreApplication.translate("MainWindow", u"Words", None))
    # retranslateUi

