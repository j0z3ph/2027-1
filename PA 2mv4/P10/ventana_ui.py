# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ventana.ui'
##
## Created by: Qt User Interface Compiler version 6.12.0
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(369, 251)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 20, 321, 131))
        font = QFont()
        font.setFamilies([u"Mi Letra Fea"])
        font.setPointSize(50)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.boton = QPushButton(self.centralwidget)
        self.boton.setObjectName(u"boton")
        self.boton.setGeometry(QRect(90, 140, 181, 71))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Mi primera ventana \U0001faea", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Hola Mundo", None))
        self.boton.setText(QCoreApplication.translate("MainWindow", u"No Tocar", None))
    # retranslateUi

